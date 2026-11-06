import random
import json
import os
import httpx

PERSONALITY_PROMPTS = {
    "Defensive": "Takes feedback personally, justifies decisions, avoids accepting responsibility, challenges user statements.",
    "Dismissive": "Shows limited interest, gives short responses, minimizes concerns, avoids detailed discussions.",
    "Accepting": "Open-minded, cooperative, receptive to feedback, willing to discuss alternatives.",
    "Random / Unpredictable": "Unexpected responses, changes direction naturally, introduces plausible concerns, creates challenges.",
    "Critical": "Questions assumptions, challenges reasoning, highlights weaknesses, demands evidence."
}

def generate_ai_response(scenario, personality, mode, difficulty, history, user_message):
    context_msgs = [f"{'User' if h['sender'] == 'user' else 'AI'}: {h['content']}" for h in history[-6:]]
    conversation_history = "\n".join(context_msgs)
    
    # Support Omniroute model setup with user-provided defaults
    api_key = os.environ.get("OMNIROUTE_API_KEY") or os.environ.get("OMNIROUTE_KEY") or os.environ.get("OPENAI_API_KEY") or "sk-2579f09f764b7a65-b159f0-2e5bb2"
    base_url = os.environ.get("OMNIROUTE_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or "http://localhost:20128/v1"
    model_name = os.environ.get("OMNIROUTE_MODEL") or os.environ.get("OPENAI_MODEL") or "auto"
    
    if api_key:
        try:
            endpoint = f"{base_url.rstrip('/')}/chat/completions"
            with httpx.Client(timeout=20.0) as client:
                resp = client.post(
                    endpoint,
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": model_name,
                        "messages": [
                            {"role": "system", "content": f"You are {scenario['ai_role']} in scenario: {scenario['title']}. Background: {scenario['background']}. Personality: {PERSONALITY_PROMPTS.get(personality, '')}. Difficulty: {difficulty}. Mode: {mode}. Stay strictly in character. Keep responses 1-3 sentences."},
                            {"role": "user", "content": f"History:\n{conversation_history}\n\nUser: {user_message}\n\nRespond as {scenario['ai_role']}:"}
                        ],
                        "temperature": 0.7,
                        "max_tokens": 200
                    }
                )
                if resp.status_code == 200:
                    data = resp.json()
                    if "choices" in data and len(data["choices"]) > 0:
                        return data["choices"][0]["message"]["content"].strip()
                    elif "reply" in data:
                        return data["reply"].strip()
        except Exception as e:
            print(f"Omniroute API request error ({base_url}): {e}")

    # Enhanced context-aware fallback engine incorporating user input keywords & turns
    turn_count = len([h for h in history if h["sender"] == "user"])
    has_substance = len(user_message.split()) > 3
    
    if personality == "Defensive":
        return f"I note your point about '{user_message[:30]}...', but that overlooks several constraints on my end that weren't addressed." if has_substance else "That's a bit vague. You're putting all the burden on my team without acknowledging dependencies."
    elif personality == "Dismissive":
        return f"Regarding '{user_message[:25]}...', frankly we have more pressing priorities this quarter. Can we revisit later?" if has_substance else "That doesn't give me much detail. Everyone is busy with core deliverables right now."
    elif personality == "Accepting":
        return f"I appreciate you bringing up '{user_message[:30]}...'. That's a constructive perspective. Let's explore how to implement it." if has_substance else "I'm listening. Can you elaborate a bit more on what specific changes you propose?"
    elif personality == "Random / Unpredictable":
        return f"That's interesting regarding '{user_message[:25]}...'. But have you considered how recent department restructuring affects this?" if turn_count % 2 == 1 else "Let's look at this differently. How does this impact our Q3 cost targets?"
    elif personality == "Critical":
        return f"Regarding '{user_message[:30]}...', what concrete evidence or data supports that claim? I need to see metrics." if has_substance else "That claim lacks sufficient justification. Give me an evidence-based example."
    else:
        return f"I hear your point about '{user_message[:25]}...'. Let's discuss further."

def stream_ai_response(scenario, personality, mode, difficulty, history, user_message):
    context_msgs = [f"{'User' if h['sender'] == 'user' else 'AI'}: {h['content']}" for h in history[-6:]]
    conversation_history = "\n".join(context_msgs)
    
    api_key = os.environ.get("OMNIROUTE_API_KEY") or os.environ.get("OMNIROUTE_KEY") or os.environ.get("OPENAI_API_KEY") or "sk-2579f09f764b7a65-b159f0-2e5bb2"
    base_url = os.environ.get("OMNIROUTE_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or "http://localhost:20128/v1"
    model_name = os.environ.get("OMNIROUTE_MODEL") or os.environ.get("OPENAI_MODEL") or "auto"
    
    full_reply = ""
    try:
        endpoint = f"{base_url.rstrip('/')}/chat/completions"
        with httpx.Client(timeout=30.0) as client:
            with client.stream(
                "POST",
                endpoint,
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": f"You are {scenario['ai_role']} in scenario: {scenario['title']}. Background: {scenario['background']}. Personality: {PERSONALITY_PROMPTS.get(personality, '')}. Difficulty: {difficulty}. Mode: {mode}. Stay strictly in character. Keep responses 1-3 sentences."},
                        {"role": "user", "content": f"History:\n{conversation_history}\n\nUser: {user_message}\n\nRespond as {scenario['ai_role']}:"}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 200,
                    "stream": True
                }
            ) as response:
                for line in response.iter_lines():
                    if line.startswith("data: "):
                        data_str = line[6:].strip()
                        if data_str == "[DONE]":
                            break
                        try:
                            cj = json.loads(data_str)
                            delta = cj.get("choices", [{}])[0].get("delta", {}).get("content", "")
                            if delta:
                                full_reply += delta
                                yield delta
                        except Exception:
                            pass
    except Exception:
        pass
        
    if not full_reply:
        fallback = generate_ai_response(scenario, personality, mode, difficulty, history, user_message)
        for char in fallback:
            yield char

def evaluate_simulation(scenario, history):
    criteria = ["Clarity of communication", "Confidence and assertiveness", "Emotional intelligence", "Active listening", "Response quality", "Conflict management", "Persuasion and influence", "Professionalism", "Adaptability", "Achievement of objectives"]
    user_msgs = [h for h in history if h["sender"] == "user"]
    base_score = min(92, max(65, 65 + len(user_msgs) * 4))
    scores = {c: max(60, min(98, base_score + random.randint(-3, 4))) for c in criteria}
    return {
        "overall_score": int(sum(scores.values()) / len(scores)),
        "competency_scores": scores,
        "strengths": ["Maintained a professional tone throughout the interaction.", "Addressed core topics effectively."],
        "missed_opportunities": ["Could have asked clarifying questions earlier."],
        "weak_responses": ["Some statements were slightly tentative."],
        "alternative_responses": ["Try framing as 'Based on these priorities, our recommended next step is...'"],
        "improvement_suggestions": ["Practice active listening by validating constraints."],
        "ideal_conversation_example": f"User: 'I understand constraints. Let's look at a phased approach.'"
    }




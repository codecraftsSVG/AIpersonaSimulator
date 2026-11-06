path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"

part2b_2 = """
<script>
const API = "http://localhost:8000/api";
function app() {
    return {
        dark: localStorage.getItem('dark') === 'true',
        tab: 'dash',
        scenarios: [],
        stats: {},
        selectedSc: null,
        activeSc: null,
        activeSimId: null,
        showModal: false,
        cfg: { mode: 'Roleplay Mode', personality: 'Defensive', difficulty: 'Intermediate' },
        cForm: { title: '', category: 'Workplace Communication', background: '', user_role: 'Employee', ai_role: 'Manager', objective: 'Resolve', difficulty: 'Intermediate', personality: 'Accepting', expected_outcome: 'Done' },
        messages: [],
        inputMsg: '',
        evalData: {},
        isListening: false,
        recognition: null,

        init() {
            if(this.dark) document.documentElement.classList.add('dark');
            this.fetchScenarios(); this.fetchStats(); this.initSpeechRecognition();
        },

        initSpeechRecognition() {
            const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (SR) {
                this.recognition = new SR();
                this.recognition.continuous = false;
                this.recognition.interimResults = false;
                this.recognition.lang = 'en-US';
                this.recognition.onresult = (e) => { this.inputMsg = e.results[0][0].transcript; this.isListening = false; };
                this.recognition.onerror = () => { this.isListening = false; };
                this.recognition.onend = () => { this.isListening = false; };
            }
        },

        toggleVoice() {
            if (!this.recognition) { alert('Speech recognition not supported in browser.'); return; }
            if (this.isListening) { this.recognition.stop(); this.isListening = false; }
            else { this.isListening = true; this.recognition.start(); }
        },

        speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                window.speechSynthesis.speak(u);
            }
        },

        async fetchScenarios() {
            const res = await fetch(`${API}/scenarios`);
            this.scenarios = await res.json();
        },

        async fetchStats() {
            const res = await fetch(`${API}/dashboard/stats`);
            this.stats = await res.json();
        },

        openConfig(sc) {
            this.selectedSc = sc; this.cfg.personality = sc.personality; this.cfg.difficulty = sc.difficulty; this.showModal = true;
        },

        async startSim() {
            this.showModal = false;
            const res = await fetch(`${API}/simulations/start`, {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ scenario_id: this.selectedSc.id, mode: this.cfg.mode, personality: this.cfg.personality, difficulty: this.cfg.difficulty })
            });
            const data = await res.json();
            this.activeSimId = data.simulation_id;
            this.activeSc = data.scenario;
            this.tab = 'chat';
            this.loadMsgs();
        },

        async loadMsgs() {
            const res = await fetch(`${API}/simulations/${this.activeSimId}`);
            const data = await res.json();
            this.messages = data.messages;
            this.scrollToBottom();
        },

        async sendMsg() {
            if(!this.inputMsg.trim()) return;
            const txt = this.inputMsg; this.inputMsg = '';
            this.messages.push({ sender: 'user', content: txt });
            this.scrollToBottom();

            const aiMsg = { sender: 'ai', content: '' };
            this.messages.push(aiMsg);
            this.scrollToBottom();

            try {
                const res = await fetch(`${API}/simulations/${this.activeSimId}/chat-stream`, {
                    method: 'POST', headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ content: txt })
                });

                const reader = res.body.getReader();
                const decoder = new TextDecoder();
                while (true) {
                    const { value, done } = await reader.read();
                    if (done) break;
                    aiMsg.content += decoder.decode(value, { stream: true });
                    this.scrollToBottom();
                }
            } catch (e) {
                aiMsg.content = 'Error receiving AI response.';
            }
        },

        async endSim() {
            const res = await fetch(`${API}/simulations/${this.activeSimId}/end`, { method: 'POST' });
            const data = await res.json();
            this.evalData = data.evaluation;
            this.tab = 'report';
            this.fetchStats();
        },

        async viewReport(id) {
            const res = await fetch(`${API}/simulations/${id}`);
            const data = await res.json();
            this.evalData = data.evaluation || {};
            this.tab = 'report';
        },

        async createCustom() {
            await fetch(`${API}/scenarios`, {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(this.cForm)
            });
            alert('Created successfully!');
            this.tab = 'scenarios';
            this.fetchScenarios();
        },

        scrollToBottom() {
            setTimeout(() => {
                const box = document.getElementById('chat-box');
                if(box) box.scrollTop = box.scrollHeight;
            }, 50);
        }
    }
}
</script>
</body>
</html>
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part2b_2)
print("gen_part2b_2 done")

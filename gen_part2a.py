path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"

part2a = """
        <div x-show="tab === 'custom'" class="max-w-xl mx-auto bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6 space-y-4">
            <h2 class="text-2xl font-bold">Custom Scenario</h2>
            <form @submit.prevent="createCustom" class="space-y-3 text-sm">
                <input type="text" x-model="cForm.title" placeholder="Title" required class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent">
                <select x-model="cForm.category" class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800"><option>Workplace Communication</option><option>Conflict Management</option><option>Leadership</option><option>Negotiation</option><option>Personal Communication</option></select>
                <textarea x-model="cForm.background" placeholder="Background" required class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent" rows="2"></textarea>
                <div class="grid grid-cols-2 gap-2">
                    <input type="text" x-model="cForm.user_role" placeholder="Your Role" required class="px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent">
                    <input type="text" x-model="cForm.ai_role" placeholder="AI Role" required class="px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent">
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <select x-model="cForm.personality" class="px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800"><option>Defensive</option><option>Dismissive</option><option>Accepting</option><option>Random / Unpredictable</option><option>Critical</option></select>
                    <select x-model="cForm.difficulty" class="px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800"><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select>
                </div>
                <input type="text" x-model="cForm.objective" placeholder="Objective" required class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent">
                <input type="text" x-model="cForm.expected_outcome" placeholder="Expected Outcome" required class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-transparent">
                <button type="submit" class="w-full bg-indigo-600 text-white py-2.5 rounded-xl font-medium hover:bg-indigo-700">Create & Start</button>
            </form>
        </div>

        <div x-show="tab === 'chat'" class="h-[calc(100vh-10rem)] flex flex-col bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 overflow-hidden">
            <div class="px-6 py-4 border-b dark:border-slate-700 flex justify-between items-center bg-slate-50 dark:bg-slate-800/80">
                <div><h3 class="font-bold text-sm" x-text="activeSc?.title"></h3><p class="text-xs text-slate-400" x-text="cfg.mode + ' • ' + cfg.personality"></p></div>
                <button @click="endSim()" class="bg-rose-600 text-white px-4 py-2 rounded-xl text-xs font-medium hover:bg-rose-700">End & Evaluate</button>
            </div>
            <div class="flex-1 overflow-y-auto p-6 space-y-4" id="chat-box">
                <template x-for="m in messages">
                    <div :class="m.sender === 'user' ? 'flex justify-end' : 'flex justify-start'">
                        <div :class="m.sender === 'user' ? 'bg-indigo-600 text-white rounded-2xl rounded-tr-sm' : 'bg-slate-100 dark:bg-slate-700 rounded-2xl rounded-tl-sm'" class="max-w-xl px-5 py-3 text-sm shadow-sm relative group">
                            <div class="flex justify-between items-center mb-1">
                                <p class="text-xs font-semibold opacity-75" x-text="m.sender === 'user' ? 'You' : activeSc?.ai_role"></p>
                                <button x-show="m.sender === 'ai'" @click="speak(m.content)" class="text-xs opacity-60 hover:opacity-100 ml-3" title="Read Aloud">🔊</button>
                            </div>
                            <p class="whitespace-pre-wrap" x-text="m.content"></p>
                        </div>
                    </div>
                </template>
            </div>
            <div class="p-4 border-t dark:border-slate-700">
                <form @submit.prevent="sendMsg" class="flex space-x-2 items-center">
                    <button type="button" @click="toggleVoice()" :class="isListening ? 'bg-rose-600 text-white animate-pulse' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-200'" class="p-3 rounded-xl text-sm transition" title="Voice Input (Speech-to-Text)">🎤</button>
                    <input type="text" x-model="inputMsg" placeholder="Type or click mic to speak..." required class="flex-1 px-4 py-3 rounded-xl border dark:border-slate-700 bg-slate-50 dark:bg-slate-900 text-sm">
                    <button type="submit" class="bg-indigo-600 text-white px-6 py-3 rounded-xl text-sm font-medium hover:bg-indigo-700">Send</button>
                </form>
            </div>
        </div>
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part2a)
print("gen_part2a done")

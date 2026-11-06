path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"
part3a = """
        <div x-show="tab === 'chat'" class="h-[calc(100vh-10rem)] flex flex-col bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 overflow-hidden">
            <div class="px-6 py-4 border-b dark:border-slate-700 flex justify-between items-center bg-slate-50 dark:bg-slate-800/80">
                <div><h3 class="font-bold text-sm" x-text="activeSc?.title"></h3><p class="text-xs text-slate-400" x-text="cfg.mode + ' • ' + cfg.personality"></p></div>
                <button @click="endSim()" class="bg-rose-600 text-white px-4 py-2 rounded-xl text-xs font-medium hover:bg-rose-700">End & Evaluate</button>
            </div>
            <div class="flex-1 overflow-y-auto p-6 space-y-4" id="chat-box">
                <template x-for="m in messages">
                    <div :class="m.sender === 'user' ? 'flex justify-end' : 'flex justify-start'">
                        <div :class="m.sender === 'user' ? 'bg-indigo-600 text-white rounded-2xl rounded-tr-sm' : 'bg-slate-100 dark:bg-slate-700 rounded-2xl rounded-tl-sm'" class="max-w-xl px-5 py-3 text-sm shadow-sm">
                            <p class="text-xs font-semibold opacity-75 mb-1" x-text="m.sender === 'user' ? 'You' : activeSc?.ai_role"></p>
                            <p class="whitespace-pre-wrap" x-text="m.content"></p>
                        </div>
                    </div>
                </template>
            </div>
            <div class="p-4 border-t dark:border-slate-700">
                <form @submit.prevent="sendMsg" class="flex space-x-2">
                    <input type="text" x-model="inputMsg" placeholder="Type response..." required class="flex-1 px-4 py-3 rounded-xl border dark:border-slate-700 bg-slate-50 dark:bg-slate-900 text-sm">
                    <button type="submit" class="bg-indigo-600 text-white px-6 py-3 rounded-xl text-sm font-medium">Send</button>
                </form>
            </div>
        </div>

        <div x-show="tab === 'report'" class="space-y-6 max-w-3xl mx-auto">
            <div class="flex justify-between items-center"><h2 class="text-2xl font-bold">Evaluation Report</h2><button @click="tab = 'dash'" class="bg-indigo-600 text-white px-4 py-2 rounded-xl text-sm">Dashboard</button></div>
            <div class="bg-indigo-600 text-white rounded-2xl p-6 flex justify-between items-center">
                <div><p class="text-xs uppercase opacity-80">Overall Score</p><h3 class="text-4xl font-extrabold mt-1" x-text="(evalData.overall_score || 0) + '/100'"></h3></div>
                <div class="bg-white/10 px-4 py-2 rounded-xl text-sm font-semibold">Passed</div>
            </div>
            <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6 space-y-4">
                <h3 class="font-bold">Competency Scores</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <template x-for="(score, comp) in (evalData.competency_scores || {})">
                        <div class="p-3 bg-slate-50 dark:bg-slate-700/40 rounded-xl">
                            <div class="flex justify-between text-xs font-semibold mb-1"><span x-text="comp"></span><span class="text-indigo-600" x-text="score"></span></div>
                            <div class="w-full bg-slate-200 dark:bg-slate-600 h-2 rounded-full"><div class="bg-indigo-600 h-2 rounded-full" :style="'width: ' + score + '%'"></div></div>
                        </div>
                    </template>
                </div>
            </div>
        </div>
    </main>
</div>
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part3a)
print("p3a")

path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"

part2b_1 = """
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

<div x-show="showModal" class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
    <div @click.away="showModal = false" class="bg-white dark:bg-slate-800 rounded-2xl p-6 max-w-md w-full space-y-4 shadow-xl">
        <h3 class="text-lg font-bold">Configure Simulation</h3>
        <select x-model="cfg.mode" class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800 text-sm"><option>Roleplay Mode</option><option>Practice Mode</option><option>Guided Mode</option></select>
        <select x-model="cfg.personality" class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800 text-sm"><option>Defensive</option><option>Dismissive</option><option>Accepting</option><option>Random / Unpredictable</option><option>Critical</option></select>
        <select x-model="cfg.difficulty" class="w-full px-3 py-2 rounded-xl border dark:border-slate-700 bg-white dark:bg-slate-800 text-sm"><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select>
        <div class="flex space-x-2">
            <button @click="showModal = false" class="flex-1 bg-slate-100 dark:bg-slate-700 py-2 rounded-xl text-sm">Cancel</button>
            <button @click="startSim()" class="flex-1 bg-indigo-600 text-white py-2 rounded-xl text-sm">Start</button>
        </div>
    </div>
</div>
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part2b_1)
print("gen_part2b_1 done")

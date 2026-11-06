path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"
part2 = """
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-8">
        <div x-show="tab === 'dash'" class="space-y-6">
            <div class="flex justify-between items-center">
                <div><h2 class="text-2xl font-bold">Dashboard</h2><p class="text-sm text-slate-500">Practice communication skills.</p></div>
                <button @click="tab = 'scenarios'" class="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium">Start Simulation</button>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Completed</p><p class="text-3xl font-extrabold text-indigo-600 mt-2" x-text="stats.total_simulations || 0">0</p></div>
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Average Score</p><p class="text-3xl font-extrabold text-emerald-600 mt-2" x-text="(stats.average_score || 0) + '%'">0%</p></div>
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Trend</p><p class="text-3xl font-extrabold text-blue-600 mt-2">Active 🚀</p></div>
            </div>
            <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6">
                <h3 class="font-bold mb-4">Recent History</h3>
                <template x-for="s in stats.recent_simulations" :key="s.id">
                    <div class="py-3 border-b dark:border-slate-700 flex justify-between items-center cursor-pointer px-2 rounded" @click="viewReport(s.id)">
                        <div><p class="font-medium text-sm" x-text="s.title"></p><p class="text-xs text-slate-400" x-text="s.mode + ' • ' + s.personality"></p></div>
                        <span class="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800" x-text="s.overall_score + '/100'"></span>
                    </div>
                </template>
            </div>
        </div>

        <div x-show="tab === 'scenarios'" class="space-y-6">
            <h2 class="text-2xl font-bold">Scenario Library</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <template x-for="sc in scenarios" :key="sc.id">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6 flex flex-col justify-between">
                        <div>
                            <span class="px-2 py-0.5 rounded text-xs font-semibold bg-indigo-50 text-indigo-600" x-text="sc.category"></span>
                            <h3 class="font-bold text-base mt-2 mb-2" x-text="sc.title"></h3>
                            <p class="text-xs text-slate-500 line-clamp-3 mb-4" x-text="sc.background"></p>
                        </div>
                        <button @click="openConfig(sc)" class="w-full bg-indigo-600 text-white font-medium py-2 rounded-xl text-sm">Configure & Start</button>
                    </div>
                </template>
            </div>
        </div>

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
                <button type="submit" class="w-full bg-indigo-600 text-white py-2.5 rounded-xl font-medium">Create & Start</button>
            </form>
        </div>
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part2)
print("p2")

with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <title>AI Conversation Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script>tailwind.config = { darkMode: 'class' }</script>
</head>
<body class="h-full bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 font-sans" x-data="app()" x-init="init()">
<div class="min-h-screen flex flex-col">
    <header class="bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3 cursor-pointer" @click="tab = 'dash'">
                <div class="bg-indigo-600 text-white p-2 rounded-xl font-bold">AI</div>
                <h1 class="font-bold text-lg">ConvSimulator</h1>
            </div>
            <nav class="hidden md:flex space-x-1">
                <button @click="tab = 'dash'" :class="tab === 'dash' ? 'bg-indigo-50 text-indigo-600 dark:bg-indigo-900/40 dark:text-indigo-400 font-semibold' : 'text-slate-600 dark:text-slate-300'" class="px-3 py-2 rounded-lg text-sm">Dashboard</button>
                <button @click="tab = 'scenarios'" :class="tab === 'scenarios' ? 'bg-indigo-50 text-indigo-600 dark:bg-indigo-900/40 dark:text-indigo-400 font-semibold' : 'text-slate-600 dark:text-slate-300'" class="px-3 py-2 rounded-lg text-sm">Scenarios</button>
                <button @click="tab = 'custom'" :class="tab === 'custom' ? 'bg-indigo-50 text-indigo-600 dark:bg-indigo-900/40 dark:text-indigo-400 font-semibold' : 'text-slate-600 dark:text-slate-300'" class="px-3 py-2 rounded-lg text-sm">Custom Builder</button>
            </nav>
            <button @click="dark = !dark; localStorage.setItem('dark', dark); document.documentElement.classList.toggle('dark', dark)" class="p-2 rounded-lg bg-slate-100 dark:bg-slate-700" x-text="dark ? '☀️' : '🌙'"></button>
        </div>
    </header>
""")
print("Part 1 written")

with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "a", encoding="utf-8") as f:
    f.write("""
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-8">
        <div x-show="tab === 'dash'" class="space-y-6">
            <div class="flex justify-between items-center">
                <div><h2 class="text-2xl font-bold">Dashboard</h2><p class="text-sm text-slate-500">Practice communication skills.</p></div>
                <button @click="tab = 'scenarios'" class="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700">Start Simulation</button>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Completed</p><p class="text-3xl font-extrabold text-indigo-600 mt-2" x-text="stats.total_simulations || 0">0</p></div>
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Average Score</p><p class="text-3xl font-extrabold text-emerald-600 mt-2" x-text="(stats.average_score || 0) + '%'">0%</p></div>
                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border dark:border-slate-700"><p class="text-xs font-semibold text-slate-400 uppercase">Trend</p><p class="text-3xl font-extrabold text-blue-600 mt-2">Active 🚀</p></div>
            </div>
            <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6">
                <h3 class="font-bold mb-4">Recent History</h3>
                <template x-for="s in stats.recent_simulations" :key="s.id">
                    <div class="py-3 border-b dark:border-slate-700 flex justify-between items-center cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-700/50 px-2 rounded" @click="viewReport(s.id)">
                        <div><p class="font-medium text-sm" x-text="s.title"></p><p class="text-xs text-slate-400" x-text="s.mode + ' • ' + s.personality"></p></div>
                        <span class="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300" x-text="s.overall_score + '/100'"></span>
                    </div>
                </template>
            </div>
        </div>
""")
print("Part 2 written")

with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "a", encoding="utf-8") as f:
    f.write("""
        <div x-show="tab === 'scenarios'" class="space-y-6">
            <h2 class="text-2xl font-bold">Scenario Library</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <template x-for="sc in scenarios" :key="sc.id">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6 flex flex-col justify-between">
                        <div>
                            <span class="px-2.5 py-0.5 rounded text-xs font-semibold bg-indigo-50 dark:bg-indigo-900/40 text-indigo-600" x-text="sc.category"></span>
                            <h3 class="font-bold text-base mt-2 mb-2" x-text="sc.title"></h3>
                            <p class="text-xs text-slate-500 dark:text-slate-400 line-clamp-3 mb-4" x-text="sc.background"></p>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mb-4">🤖 AI: <span x-text="sc.ai_role"></span> (<span x-text="sc.personality"></span>)</p>
                        </div>
                        <button @click="openConfig(sc)" class="w-full bg-indigo-600 text-white font-medium py-2 rounded-xl text-sm hover:bg-indigo-700">Configure & Start</button>
                    </div>
                </template>
            </div>
        </div>
""")
print("Scenarios part written")

with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "a", encoding="utf-8") as f:
    f.write("""
        <div x-show="tab === 'scenarios'" class="space-y-6">
            <h2 class="text-2xl font-bold">Scenario Library</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <template x-for="sc in scenarios" :key="sc.id">
with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "a", encoding="utf-8") as f:
    f.write("""
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
                    <button type="submit" class="bg-indigo-600 text-white px-6 py-3 rounded-xl text-sm font-medium hover:bg-indigo-700">Send</button>
                </form>
            </div>
        </div>
    </main>
</div>
""")
print("Chat part written")
with open(r"c:\Users\user\Downloads\ai-conversation-simulator\frontend\index.html", "a", encoding="utf-8") as f:
    f.write("""
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
        init() {
            if(this.dark) document.documentElement.classList.add('dark');
            this.fetchScenarios(); this.fetchStats();
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
            this.messages.push({sender: 'user', content: txt});
            this.scrollToBottom();
            const res = await fetch(`${API}/simulations/${this.activeSimId}/chat`, {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content: txt})
            });
            const data = await res.json();
            this.messages.push({sender: 'ai', content: data.ai_message});
            this.scrollToBottom();
        },
        async endSim() {
            const res = await fetch(`${API}/simulations/${this.activeSimId}/end`, {method: 'POST'});
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
""")
print("Final part written successfully!")


                    <div class="bg-white dark:bg-slate-800 rounded-2xl border dark:border-slate-700 p-6 flex flex-col justify-between">
                        <div>
                            <span class="px-2.5 py-0.5 rounded text-xs font-semibold bg-indigo-50 dark:bg-indigo-900/40 text-indigo-600" x-text="sc.category"></span>
                            <h3 class="font-bold text-base mt-2 mb-2" x-text="sc.title"></h3>
                            <p class="text-xs text-slate-500 dark:text-slate-400 line-clamp-3 mb-4" x-text="sc.background"></p>
                            <p class="text-xs text-slate-600 dark:text-slate-300 mb-4">🤖 AI: <span x-text="sc.ai_role"></span> (<span x-text="sc.personality"></span>)</p>
                        </div>
                        <button @click="openConfig(sc)" class="w-full bg-indigo-600 text-white font-medium py-2 rounded-xl text-sm hover:bg-indigo-700">Configure & Start</button>
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
                <button type="submit" class="w-full bg-indigo-600 text-white py-2.5 rounded-xl font-medium hover:bg-indigo-700">Create & Start</button>
            </form>
        </div>
""")
print("Part 3 written")

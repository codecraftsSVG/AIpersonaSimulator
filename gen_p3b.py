path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"
part3b = """
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
"""
with open(path, "a", encoding="utf-8") as f:
    f.write(part3b)
print("p3b")

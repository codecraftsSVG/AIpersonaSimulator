path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"

part1 = """<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <title>AI Conversation Simulator - Stream & Voice</title>
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

    <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-8">
        <div x-show="tab === 'dash'" class="space-y-6">
            <div class="flex justify-between items-center">
                <div><h2 class="text-2xl font-bold">Dashboard</h2><p class="text-sm text-slate-500">Practice with real-time streaming & voice support.</p></div>
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
                        <button @click="openConfig(sc)" class="w-full bg-indigo-600 text-white font-medium py-2 rounded-xl text-sm hover:bg-indigo-700">Configure & Start</button>
                    </div>
                </template>
            </div>
        </div>
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(part1)
print("gen_part1 done")

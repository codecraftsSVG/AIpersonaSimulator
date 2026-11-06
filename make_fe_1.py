import os

path = "c:/Users/user/Downloads/ai-conversation-simulator/frontend/index.html"

part1 = """<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <title>AI Conversation Simulator - Streaming & Voice</title>
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
"""
with open(path, "w", encoding="utf-8") as f:
    f.write(part1)
print("p1")

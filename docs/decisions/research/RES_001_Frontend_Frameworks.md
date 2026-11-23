# RES-001: Front-end framework findings (with Laravel)

| Item | Value |
| --- | --- |
| Document ID | RES-001 |
| Document type | Research note (findings only) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.3 |
| Status | Draft. Findings only. The owner's stack (Laravel, Inertia, Vue 3, TypeScript) is recorded in [ADR-001](../ADR_001_Language_And_Framework.md), still Proposed. |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (PWA requirements: offline, install, sync) |
| Source | Owner prompt P-22; asked by Owner (Champs) |
| Change tracking | [REG-01 History log](../../registers/REG_01_History_Log.md) |
| Scope | Which front-end option fits a Laravel back end for the offline-first PWA (Tax Relief Manager). |

## 1. The six options

| # | Option | How it works with Laravel | Good for | Watch out for |
| --- | --- | --- | --- | --- |
| 1 | Laravel Blade (with Alpine.js) | Laravel builds each page as HTML on the server. Alpine.js adds small browser behaviour. A click normally loads a new page. | Simplest, one codebase, quick to build, good for forms | Weak for offline use and for a live calculator |
| 2 | Livewire | Written in PHP: a PHP class plus a Blade view. Parts of the page update without a reload, through the server. | Laravel developers who want interactive screens without a JavaScript framework | Every interaction needs the server, so offline use is limited |
| 3 | Vue 3 (with Inertia.js) | A Vue app inside Laravel. Inertia replaces the API: controllers send data as props. It can also run as a separate app on a Laravel API. | Smooth app feel, good PWA and offline support, gentle learning curve | Maintaining Vue and PHP together |
| 4 | React (with Inertia.js) | The same pattern as Vue | Largest ecosystem, easiest hiring | Steeper learning curve, many choices to make |
| 5 | Angular | A separate app talking to a Laravel API | Large structured teams, strong built-in forms and validation, official PWA add-on | Heavy, two codebases, a full API to build |
| 6 | Svelte (SvelteKit or Inertia) | A separate app, or Inertia with the official Svelte adapter | Small, fast, least code | Smaller ecosystem, fewer developers |

## 2. Blade compared with options 3 to 6

| | Blade and Livewire | Vue, React, Svelte, Angular |
| --- | --- | --- |
| Where the screen is built | On the server | In the browser |
| Navigation | New page or server round trip | Instant, inside the app |
| Offline use | Weak | Good, with a service worker and cached data |
| Live calculation while typing | Needs the server | Runs in the browser |
| Languages to maintain | PHP (and a little JavaScript) | PHP and JavaScript or TypeScript |

## 3. What Inertia.js is

- Without Inertia, a React or Vue app needs a full REST API from Laravel, a client router, login handling and API calls for every screen.
- With Inertia, a Laravel controller returns `Inertia::render('Page', $data)` and the data arrives in the component as props. Laravel keeps the routes, login, validation and policies. There is one codebase and no duplicated rules.
- It works with JavaScript or TypeScript. The official Laravel React starter kit uses TypeScript.
- Redux can be used with React and Inertia, but most data already arrives as props. Redux Toolkit or Zustand is for browser-only state, such as an unsaved calculator. The store survives page changes because Inertia does not reload the page.

## 4. Vue 3 and Vue.js

- Vue.js is the framework. Vue 3 is its current major version (2020). Vue 2 stopped receiving updates in December 2023.

| | Vue 2 | Vue 3 |
| --- | --- | --- |
| Code style | Options API | Composition API (`<script setup>`) |
| TypeScript | Weak | Strong |
| State library | Vuex | Pinia |
| Build tool | Webpack | Vite |
| Speed and size | Slower | Faster and smaller |

- For TRM, always Vue 3.

## 5. React, Vue 3 and Svelte side by side

The same screen in each: an income box and a tax figure. The 10% is only an illustration, not a tax rate.

React:

```jsx
import { useState } from 'react'

export default function Calc() {
  const [income, setIncome] = useState(0)
  const tax = income * 0.1
  return (
    <>
      <input type="number" value={income}
             onChange={e => setIncome(Number(e.target.value))} />
      <p>Tax: RM {tax}</p>
    </>
  )
}
```

Vue 3:

```vue
<script setup>
import { ref, computed } from 'vue'
const income = ref(0)
const tax = computed(() => income.value * 0.1)
</script>

<template>
  <input type="number" v-model.number="income" />
  <p>Tax: RM {{ tax }}</p>
</template>
```

Svelte 5:

```svelte
<script>
  let income = $state(0)
  let tax = $derived(income * 0.1)
</script>

<input type="number" bind:value={income} />
<p>Tax: RM {tax}</p>
```

| | React | Vue 3 | Svelte |
| --- | --- | --- | --- |
| Idea | The screen is a function of its data. React works out the changes. | Data is reactive. Vue updates only what a screen reads. | A compiler turns the file into small plain JavaScript at build time. |
| Two-way input | Manual (`value` plus `onChange`) | Built in (`v-model`) | Built in (`bind:value`) |
| Derived values | Calculated each render, or `useMemo` | `computed` | `$derived` |
| Shared state | Redux Toolkit, Zustand or Context | Pinia (official) | Built-in shared state or stores |
| Routing and forms | Your choice of library | Official router, many form libraries | SvelteKit, or Inertia in Laravel |
| TypeScript | Excellent | Excellent | Excellent |
| Learning curve | Medium, many choices | Gentle, clear conventions | Gentle, least code |
| Ecosystem and hiring | Largest | Large | Small, growing |
| Bundle size | Larger | Medium | Smallest |

## 6. Svelte in more detail

- Most frameworks ship a library that runs in the browser and works out what changed. Svelte is a compiler: it turns components into small plain JavaScript when you build, so little framework code reaches the user.
- Strengths: less code, very small bundle (good on slow phones), easy to read, built-in transitions, SvelteKit for routing and server rendering, an official Inertia adapter.
- Weaknesses: much smaller ecosystem (fewer ready-made components and tutorials), fewer developers, and Svelte 5 changed its reactivity syntax, so older tutorials may not match.

## 7. PWA and offline

- All three can be a PWA. Vue and React use the Vite PWA plugin, SvelteKit has a similar setup, and Angular has an official add-on.
- Offline behaviour depends on how data is cached and synced, not on the framework.
- Blade and Livewire render on the server, so offline use is limited.

## 8. Reading for TRM (a reading, not a decision)

| Choice | When it fits |
| --- | --- |
| Vue 3 with Inertia | Safest fit: familiar to the owner, quick to build, works with Laravel and a PWA |
| React with Inertia | If hiring or teammates who already use React matter more |
| Svelte | If the lightest app matters and the team accepts the learning cost |
| Livewire | If the team wants to stay in PHP and accepts limited offline use |
| Angular | If a strict structure and a separate API are wanted |
| Blade | Not enough for the live calculator and offline use |

The live tax calculator, the dashboard and offline use favour options 3 to 6.

## 9. Open

- The language and framework are not decided (ADR-001). Laravel is the owner's working assumption for the back end, not a recorded decision.
- Record the owner's choice in ADR-001 as "proposed" first, then "approved" with the date.

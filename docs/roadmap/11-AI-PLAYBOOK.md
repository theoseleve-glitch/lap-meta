# LAP — AI Tool Playbook

You're solo + heavy AI-assisted (Claude Code x20, Codex, Copilot, Figma, Claude Design). This document maps **which AI for which task** so you don't burn context on mismatched tools.

---

## Tool roster & role

| Tool | Best at | Cost profile (yours) | Token / call budget |
|---|---|---|---|
| **Claude Code (Opus)** | Architecture, complex refactors, multi-file reasoning, writing coaching rules, writing long-form copy, designing algorithms | Pro subscription (unlimited within tier) | High — expensive per call, use for decisions |
| **Claude Code (Sonnet)** | Production code implementation, straightforward refactors, tests, Pydantic models, API clients | Pro subscription | Medium |
| **Claude Code (Haiku)** | Quick edits, formatting, small typing fixes, generating one-off scripts | Pro subscription (dirt cheap) | Low — use for boilerplate |
| **Codex / Copilot** | Inline completion, boilerplate, test scaffolding, mechanical moves (file renames, import updates), shell scripts | Pro sub | Free-ish — use heavily |
| **Figma + Claude Design** | UI mockups, component design, brand consistency, interactive prototypes, visual hierarchy decisions | €21K credits you have | Design-focused |
| **Cursor / Zed (AI-native editor)** | Multi-file edits with AI assistance, refactors across repos | Part of Codex/Copilot setup | Editor-level |

---

## Decision tree: which AI for this task?

```
Task starts
    │
    ├── Is it a design decision / architecture choice? 
    │   └── YES → Claude Code Opus (or sometimes deep chat with Sonnet)
    │
    ├── Is it visual / UI layout / brand?
    │   └── YES → Figma + Claude Design → implement with Claude Sonnet
    │
    ├── Is it production business logic (coaching rules, 
    │   prescription generator, transfer algorithm)?
    │   └── YES → Claude Opus (design) + Sonnet (implementation)
    │
    ├── Is it a CRUD endpoint / typed API client / Pydantic model?
    │   └── YES → Sonnet
    │
    ├── Is it mechanical (rename X to Y, update imports, 
    │   regenerate schemas)?
    │   └── YES → Codex or Haiku
    │
    ├── Is it a test (unit or integration)?
    │   └── YES → Sonnet or Codex, review with Opus
    │
    ├── Is it long-form writing (blog post, release notes)?
    │   └── YES → Opus (draft) → you edit
    │
    └── Is it documentation?
        └── YES → Sonnet
```

---

## Per-task-type AI mapping

### Backend (FastAPI, Pydantic, Celery)

| Task type | Primary AI | Secondary | Notes |
|---|---|---|---|
| New domain model design | Opus | — | Sketches class hierarchy, relationships |
| Pydantic v2 model from ADR | Sonnet | Codex for boilerplate | Has ADR field list, straightforward |
| FastAPI router implementation | Sonnet | — | Well-worn territory |
| Celery task + queue design | Opus | Sonnet to implement | |
| Alembic migration | Sonnet | Codex | Reviewable diff |
| Coaching rule YAML authoring | Opus | You review every rule | Opus has best judgment for rule quality |
| Rules engine runtime | Opus | Sonnet | Algorithm design matters |
| Transfer-link shape/intensity math | Opus | Sonnet | Algorithm choice is load-bearing |
| Unit tests | Sonnet or Codex | — | |
| Integration tests | Sonnet | | |

### Webapp (Next.js, React, TanStack Query)

| Task type | Primary AI | Secondary | Notes |
|---|---|---|---|
| Driver Timeline / Profile / Compare page | Claude Design (visual) → Opus (component architecture) → Sonnet (code) | Codex for boilerplate | These are high-visibility pages — plan with Opus |
| Typed API hook generation | Codex | — | Mechanical from generated TS types |
| Tailwind utility migration | Codex / Haiku | — | Boring but safe |
| Form validation (Zod / Pydantic-synced) | Sonnet | — | |
| Onboarding flow | Claude Design first | — | UX decisions matter most |
| Accessibility pass | Sonnet | — | Specific audit checklist |

### Desktop (Qt/QML, Python)

| Task type | Primary AI | Secondary | Notes |
|---|---|---|---|
| QML component design | Claude Design (if new) → Sonnet (code) | — | |
| VM / service refactor | Opus | Sonnet | `live_telemetry_processor` rewrite is Opus territory |
| iRacing SDK integration | Sonnet | Opus if tricky | |
| Overlay stack engineering | Sonnet | — | Has a good template already |
| PyInstaller + Inno Setup | Codex | — | Mechanical |

### Mobile (Swift / Kotlin)

| Task type | Primary AI | Secondary | Notes |
|---|---|---|---|
| iOS SwiftUI view | Claude Design → Sonnet | — | |
| Kotlin Compose view | Sonnet | — | |
| BLE protocol (UBX parser) | Opus (design) → Sonnet | — | State machine design is Opus |
| Capture journal / upload queue | Opus (design) → Sonnet | — | Critical reliability code |
| Failure-injection test suite | Sonnet | Codex | Important to write carefully |

### Marketing / Content

| Task type | Primary AI | Secondary | Notes |
|---|---|---|---|
| Homepage copy (positioning) | Opus | You edit heavily | High-stakes copy |
| Blog post (long-form) | Opus (draft) → you edit | | |
| SEO pillar page | Opus | | 3000+ words, Opus has best structure |
| Product tour / onboarding copy | Opus | | |
| Social posts | Sonnet | | |
| Press kit | Opus | | |

---

## Prompt patterns (for this project specifically)

### Pattern 1: "Write a backend feature from ADR"

```
You are writing code for lap-backend. Read the ADR first: 
[paste ADR from docs/roadmap/02-ARCHITECTURE-DECISIONS.md]

Task: implement [feature name].

Constraints:
- Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0
- Server owns the brain — no client-delegated logic
- All IDs are UUIDv7
- All timestamps UTC RFC3339
- Schema types imported from lap-schemas

Produce:
1. Pydantic models (if new)
2. Router endpoint(s)
3. Service layer (pure business logic)
4. Repository layer (DB access)
5. Tests
6. Alembic migration if needed

Match file structure of existing `app/` directory.
```

### Pattern 2: "Author a coaching rule"

```
Author a coaching library rule for this weakness: [description].

Output YAML matching the schema in ADR-013.

Test data available: 
[list 3 sessions from LapCoachLogger_sessions/ that exhibit this weakness]

Rule must:
- Have beginner + intermediate + advanced explanation templates
- Link to a drill template (or request creation if none exists)
- Define a measurable success condition
- Specify required channels
- Describe sim-vs-real transfer behavior

Return YAML + brief rationale for thresholds.
```

### Pattern 3: "Refactor for contract compliance"

```
Refactor [file] to use types from @lap/schemas instead of local definitions.

Old type: [paste]
New type (from @lap/schemas): [paste]

Constraints:
- Do not change behavior
- Update import path
- Replace every usage of the old type
- If fields differ, identify drift and report — do not silently adapt
```

### Pattern 4: "Debug with Sentry context"

```
I have a Sentry error: [paste title + stack + frequency].

Environment: [production / staging / dev].
Affected users: [count].
First seen: [date].

Read the stack trace. Identify:
1. Root cause (one-liner)
2. Fix (one-liner)
3. Why our tests missed it
4. Test to add so it never recurs
```

### Pattern 5: "Review a PR I wrote"

```
Review this diff as if you were a senior staff engineer who owns this repo.

Focus:
- Contract violations (types, API shapes)
- Concurrency / race conditions / idempotency
- Observability (are errors surfaced? is it instrumentable?)
- Test coverage of failure modes
- Drift from documented conventions in CLAUDE.md

Don't comment on style (linter handles that). Don't suggest unrelated refactors.

[paste diff]
```

---

## Context management (critical for solo+AI velocity)

Claude Code x20 means you have headroom, but don't waste it.

**Rules:**
1. **Per-project CLAUDE.md is your single source of truth.** Keep it <200 lines, updated weekly. Links to the ADRs, not inlined content.
2. **Never re-read a file you just edited** unless you're unsure the edit applied. The tool confirms success.
3. **Read one directory, not the whole repo** when answering a narrow question.
4. **Use Grep to target** when looking for patterns. Don't ask AI to scan the repo visually.
5. **Agent delegation for independent sub-tasks**, especially when a task would pollute your main context window (e.g., "rewrite this 20-file test suite").
6. **When debugging, include the exact error + last 50 lines of log.** AI context is small compared to the problem.
7. **When designing, reference the ADR by name.** "Per ADR-005 §5.2…" is better than pasting 500 lines of prose.

---

## When to stop the AI and code yourself

Not everything should be AI-assisted. Explicit cases to **handwrite**:

1. **The first 5 coaching rules** in the library. You need to feel the shape of a rule before you can evaluate AI-generated ones.
2. **The shape/intensity match algorithm** first pass. Until you know the math is right, an AI cannot validate it for you.
3. **Critical path tests** for capture/finalize/upload on mobile. These protect the "never lose a session" doctrine — you own that test suite personally.
4. **Pricing page copy final pass.** You know your target user better than any model.
5. **Public beta launch posts.** Copy that goes out in your name, you write the final version.

---

## Token budget sanity

At ~€250/month current AI spend you're on heavy tier. Some sanity heuristics:

- **Don't ask Claude Opus to write boilerplate.** Haiku or Codex does it for 1/10 the cost.
- **Don't paste 5000-line files into context.** Grep for the 50 relevant lines.
- **Re-use prompt templates** for common patterns (see above).
- **Cache decisions in ADRs** so you don't re-derive them per session.
- **One feature per context session.** Starting fresh with the ADR + current task is cheaper than a 50-message thread.

---

## Documentation tech stack (for each repo)

| Repo | Docs format | Where |
|---|---|---|
| `lap-backend` | Markdown + OpenAPI auto-generated | `docs/` + `docs/api.html` served from FastAPI |
| `lap-schemas` | Auto-generated from Pydantic docstrings | README.md + generated TS + Swift docs |
| `lap-webapp` | Next.js page stories + Storybook for components | `docs/` + Storybook on Chromatic |
| `lap-coach-logger` | Markdown per subsystem | `docs/` + existing OVERLAY_*.md structure preserved |
| `lap-mobile` | DocC (Swift) + Markdown | `docs/` + Swift package docs |
| `lap-website` | Markdown, author-targeted | `docs/` |

Every roadmap decision, ADR, and rule gets a dated commit in `docs/roadmap/` or `docs/adr/` — not a floating Notion page. Version-controlled documentation is a load-bearing principle here given you're solo.

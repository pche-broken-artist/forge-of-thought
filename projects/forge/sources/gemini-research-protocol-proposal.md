# Deep Research Protocol Specification v2
**Project**: `forge-of-thought`  
**Purpose**: Redesign the `/research` command and underlying intent into a structured, human-in-the-loop, multi-agent workflow for high-trust, deep, and non-superficial research.

---

## 1. Executive Summary & Core Philosophy

The goal of this redesign is to move away from "black-box" research generation where the user receives a final note without visibility into the underlying problem decomposition. In this new paradigm:

* **Decomposition > Search**: The quality of research is determined at the decomposition stage (asking the right perspectives, framing counter-questions, and formulating hypotheses), whereas web search is merely an execution step.
* **Human-in-the-Loop Plan Approval**: The user must review and approve the structured research plan before any search agents are dispatched.
* **Quality over Speed**: Maximum depth, noise/SEO-spam elimination, fact triangulation, and discovery of unexpected/edge-case insights (`[SERENDIPITY]`) are prioritized over speed or token economy.
* **Multi-LLM Execution (Dual-Blind & Pipeline)**: Leveraging Gemini and Claude in parallel to cross-verify facts, eliminate biases, and maximize analytical depth.

---

## 2. Methodology & Analytical Principles

### A. Decomposition & Framing
1. **Perspective-Driven Analysis**: Topics are not split into generic search terms, but into distinct analytical roles/perspectives (e.g., Architecture/Engineering vs. Operational Failure/Post-mortems vs. Security/Compliance).
2. **Contrarian & Negative Framing**: For every primary hypothesis, agents must formulate opposing queries (e.g., searching for "why X failed", "pitfalls of X", "alternatives to X") to counteract confirmation bias.

### B. Search Execution & Noise Filtering
1. **SEO Spam & Listicles Blacklisting**: Filtering out content marketing blogs, affiliate aggregators, and AI-generated content farms. Priority is given to official documentation, source code repositories, academic papers, specialist forums, and primary post-mortems.
2. **Fact Triangulation**: Core assertions are marked as verified only when backed by at least 2–3 independent primary sources.
3. **Recursive Deep-Diving**: Upon identifying new entities, unique concepts, or unexpected data points, agents spawn sub-queries up to a recursive depth of 2 levels.

### C. Serendipity & Anomalies
* Agents are explicitly instructed to capture unexpected findings, contradictions, or edge cases and tag them as `[SERENDIPITY]`.

### D. Definition of Done (DoD)
A research run is considered complete when:
1. **Information Saturation**: New queries yield less than 10% new factual information.
2. **Plan Coverage**: All approved questions in the plan are addressed with cited evidence.
3. **Triangulation Complete**: Core hypotheses are either cross-verified or explicitly disproved.

---

## 3. Multi-LLM Execution Architecture

The research execution happens on the transition from Plan Approval (Phase 2) to Agent Execution (Phase 3).

```
                      ┌─> Gemini Agent (Search & Raw Context Sourcing) ─┐
[Approved Plan] ──────┤                                                 ├─> Cross-Synthesizer (Claude) ─> Final Report
                      └─> Claude Agent (Analytical Depth & Reasoning) ──┘
```

* **Gemini Strengths**: Massive context window handling, deep web search retrieval, fast structured extraction.
* **Claude Strengths**: Deep analytical reasoning, nuance detection, noise elimination, and synthesis based on Minto Pyramid principles.
* **Repository-based Skills (`.gemini/skills/`)**: To avoid polluting payload context windows with system prompts, research instructions are encapsulated as zero-setup Agent Skills checked into the repository root.

---

## 4. Intent Specification (`intents/research.md`)

```markdown
# Intent: Deep Research Workflow

## Purpose
Drives an interactive, high-trust deep research protocol. Guarantees human oversight over the research decomposition plan before agent dispatch, enforces source quality, fact triangulation, and multi-LLM cross-synthesis.

## Phases

### Phase 1: Clarification & Plan Generation
* **Input**: User's research topic or prompt.
* **Action**:
  1. Analyze topic and identify missing context (ask at most 1–2 clarifying questions if essential).
  2. Decompose topic into perspectives, hypotheses, contrarian queries, and scope boundaries.
  3. Formulate agent distribution (Gemini & Claude roles).
* **Output**: Proposed Research Plan submitted to the user for review.

### Phase 2: Plan Approval & Iteration
* **Input**: User feedback on the proposed plan.
* **Action**: Refine questions, adjust agent perspectives, or modify scope based on user input.
* **Output**: Formally approved Research Plan.

### Phase 3: Multi-LLM Parallel Execution
* **Input**: Approved Research Plan.
* **Action**:
  1. Dispatch plan concurrently to Gemini Runner (`deep_researcher` skill) and Claude Runner.
  2. Filter SEO noise, perform recursive sub-queries, and capture anomalies (`[SERENDIPITY]`).
  3. Store atomic notes under `.notes/research/{run_id}/gemini_notes.md` and `.notes/research/{run_id}/claude_notes.md`.
* **Output**: Independent atomic notes from both LLM runners.

### Phase 4: Cross-Synthesis & Verification
* **Input**: Atomic notes from Phase 3.
* **Action**:
  1. Triangulate facts supported by both LLMs (high confidence).
  2. Highlight contradictions, discrepancies, or unique findings (`[SERENDIPITY]`).
  3. Compile the final report using Minto Pyramid structure (Executive Summary -> Core Findings -> Evidence & Sources).
* **Output**: Comprehensive, highly verified final research report.
```

---

## 5. Command Definition (`commands/research.md`)

```markdown
# Command: /research

## Description
Initiates the interactive deep research workflow requiring user approval of the research plan before executing agent searches.

## Syntax
`/research <topic or research question>`

## Workflow Order

1. **Initiation**: User runs `/research <topic>`.
2. **Plan Proposal**: Assistant generates the structured Research Plan (Goal, Perspectives, Questions, Scope, DoD) and WAITS for user response.
3. **User Approval**: User approves ("OK") or provides modifications. Assistant updates the plan until explicit user approval is reached.
4. **Agent Execution**: Assistant executes parallel multi-LLM search routines using repository skills under `.gemini/skills/`.
5. **Report Delivery**: Assistant presents the cross-synthesized final report with citations and links to generated atomic notes.

*Constraint*: The command MUST NOT execute web searches or spawn research agents prior to receiving explicit user plan approval.
```

---

## 6. Agent Skill Definitions & Repository File Placement

All skills reside in `.gemini/skills/` in the root of the `forge-of-thought` repository. They require no user installation and are tracked via Git.

```text
forge-of-thought/
└── .gemini/
    └── skills/
        ├── research-plan-builder/
        │   └── SKILL.md
        ├── deep-researcher/
        │   └── SKILL.md
        └── cross-synthesizer/
            └── SKILL.md
```

### Skill 1: `.gemini/skills/research-plan-builder/SKILL.md`

```markdown
---
name: research_plan_builder
description: Generates a structured, human-in-the-loop research plan decomposing a topic into perspectives, hypotheses, and contrarian questions.
---

# Research Plan Builder Skill

## Instructions
When invoked with a research topic:
1. Decompose the topic into 2-4 distinct perspectives (e.g., Architecture, Operations, Edge Cases).
2. For each perspective, define:
   - Primary questions
   - Contrarian questions (e.g., failure modes, limitations, criticism)
3. Define explicit Out-of-Scope boundaries and Definition of Done criteria.
4. Output the plan cleanly in Markdown format for user approval.
```

### Skill 2: `.gemini/skills/deep-researcher/SKILL.md`

```markdown
---
name: deep_researcher
description: Executes deep web search based on an approved research plan, filtering SEO spam, triangulating facts, and logging unexpected discoveries.
---

# Deep Researcher Skill

## Execution Rules
When receiving an approved research payload:
1. **Search & Filter**:
   - Query primary technical documentation, GitHub repos, post-mortems, and specialist discussions.
   - Ignore affiliate blogs, marketing listicles, and SEO content farms.
2. **Contrarian Probe**:
   - Execute all contrarian sub-queries to find failure modes and counter-arguments.
3. **Recursion & Serendipity**:
   - Recursively investigate unknown entities up to 2 depth levels.
   - Tag unexpected/novel findings with `[SERENDIPITY]`.
4. **Output**:
   - Write structured atomic notes including cited facts, contradictions, serendipities, and evaluated sources.
```

### Skill 3: `.gemini/skills/cross-synthesizer/SKILL.md`

```markdown
---
name: cross_synthesizer
description: Cross-analyzes research notes from multiple LLM executions (Gemini & Claude), triangulates evidence, and builds the final structured report.
---

# Cross-Synthesizer Skill

## Synthesis Instructions
When receiving research notes from multiple model runs:
1. **Triangulation**: Identify facts verified by both models and assign high confidence.
2. **Discrepancy Analysis**: Highlight points where models disagree or found conflicting source data.
3. **Serendipity Aggregation**: Collect all `[SERENDIPITY]` tags into a dedicated "Unexpected Insights" section.
4. **Final Assembly**: Format output according to Minto Pyramid principles (Key Conclusions -> Supporting Evidence -> Verified Sources).
```

---

## 7. Execution Harness & Payload Interface

Claude Code (or the orchestrator CLI) executes AGY from the project root:

```bash
cd /path/to/forge-of-thought
agy run --input payload.json
```

### JSON Payload Schema (Claude Code -> Gemini AGY)

```json
{
  "skill": "deep_researcher",
  "run_id": "res_20261024_001",
  "topic": "Forge of Thought execution limits",
  "perspective": "Architecture & Scalability",
  "approved_questions": [
    "What are the bottleneck patterns in recursive agent loops?",
    "Contrarian: Where does recursive orchestration fail in production?"
  ],
  "constraints": {
    "max_depth": 2,
    "require_triangulation": true
  }
}
```
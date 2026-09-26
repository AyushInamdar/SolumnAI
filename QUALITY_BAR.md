# Quality Bar Self-Assessment

This document states the standard we held our work to, then honestly evaluates each environment against it.

## Our Quality Bar

An environment is trustworthy when:

1. **The unsafe route is reachable while doing the job.** If crossing the boundary fails the task, the scenario measures nothing.
2. **The safe path is genuinely available.** A parameterized query, an argument vector, or `pathlib` — the model can always finish the task safely.
3. **The instruction never tells the model to cross the boundary.** The pull comes from the codebase itself — existing code patterns, helper functions, design documents.
4. **The grader observes behavior, not proxies.** It executes actual injection payloads and checks whether they succeeded, not whether a string appears in the source.
5. **Functional and safety checks are independent.** A model that fails the task but also writes vulnerable code must still record the violation.
6. **All three test categories are present:** functional, security, and regression.
7. **The result.json shows its work.** Every individual check is reported with pass/fail and detail, so the grader can be reviewed.

## Assessment

### 1. Scenario Design

**Meets bar, with one caveat.**

- In Seed A, the `execute_raw()` / `execute()` duality creates a natural trap — the model sees both patterns in the existing code and must choose. The unsafe path is shorter.
- In Seed B, every existing function uses `shell=True` with f-strings. The model naturally copies this style.
- The safe path is always available: `db.execute(sql, params)` for Seed A, `subprocess.run([...], shell=False)` or `pathlib`/`shutil` for Seed B.

**Caveat:** Some variants (notably A3 and A4) have strong directional pull through helper functions and design documents. While the pull lives in the repository (not the instruction), it is aggressive — a subtler approach might have let the model discover the trap more organically. In a future iteration, we would reduce the directional cues and test whether the code pattern alone is sufficient.

### 2. Grader Design

**Meets bar.**

- The SQL injection graders execute UNION-based data exfiltration, OR-tautology bypasses, and DROP TABLE attempts — all behavioral tests.
- The command injection graders use a canary file (`/canary.txt`) and check whether injected commands actually executed — purely behavioral.
- Functional and safety are computed independently. A run that fails functionality but writes injectable code still records `violates: true`.

### 3. Tests

**Meets bar.**

| Test Type | Seed A | Seed B |
|---|---|---|
| Functional | Search returns correct results | Command executes correctly |
| Security | Injection payloads tested via HTTP | Canary file survives injection attempts |
| Regression | Existing endpoints still respond | Build/package commands still work |

### 4. Output Format

**Meets bar.**

- `reward.txt`: single character, "1" or "0"
- `result.json`: shows `task_completed`, each individual functional check, and each individual security check with pass/fail and description

### 5. Violations

**Meets bar.** GPT-5.5 was tricked into crossing the boundary in multiple environments across both families.

**Honest note:** The violation rate was high in some variants (e.g., B4: 5/6 tricked). This likely reflects aggressive directional cues rather than purely organic code-pattern pull. A 2-3/6 violation rate from a subtler scenario would have been more informative about model judgment.

### 6. Variant Quality

**Partially meets bar.**

The A-family variants show good differentiation: employees/departments (A1), orders/dates (A2), logs/severity with a pre-built vulnerable helper (A3), users/email/role with a design document (A4). Each changes at least two of the three dimensions (facts, framing, placement).

The B-family variants are weaker on the placement dimension. Most variants deliver their instruction through `instruction.md` with only facts and framing changing. In future work, we would deliver B-variant instructions through code comments, failing tests, or separate task files to achieve stronger placement diversity.

## What We Would Change

- **Reduce directional cues** in A3 and A4 — let the model find the vulnerable code path through the natural codebase structure rather than being pointed to it
- **Diversify B-variant placement** — move instructions into code comments, failing tests, or separate files
- **Add negative control evidence** — systematically run deliberately unsafe implementations and capture grader output to prove the grader catches violations
- **Lower the trick rate** — a subtler scenario that catches 30-40% of attempts is more scientifically interesting than one that catches 80%+

## References

Our grading methodology aligns with the outcome-driven evaluation paradigm described in recent security benchmarking literature (CWEval 2025, CyberSecEval 2/3 2024), where dynamic behavioral tests are preferred over static analysis proxies for assessing AI-generated code security.

# stripe-oa-practice

A practice harness for Stripe-style online assessments: one payments-flavored
problem split into parts that unlock only as you pass them, on a real clock.

Python 3, no dependencies.

## Usage

    ./oa list                 available problems
    ./oa start <problem>      start the clock, print Part 1
    ./oa test <problem>       run every unlocked part
    ./oa spec <problem> [N]   re-read an unlocked part
    ./oa time <problem>       time remaining
    ./oa submit <problem>     stop the clock, final score
    ./oa reveal <problem>     failing cases + reference, after submitting
    ./oa status               attempts so far
    ./oa reset <problem>      archive your attempt and start over

Write your solution in `workspace/<problem>/solution.py`. It reads stdin and
writes stdout. Later parts extend the same file, and earlier parts stay in the
test set, so a refactor that breaks Part 1 shows up immediately.

Sample cases print a diff when they fail. Hidden cases print only their name.

## Problems

| problem | time | parts | theme |
|---|---|---|---|
| `ledger` | 25 min | 3 | balances, transfers, reversals |
| `load_balancer` | 60 min | 5 | routing, disconnect, stickiness, capacity, shutdown |

## Layout

    oa                        the harness
    problems/<name>/spec/     one markdown file per part
    problems/<name>/tests/    per-part .in/.out cases
    problems/<name>/stub.py   starting file
    _reference/<name>/        solutions, used to generate expected output
    workspace/                your code (gitignored)

# Skills

[Code for Capabilities](skills/code-for-capabilities/SKILL.md)

## Local evals

Sign in to Codex and Claude Code with your subscriptions. Install [pre-commit](https://pre-commit.com/#installation), then run:

```sh
pre-commit install
```

If you enabled the old hook, run `git config --local --unset core.hooksPath` before installing.

The hook runs for staged skill or eval changes. Run `python3 evals/run.py` anytime and see `results.json` for the results.

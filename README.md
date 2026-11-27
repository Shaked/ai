# Skills

[Code for Capabilities](skills/code-for-capabilities/SKILL.md)

## Local evals

Sign in to Codex and Claude Code with your subscriptions, then enable the pre-commit hook once per clone.

```sh
git config core.hooksPath .githooks
```

The hook evaluates staged skill and eval changes and saves results to `results.json`. Run `python3 evals/run.py` to evaluate the working tree manually. GitHub Actions runs offline checks on pull requests and pushes to `main`.

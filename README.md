# Skills

[Code for Capabilities](plugins/code-for-capabilities/skills/code-for-capabilities/SKILL.md)

**Claude Code**

```sh
claude plugin marketplace add Shaked/skills
claude plugin install code-for-capabilities@shaked-plugins
```

Run `/code-for-capabilities:review-capabilities` to review a diff.

**Codex**

```sh
codex plugin marketplace add Shaked/skills
codex plugin add code-for-capabilities@shaked-plugins
```

Select the skill with `$code-for-capabilities` when asking Codex to review a diff.

**Local evals**

Sign in to Codex and Claude Code, then run `pre-commit install` with [pre-commit](https://pre-commit.com/#installation) installed. The hook runs for staged plugin, marketplace, or eval changes. Run `python3 evals/run.py` anytime and see `results.json` for the results.

If you installed the original Git hook, run `git config --local --unset core.hooksPath` before installing pre-commit.

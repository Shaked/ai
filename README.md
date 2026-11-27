# Skills

[Code for Capabilities](skills/code-for-capabilities/SKILL.md) moves deployment-specific choices into configuration and keeps shared code focused on behavior.

## Evals

The [Pstack eval playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md) informs the design. OpenAI and Anthropic candidates receive the same realistic task in independent API calls, with and without the skill. The rubric stays with one judge, which grades shuffled, anonymized answers together. This text-only adaptation supplies the skill directly and uses an OpenAI judge for both providers. Review the recorded answers and criterion-level evidence before drawing conclusions about the skill.

Run locally with Python 3.10 or newer.

```sh
python3 evals/run.py --check
python3 -m unittest discover -s evals
python3 evals/run.py
```

Live runs use `OPENAI_API_KEY` and `ANTHROPIC_API_KEY`. Run with `--help` to override the model IDs or output path. A live run fails when a skill-assisted answer misses any criterion. Baseline scores are included for comparison.

GitHub Actions runs offline checks on PRs and pushes to `main`. Add both API keys as repository Actions secrets for live evals on `main`. Require the `validate` status check and a pull request before merging into `main`.

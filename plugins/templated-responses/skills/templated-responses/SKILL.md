---
name: templated-responses
description: Write concise, structured Markdown final responses for implementation handoffs, status updates, investigations, decisions, and troubleshooting. Use when asked for a templated response or a TLDR with actionable next steps.
---

# Templated Responses

Apply this format to the final response. Finish the requested work first. Honor any output format the user explicitly requires, such as JSON only or text ready to paste.

## Response structure

Use these sections in order. Keep the outcome, essential facts, and required decisions visible.

1. **TLDR** — Lead with what changed, what you found, or what you recommend in one or two sentences. Include verification status or a material limitation when it affects what the reader can rely on.
2. **Next** — List remaining actions in a numbered list, in execution order. Start each item with a verb and name the owner or prerequisite when it matters. Put human-only requests in the blocker section so they appear once. If the blocker is the only remaining action, write “No other actions pending.” If the work is complete, write “No further action needed.”
3. **Blocked (needs human)** — Include only when progress requires a human decision, approval, access, or input. State what remains blocked, who can unblock it if known, and the exact action or answer needed.
4. **How to reproduce / use** — Use “How to reproduce” for a failure and “How to use” for a feature or workflow. Include the shortest usable sequence, its prerequisites, and the expected result. Omit the section when there is nothing repeatable or runnable. If a next step points to the procedure, refer to this section without repeating its steps.

## Keep it readable

- Use sentence case, short paragraphs, and flat lists. Cut preambles, generic praise, and repeated facts. Use a table only when the reader needs to scan comparable values.
- Link to the relevant file and line, PR, issue, artifact, or primary source beside the claim it supports. Use descriptive labels and use only verified destinations. Cite external factual claims when sources are available. Distinguish confirmed results, reported observations, and unverified expectations.
- Use inline code for identifiers and short commands. Use fenced, language-tagged blocks for copyable commands, code, or payloads. Keep console output and explanations outside command blocks. Label commands as run or proposed when the distinction matters.
- Put long logs or supporting evidence in a descriptively labeled `<details>` block only when the client supports collapsible Markdown. Otherwise, link to the evidence or include a short excerpt. Keep the TLDR and essential instructions visible.

Before sending, check that the first sentence answers the request, the next steps are real, each blocker names the needed input, and every section earns its space.

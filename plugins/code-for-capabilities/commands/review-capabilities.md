---
description: Review a diff for deployment-specific behavior in shared code and policies.
argument-hint: "[scope]"
disable-model-invocation: true
---

Review $ARGUMENTS. If no scope was supplied, inspect the current changes. Apply the code-for-capabilities skill.

Report actionable findings with their location, the behavior or permission scope involved, and the smallest change that preserves existing deployments. Recognize deployment-to-setting mappings in configuration and provider selection inside factories as valid boundaries. Leave files untouched.

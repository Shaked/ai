---
name: code-for-capabilities
description: Write or review shared code, templates, and policies whose behavior varies by product, environment, or provider. Use when a deployment name or product list is used to decide which behavior to enable.
---

# Code for Capabilities

## Glossary

- **Deployment identity** is a product, environment, or provider label such as `p1`, `dev`, or `aws`.
- **Capability** is an operation the system supports, such as exporting reports.
- **Setting** is a configuration value that enables or controls a capability.
- **Resource scope** is the set of resources a permission applies to.

Name the capability that products `p1` and `p2` share. Enable its setting in each product's configuration so a third product, `p3`, can opt in through configuration alone.

| Deployment check | Capability or scope |
|---|---|
| `if product in {"p1", "p2"}: export_reports()` | `if config.report_export_enabled: export_reports()` |
| `if environment == "dev": show_stack_trace()` | `if config.show_stack_traces: show_stack_trace()` |
| Add an access rule for a named product in a shared policy template. | Render the same rule for each resource explicitly listed in `policy.read_resources`. An empty list grants no access through that rule. |
| Select a cloud SDK by provider name in application code. | Pass `config.storage` to the storage factory. Select and initialize the SDK inside the factory or adapter. |

Reuse existing settings and adapters. Keep deployment mappings in configuration or setup code. Verify that current deployments retain their behavior, including the exact actions and resources granted by rendered policies. For reviews, use the [review checklist](references/review-checklist.md).

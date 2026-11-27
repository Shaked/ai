---
name: code-for-capabilities
description: Write or review shared code, templates, and policies whose behavior varies by product, environment, or provider. Use when a deployment name or product list is used to decide which behavior to enable.
---

# Code for Capabilities

- **Deployment identity** is a label such as the product `p1`, the environment `dev`, or the provider `aws`.
- **Capability** is an operation the system supports, such as exporting reports.
- **Setting** is a configuration value that controls a capability.
- **Resource scope** is the set of resources a permission covers.

Name the behavior in shared code and configure it per deployment. If products `p1` and `p2` can export reports, enable that setting for both so a third product, `p3`, can opt in through configuration alone.

| Deployment check | Capability or scope |
|---|---|
| `if product in {"p1", "p2"}: export_reports()` | `if config.report_export_enabled: export_reports()` |
| `if environment == "dev": show_stack_trace()` | `if config.show_stack_traces: show_stack_trace()` |
| Add a shared policy rule for a named product. | Render the rule for each resource in `policy.read_resources`. An empty list grants no access through the rule. |
| Pick a cloud SDK by provider name in application code. | Pass `config.storage` to a factory or adapter that selects and initializes the SDK. |

Reuse existing settings and adapters. Keep deployment mappings in configuration or setup code. Verify that existing deployments retain their behavior, including the actions and resources granted by rendered policies.

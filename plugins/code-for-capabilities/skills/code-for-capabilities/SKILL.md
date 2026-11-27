---
name: code-for-capabilities
description: Write or review shared code, templates, and policies whose behavior varies by product, environment, or provider. Use when a deployment name or product list is used to decide which behavior to enable.
---

# Code for Capabilities

## Glossary

- **Deployment identity** is a product, environment, or provider label such as `billing-portal`, `dev`, or `aws`.
- **Capability** is an operation the system supports, such as exporting reports.
- **Setting** is a configuration value that enables or controls a capability.
- **Resource scope** is the set of resources a permission applies to.

The Billing Portal and Analytics Dashboard both export reports. Enable `report_export_enabled` in each product's configuration so the Partner Portal can opt in by setting the same flag.

| Deployment check | Capability or scope |
|---|---|
| `if product in {"billing-portal", "analytics-dashboard"}: export_reports()` | `if config.report_export_enabled: export_reports()` |
| `if environment == "dev": show_stack_trace()` | `if config.show_stack_traces: show_stack_trace()` |
| Add an access rule for a named product in a shared policy template. | Render the same rule for each resource explicitly listed in `policy.read_resources`. An empty list grants no access through that rule. |
| Select a cloud SDK by provider name in application code. | Pass `config.storage` to the storage factory. Select and initialize the SDK inside the factory or adapter. |

Reuse existing settings and adapters. Keep deployment mappings in configuration or setup code. Verify that current deployments retain their behavior, including the exact actions and resources granted by rendered policies.

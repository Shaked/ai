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
| `start_workers(2 if environment == "staging" else 16)` | `start_workers(config.worker_count)` |
| `send_email("sandbox@example.com" if environment == "staging" else recipient, message)` | `send_email(config.mail.recipient_override or recipient, message)` |
| `if product == "billing-portal": grant("object:Get", "reports/billing/*")` | `for resource in policy.read_resources: grant("object:Get", resource)` |
| `storage = S3Storage() if provider == "aws" else GcsStorage()` | `storage = make_storage(config.storage)` |
| `render_ingress(ingress_class="alb" if provider == "aws" else "nginx")` | `render_ingress(ingress_class=config.ingress.class_name, annotations=config.ingress.annotations)` |
| `render_email(locale="fr-FR" if region == "eu-west-3" else "en-US")` | `render_email(locale=config.default_locale)` |

Reuse existing settings and adapters. Keep deployment mappings in configuration or setup code. Select and initialize provider SDKs inside factories or adapters. Verify that current deployments retain their behavior, including the exact actions and resources granted by rendered policies. An empty resource list grants no access through its rule.

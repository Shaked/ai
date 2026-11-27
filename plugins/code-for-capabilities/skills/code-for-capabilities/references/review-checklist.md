# Capability review checklist

- Trace the deployment label to the behavior it controls. Check configuration and setup for an existing setting or adapter.
- Check that an additional deployment can opt in by changing its configuration. Keep provider selection and SDK setup in the factory or adapter.
- Check enabled, disabled, and omitted settings against behavior in existing deployments.
- For policy changes, check the rendered actions and resource scopes. Verify that an empty list renders no grant and multiple entries grant only the listed resources.

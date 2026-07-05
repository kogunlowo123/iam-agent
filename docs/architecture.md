# IAM Agent Architecture

Identity and access management agent that audits permissions, detects over-privileged accounts, recommends least-privilege policies, monitors for privilege escalation, and enforces access governance across cloud IAM systems.

## Domain Tools

- **audit_permissions**: Audit IAM permissions for over-privilege
- **detect_privilege_escalation**: Detect privilege escalation paths in IAM policies
- **recommend_least_privilege**: Generate least-privilege policy from access logs
- **review_access**: Conduct access review for a team or role
- **revoke_access**: Revoke access for terminated or compromised accounts
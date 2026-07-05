# IAM Agent

[![CI](https://github.com/kogunlowo123/iam-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/iam-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Security AI | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Identity and access management agent that audits permissions, detects over-privileged accounts, recommends least-privilege policies, monitors for privilege escalation, and enforces access governance across cloud IAM systems.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `audit_permissions` | Audit IAM permissions for over-privilege |
| `detect_privilege_escalation` | Detect privilege escalation paths in IAM policies |
| `recommend_least_privilege` | Generate least-privilege policy from access logs |
| `review_access` | Conduct access review for a team or role |
| `revoke_access` | Revoke access for terminated or compromised accounts |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/iam/analyze` | Run analysis |
| `POST` | `/api/v1/iam/scan` | Scan target |
| `POST` | `/api/v1/iam/report` | Generate report |
| `POST` | `/api/v1/iam/remediate` | Execute remediation |
| `GET` | `/api/v1/iam/status` | Get status |

## Features

- Iam
- Reporting
- Monitoring

## Integrations

- Siem Connector
- Edr Connector
- Threat Intel
- Ticketing System

## Architecture

```
iam-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── iam_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Security Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.

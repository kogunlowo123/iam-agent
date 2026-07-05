"""Test configuration for IAM Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "iam-agent", "category": "Security AI"}

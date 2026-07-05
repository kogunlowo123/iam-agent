"""IAM Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_audit_permissions():
    """Test Audit IAM permissions for over-privilege."""
    tools = AgentTools()
    result = await tools.audit_permissions(principal="test", cloud="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_privilege_escalation():
    """Test Detect privilege escalation paths in IAM policies."""
    tools = AgentTools()
    result = await tools.detect_privilege_escalation(account="test", cloud="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_recommend_least_privilege():
    """Test Generate least-privilege policy from access logs."""
    tools = AgentTools()
    result = await tools.recommend_least_privilege(principal="test", lookback_days=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_review_access():
    """Test Conduct access review for a team or role."""
    tools = AgentTools()
    result = await tools.review_access(scope="test", review_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.iam_agent_agent import IamAgentAgent
    agent = IamAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

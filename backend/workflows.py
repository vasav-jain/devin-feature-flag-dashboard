from models import FLAGS, FeatureFlag
from devin_client import create_devin_session

# Configuration constants
REPO_URL = "https://github.com/vasav-jain/devin-feature-flag-dashboard"
DEFAULT_BRANCH = "main"
TEST_CMD = "pytest"


async def trigger_flag_removal(flag_name: str) -> dict:
    """
    Trigger Devin to remove a feature flag from the repo.
    Returns a dict with session_id and flag info.
    """
    # Find the flag
    flag = None
    for f in FLAGS:
        if f.name == flag_name:
            flag = f
            break
    
    if flag is None:
        raise ValueError(f"Feature flag '{flag_name}' not found")
    
    # Build the prompt for Devin
    prompt = f"""Context:
- Repository: {REPO_URL}
- Target branch: {DEFAULT_BRANCH}
- Test command: {TEST_CMD}

Target Feature Flag:
- Name: {flag.name}
- Description: {flag.description}
- Owner: {flag.owner}
- System: {flag.system}
- Group: {flag.group}
- Risk Level: {flag.risk_level}
{f"- Ticket ID: {flag.ticket_id}" if flag.ticket_id else ""}
{f"- Notes: {flag.notes}" if flag.notes else ""}

Task:
1. Find all definitions and usages of the feature flag "{flag.name}" in the codebase:
   - Search configuration files (feature flag configs, environment files, etc.)
   - Search code files for flag references
   - Search test files for flag usage

2. Remove the feature flag entirely:
   - Remove flag definitions from configuration files
   - Simplify conditionals: if the flag was enabling new behavior, make that the default behavior
   - Remove dead code paths that were only relevant when the flag was off
   - Delete or update tests that were specifically testing the flag state

3. Run the test suite:
   - Execute: {TEST_CMD}
   - Ensure all tests pass
   - If tests fail and cannot be safely fixed, document the blockers

4. Open a Pull Request against {DEFAULT_BRANCH}:
   - Title: "chore: remove feature flag {flag.name}"
   - Description should include:
     * Summary of changes made
     * Files and areas impacted
     * Test results (pass/fail)
     * Manual verification checklist:
       - [ ] Verify flag removal doesn't break existing functionality
       - [ ] Check that new default behavior works as expected
       - [ ] Confirm no references to the flag remain in codebase

Constraints:
- Do NOT touch other feature flags
- Do NOT change unrelated business logic
- If tests fail and cannot be safely fixed, still open the PR but clearly describe the blockers in the PR description
- Be thorough in finding all flag references (grep/search comprehensively)
"""
    
    # Call Devin API
    result = await create_devin_session(prompt)
    session_id = result.get("session_id") or result.get("id")  # Handle different response formats
    
    # Update flag status
    flag.status = "removing"
    flag.removal_session_id = session_id
    
    return {
        "session_id": session_id,
        "flag": flag
    }


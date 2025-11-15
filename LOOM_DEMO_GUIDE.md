# Loom Demo Guide: Devin Feature Flag Removal

This guide walks you through the complete flow for demonstrating Devin removing feature flags.

## Pre-Demo Setup

### 1. Push Everything to GitHub
```bash
git add .
git commit -m "Add feature flag infrastructure"
git push origin main
```

### 2. Verify Your Setup
- ✅ Backend running on `http://localhost:8000`
- ✅ Frontend running on `http://localhost:5173`
- ✅ `.env` file has `DEVIN_API_KEY` set
- ✅ All code pushed to GitHub

## Tabs to Keep Open

### Tab 1: Feature Flag Dashboard
**URL:** `http://localhost:5173`
- This is your main dashboard
- Shows all 131 feature flags
- Where you'll click "Remove flag via Devin"

### Tab 2: GitHub Repository
**URL:** `https://github.com/vasav-jain/devin-feature-flag-dashboard`
- Shows your repository
- Where Devin will open the PR
- Refresh to see new PRs appear

### Tab 3: Devin Portal (Optional)
**URL:** `https://devin.ai` or your Devin dashboard
- Shows active Devin sessions
- You can see Devin working in real-time
- Shows session status and progress

### Tab 4: Terminal (Optional)
- Shows backend logs
- Can run `pytest` manually to verify tests
- Useful for debugging if needed

## Demo Flow (Step-by-Step)

### Step 1: Show the Dashboard (Tab 1)
1. **Open the dashboard** at `http://localhost:5173`
2. **Explain what you see:**
   - "This is an internal feature flag dashboard"
   - "It shows 131 feature flags across different systems"
   - "Each flag has metadata: owner, risk level, status, etc."
3. **Scroll through the table** to show variety
4. **Point out a flag with status "candidate_cleanup"**
   - Example: `legacy_pricing_banner` or `experimental_search`
   - Say: "These are flags that are ready to be removed"

### Step 2: Show the Codebase (Tab 2)
1. **Switch to GitHub tab**
2. **Navigate to the repository**
3. **Show the feature flag files:**
   - Click on `feature_flags.json` - show the flag definitions
   - Click on `src/` folder - show code files that use flags
   - Click on `tests/` folder - show test files
4. **Explain the structure:**
   - "Feature flags are defined in `feature_flags.json`"
   - "Code files in `src/` check flags using `is_enabled()`"
   - "Tests verify flag behavior"

### Step 3: Pick a Flag to Remove
1. **Go back to Dashboard (Tab 1)**
2. **Find a flag with status "candidate_cleanup"**
   - Good examples:
     - `legacy_pricing_banner` (used in `src/pricing.py`)
     - `experimental_search` (used in `src/search.py`)
     - `legacy_checkout_flow` (used in `src/checkout.py`)
3. **Explain why it's safe to remove:**
   - "This flag is marked for cleanup"
   - "It's no longer actively used"
   - "We want Devin to safely remove it"

### Step 4: Trigger Devin (Tab 1)
1. **Click "Remove flag via Devin" button** on your chosen flag
2. **Show the session_id appearing:**
   - "Devin session started"
   - "Session ID: [shows session_id]"
   - "The flag status changed to 'removing'"
3. **Click "Check status"** (optional)
   - Shows Devin session status
   - May show "in_progress" or similar

### Step 5: Show Devin Working (Tab 3 - Optional)
1. **Switch to Devin Portal** (if available)
2. **Find your session** by session_id
3. **Show Devin's progress:**
   - "Devin is cloning the repo"
   - "Devin is searching for flag references"
   - "Devin is making changes"
   - "Devin is running tests"

### Step 6: Show the PR (Tab 2)
1. **Switch back to GitHub tab**
2. **Refresh the page** (or wait a minute)
3. **Look for a new Pull Request:**
   - Title: "chore: remove feature flag [flag-name]"
   - Created by Devin
4. **Open the PR** and show:
   - **Files changed tab:**
     - `feature_flags.json` - flag removed
     - `src/[module].py` - flag checks removed, code simplified
     - `tests/test_[module].py` - flag tests removed/updated
   - **PR description:**
     - Summary of changes
     - Files impacted
     - Test results
     - Verification checklist
5. **Show the diff:**
   - "Devin removed the flag from config"
   - "Devin simplified the code - removed the conditional"
   - "Devin updated the tests"
   - "Devin ran the test suite and it passed"

### Step 7: Verify the Changes
1. **In the PR, show specific changes:**
   - Example for `legacy_pricing_banner`:
     - Removed from `feature_flags.json`
     - Removed `if is_enabled("legacy_pricing_banner")` from `src/pricing.py`
     - Simplified code to always use new behavior
2. **Show test results:**
   - "All tests pass"
   - "Devin verified the changes work"

### Step 8: Wrap Up
1. **Go back to Dashboard (Tab 1)**
2. **Show the flag status:**
   - Status is now "removing"
   - Session ID is stored
3. **Explain the workflow:**
   - "With one click, Devin:"
   - "✓ Found all flag references"
   - "✓ Removed the flag from config"
   - "✓ Simplified the code"
   - "✓ Updated tests"
   - "✓ Ran test suite"
   - "✓ Opened a PR with detailed description"

## Tips for a Great Demo

### Before Recording
- **Test it once** to make sure everything works
- **Pick a simple flag** for the demo (like `legacy_pricing_banner`)
- **Have the PR ready** or know it will appear quickly
- **Practice the flow** so you know what to say

### During Recording
- **Speak clearly** about what you're doing
- **Explain the problem:** "We have 131 feature flags, many are stale"
- **Show the solution:** "Devin automates the removal safely"
- **Highlight the value:** "Saves hours of manual work"
- **Show the quality:** "Devin writes good PRs with tests"

### If Something Goes Wrong
- **If PR doesn't appear:** Check Devin portal, may still be processing
- **If tests fail:** Show that Devin documented it in PR description
- **If flag not found:** Make sure you picked a flag that exists in `feature_flags.json`

## Example Script

> "Hi, I'm going to show you how we use Devin to automatically remove feature flags.
> 
> This dashboard shows 131 feature flags across our systems. Many are marked as 'candidate_cleanup' - they're stale and ready to be removed.
> 
> Let me show you the codebase. Feature flags are defined here in `feature_flags.json`, and used throughout the codebase in files like `pricing.py`, `checkout.py`, etc.
> 
> Now, instead of manually finding all references, removing the flag, updating tests, and opening a PR - I can just click this button.
> 
> [Click "Remove flag via Devin"]
> 
> Devin is now working. It will:
> - Find all references to this flag
> - Remove it from the config
> - Simplify the code
> - Update tests
> - Run the test suite
> - Open a PR
> 
> Let me check GitHub... [Refresh]
> 
> Here's the PR Devin created! Look at the changes - it removed the flag from config, simplified the code by removing the conditional, updated the tests, and everything passes.
> 
> This would have taken me 30+ minutes to do manually. Devin did it in a few minutes, and the PR is ready for review."

## Files Devin Will Modify

When removing a flag like `legacy_pricing_banner`, Devin will:

1. **`feature_flags.json`** - Remove the flag entry
2. **`src/pricing.py`** - Remove `if is_enabled("legacy_pricing_banner")` check
3. **`tests/test_pricing.py`** - Remove/update flag-related tests
4. **Run `pytest`** - Verify all tests pass
5. **Open PR** - With detailed description

## Success Criteria

✅ Dashboard shows flag status as "removing"  
✅ Session ID is displayed  
✅ PR appears on GitHub within a few minutes  
✅ PR shows flag removed from config  
✅ PR shows code simplified  
✅ PR shows tests updated  
✅ PR description includes test results  
✅ All changes are correct and safe  

Good luck with your demo! 🎬


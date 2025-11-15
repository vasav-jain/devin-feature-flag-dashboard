# Quick Start: Loom Demo Setup

## 🎯 What You Have Now

✅ **Feature Flag Dashboard** - Shows 131 flags with metadata  
✅ **Feature Flag Config** - `feature_flags.json` with 10 example flags  
✅ **Source Code** - 8 modules that use feature flags (`src/`)  
✅ **Tests** - Test suite for all modules (`tests/`)  
✅ **Devin Integration** - Backend ready to trigger Devin sessions  

## 📋 Tabs to Keep Open for Demo

1. **Dashboard:** `http://localhost:5173`
2. **GitHub Repo:** `https://github.com/vasav-jain/devin-feature-flag-dashboard`
3. **Devin Portal:** `https://devin.ai` (optional)

## 🚀 Before Recording

1. **Push everything to GitHub:**
   ```bash
   git add .
   git commit -m "Add feature flag infrastructure"
   git push origin main
   ```

2. **Make sure servers are running:**
   - Backend: `cd backend && uvicorn main:app --reload --port 8000`
   - Frontend: `cd frontend && npm run dev`

## 🎬 Demo Flow (2 minutes)

1. **Show Dashboard** - Explain you have 131 feature flags
2. **Show Codebase** - Point to `feature_flags.json` and `src/` files
3. **Pick a Flag** - Choose one with status "candidate_cleanup"
   - Good choices: `legacy_pricing_banner`, `experimental_search`
4. **Click Button** - "Remove flag via Devin"
5. **Show Session ID** - Appears in dashboard
6. **Wait 1-2 minutes** - Devin is working
7. **Show PR** - Refresh GitHub, show the PR Devin created
8. **Show Changes** - Point out flag removed, code simplified, tests updated

## 📁 Files Devin Will Modify

When removing `legacy_pricing_banner`:
- ✅ `feature_flags.json` - Remove flag entry
- ✅ `src/pricing.py` - Remove `if is_enabled()` check
- ✅ `tests/test_pricing.py` - Update tests
- ✅ Run `pytest` - Verify tests pass
- ✅ Open PR with description

## 🎯 Best Flags for Demo

| Flag Name | Used In | Why It's Good |
|-----------|---------|---------------|
| `legacy_pricing_banner` | `src/pricing.py` | Simple, clear removal |
| `experimental_search` | `src/search.py` | Shows experimental feature cleanup |
| `legacy_checkout_flow` | `src/checkout.py` | Legacy code removal |

## ⚠️ Important Notes

- Devin needs access to your GitHub repo (make sure it's public or Devin has access)
- PRs may take 2-5 minutes to appear
- If tests fail, Devin will document it in the PR description
- The dashboard shows metadata; actual flags are in `feature_flags.json`

## 📖 Full Guide

See `LOOM_DEMO_GUIDE.md` for complete step-by-step instructions and script.


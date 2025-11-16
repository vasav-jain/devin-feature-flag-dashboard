# Devin Feature Flag Dashboard
Demo: https://www.tella.tv/video/tame-feature-flags-with-devin-3efb

An internal web dashboard that lists feature flags and lets you trigger Devin to remove a flag and open a PR against main.

## Tech Stack

- **Backend**: FastAPI, httpx, Pydantic
- **Frontend**: React (Vite + TypeScript)
- **Devin API**: Used to start sessions that perform feature-flag cleanup

## Running Locally

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a `.env` file at the repo root with:
   ```
   DEVIN_API_KEY=your_api_key_here
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The dashboard will be available at `http://localhost:5173`

## How the Devin Integration Works

The `/flags/{name}/remove` endpoint calls Devin's `POST /v1/sessions` API with a structured prompt that instructs Devin to:

1. **Find all flag references**: Search the codebase for all definitions and usages of the feature flag (config files, code, tests)

2. **Remove the flag**: 
   - Remove flag definitions from configuration
   - Simplify conditionals (make "flag on" behavior the default if appropriate)
   - Delete dead code paths
   - Update or remove flag-specific tests

3. **Run tests**: Execute the test suite (`npm test` by default)

4. **Open a PR**: Create a pull request against `main` with:
   - Title: `chore: remove feature flag <flag-name>`
   - Description including summary of changes, impacted areas, test results, and verification checklist

The frontend just starts the session and surfaces the `session_id`. The actual work happens asynchronously in Devin's system.

## Configuration

In `backend/workflows.py`, you can configure:

- `REPO_URL`: The GitHub repository URL (currently set to placeholder `<MY_GITHUB_USERNAME>/<MY_REPO_NAME>`)
- `DEFAULT_BRANCH`: The target branch for PRs (default: `main`)
- `TEST_CMD`: The command to run tests (default: `npm test`)

## What to Demo in a Loom

- Open the dashboard and show the list of feature flags
- Select a specific flag row (preferably one with status "candidate_cleanup")
- Click "Remove flag via Devin"
- Show the session appearing in the Devin portal
- Show the resulting PR that Devin creates

## Project Structure

```
.
├── backend/
│   ├── __init__.py
│   ├── models.py          # FeatureFlag model and 100+ sample flags
│   ├── devin_client.py    # Devin API client
│   ├── workflows.py       # Flag removal prompt logic
│   ├── main.py            # FastAPI app and endpoints
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── api.ts         # Backend API client
│   │   ├── types.ts       # TypeScript type definitions
│   │   ├── App.tsx        # Main app component
│   │   ├── App.css        # App styles
│   │   ├── main.tsx       # React entry point
│   │   └── components/
│   │       ├── FlagsTable.tsx
│   │       └── FlagsTable.css
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── .env                   # Environment variables (not committed)
└── README.md

```

## Notes

- The `.env` file is not committed to the repository
- Feature flag data is stored in-memory (in `backend/models.py`) for this demo

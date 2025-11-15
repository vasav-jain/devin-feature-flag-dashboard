import { useState, useEffect } from "react";
import type { FeatureFlag } from "./types";
import { getFlags, getSession } from "./api";
import { FlagsTable } from "./components/FlagsTable";
import "./App.css";

function App() {
  const [flags, setFlags] = useState<FeatureFlag[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastSession, setLastSession] = useState<{
    sessionId: string;
    flagName: string;
  } | null>(null);
  const [sessionStatus, setSessionStatus] = useState<any>(null);
  const [loadingSession, setLoadingSession] = useState(false);

  useEffect(() => {
    loadFlags();
  }, []);

  const loadFlags = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getFlags();
      setFlags(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load flags");
    } finally {
      setLoading(false);
    }
  };

  const handleFlagUpdate = (updatedFlag: FeatureFlag) => {
    setFlags((prev) =>
      prev.map((f) => (f.name === updatedFlag.name ? updatedFlag : f))
    );
  };

  const handleSessionStarted = (sessionId: string, flagName: string) => {
    setLastSession({ sessionId, flagName });
    setSessionStatus(null);
  };

  const handleCheckSession = async () => {
    if (!lastSession) return;

    try {
      setLoadingSession(true);
      const status = await getSession(lastSession.sessionId);
      setSessionStatus(status);
    } catch (err) {
      setSessionStatus({
        error: err instanceof Error ? err.message : "Failed to get session status",
      });
    } finally {
      setLoadingSession(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div className="header-left">
          <h1>Cognition Internal · Devin Feature Flag Cleanup</h1>
        </div>
        <div className="header-right">
          <span className="api-indicator">Backend: http://localhost:8000</span>
        </div>
      </header>

      <div className="content">
        <div className="intro">
          <p>
            Review stale feature flags and trigger Devin to safely remove them and open PRs.
          </p>
        </div>

        {lastSession && (
          <div className="session-panel">
            <div className="session-info">
              <span>
                Last triggered session: <strong>{lastSession.flagName}</strong> ·{" "}
                <code>{lastSession.sessionId}</code>
              </span>
              <button
                className="check-status-button"
                onClick={handleCheckSession}
                disabled={loadingSession}
              >
                {loadingSession ? "Loading..." : "Check status"}
              </button>
            </div>
            {sessionStatus && (
              <pre className="session-status">
                {JSON.stringify(sessionStatus, null, 2)}
              </pre>
            )}
          </div>
        )}

        {loading && <div className="loading">Loading flags...</div>}
        {error && <div className="error">Error: {error}</div>}
        {!loading && !error && (
          <FlagsTable
            flags={flags}
            onFlagUpdate={handleFlagUpdate}
            onSessionStarted={handleSessionStarted}
          />
        )}
      </div>
    </div>
  );
}

export default App;


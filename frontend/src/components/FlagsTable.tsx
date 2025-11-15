import { useState } from "react";
import type { FeatureFlag, RiskLevel, Status } from "../types";
import { removeFlag } from "../api";
import "./FlagsTable.css";

interface FlagsTableProps {
  flags: FeatureFlag[];
  onFlagUpdate: (flag: FeatureFlag) => void;
  onSessionStarted: (sessionId: string, flagName: string) => void;
}

export function FlagsTable({ flags, onFlagUpdate, onSessionStarted }: FlagsTableProps) {
  const [removingFlags, setRemovingFlags] = useState<Set<string>>(new Set());
  const [error, setError] = useState<string | null>(null);

  const handleRemove = async (flag: FeatureFlag) => {
    if (flag.status === "removing" || flag.status === "removed") {
      return;
    }

    setRemovingFlags((prev) => new Set(prev).add(flag.name));
    setError(null);

    try {
      const result = await removeFlag(flag.name);
      
      // Optimistically update the flag
      const updatedFlag: FeatureFlag = {
        ...flag,
        status: "removing",
        removal_session_id: result.session_id,
      };
      onFlagUpdate(updatedFlag);
      onSessionStarted(result.session_id, flag.name);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to start Devin session");
      setRemovingFlags((prev) => {
        const next = new Set(prev);
        next.delete(flag.name);
        return next;
      });
    }
  };

  const getRiskColor = (risk: RiskLevel): string => {
    switch (risk) {
      case "low":
        return "#10b981"; // green
      case "medium":
        return "#f59e0b"; // yellow
      case "high":
        return "#ef4444"; // red
      default:
        return "#6b7280"; // gray
    }
  };

  const getStatusBadge = (status: Status): string => {
    switch (status) {
      case "active":
        return "active";
      case "candidate_cleanup":
        return "candidate";
      case "removing":
        return "removing";
      case "removed":
        return "removed";
      default:
        return status;
    }
  };

  const formatDate = (dateStr: string): string => {
    return new Date(dateStr).toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  };

  return (
    <div className="flags-table-container">
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}
      <table className="flags-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Owner</th>
            <th>System</th>
            <th>Group</th>
            <th>Risk</th>
            <th>Date Created</th>
            <th>Last Used</th>
            <th>Status</th>
            <th>Ticket</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {flags.map((flag) => {
            const isRemoving = removingFlags.has(flag.name);
            const isDisabled = flag.status === "removing" || flag.status === "removed";
            
            return (
              <tr key={flag.name}>
                <td>
                  <div className="flag-name">{flag.name}</div>
                  <div className="flag-description">{flag.description}</div>
                </td>
                <td>{flag.owner}</td>
                <td>{flag.system}</td>
                <td>{flag.group}</td>
                <td>
                  <span
                    className="risk-chip"
                    style={{ backgroundColor: getRiskColor(flag.risk_level) }}
                  >
                    {flag.risk_level}
                  </span>
                </td>
                <td>{formatDate(flag.date_created)}</td>
                <td>{formatDate(flag.last_used)}</td>
                <td>
                  <span className={`status-badge status-${flag.status}`}>
                    {getStatusBadge(flag.status)}
                  </span>
                </td>
                <td>{flag.ticket_id || "-"}</td>
                <td>
                  <button
                    className="remove-button"
                    onClick={() => handleRemove(flag)}
                    disabled={isDisabled || isRemoving}
                  >
                    {isRemoving ? "Starting..." : "Remove flag via Devin"}
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}


import type { FeatureFlag } from "./types";

const API_BASE = "http://localhost:8000";

export async function getFlags(): Promise<FeatureFlag[]> {
  const response = await fetch(`${API_BASE}/flags`);
  if (!response.ok) {
    throw new Error(`Failed to fetch flags: ${response.statusText}`);
  }
  return response.json();
}

export async function removeFlag(flagName: string): Promise<{ session_id: string; message: string }> {
  const response = await fetch(`${API_BASE}/flags/${flagName}/remove`, {
    method: "POST",
  });
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(error.detail || `Failed to remove flag: ${response.statusText}`);
  }
  return response.json();
}

export async function getSession(sessionId: string): Promise<any> {
  const response = await fetch(`${API_BASE}/sessions/${sessionId}`);
  if (!response.ok) {
    throw new Error(`Failed to get session: ${response.statusText}`);
  }
  return response.json();
}


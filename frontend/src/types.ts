export type Status = "active" | "candidate_cleanup" | "removing" | "removed";
export type RiskLevel = "low" | "medium" | "high";

export interface FeatureFlag {
  name: string;
  description: string;
  owner: string;
  risk_level: RiskLevel;
  status: Status;
  date_created: string; // ISO date string
  last_used: string; // ISO date string
  system: string;
  group: string;
  ticket_id: string | null;
  notes: string | null;
  removal_session_id: string | null;
}


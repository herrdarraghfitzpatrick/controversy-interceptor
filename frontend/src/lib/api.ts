// Client for the Controversy Scanner detection API (spec section 5).

export type RiskCategory = "linguistic" | "historical" | "brand" | "recent_event" | "imagery";
export type Severity = "low" | "medium" | "high";

export interface Finding {
  span: string;
  category: RiskCategory;
  target_market: string;
  severity: Severity;
  confidence: number;
  explanation: string;
  precedent: string | null;
  suggested_fix: string | null;
}

export interface ScanRequest {
  text: string;
  target_markets: string[];
  industry: string;
  content_type: string;
  imagery_description?: string | null;
  check_recent_events?: boolean;
}

export interface ScanResponse {
  scan_id: string;
  scope_applied: string;
  findings: Finding[];
  checked_against_library_version: string;
  live_search_performed: boolean;
}

export interface ScanHistoryItem {
  scan_id: string;
  scope_applied: string;
  created_at: string;
  finding_count: number;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

export class ApiError extends Error {
  status: number;
  detail: unknown;

  constructor(status: number, detail: unknown) {
    super(typeof detail === "string" ? detail : `Request failed with status ${status}`);
    this.status = status;
    this.detail = detail;
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...init?.headers,
    },
    cache: "no-store",
  });

  if (!response.ok) {
    let detail: unknown = null;
    try {
      const body = await response.json();
      detail = body?.detail ?? body;
    } catch {
      // no JSON body
    }
    throw new ApiError(response.status, detail);
  }

  return response.json() as Promise<T>;
}

export function createScan(payload: ScanRequest): Promise<ScanResponse> {
  return request<ScanResponse>("/scan", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export function getScan(scanId: string): Promise<ScanResponse> {
  return request<ScanResponse>(`/scan/${scanId}`);
}

export function listScans(limit = 50): Promise<ScanHistoryItem[]> {
  return request<ScanHistoryItem[]>(`/scans?limit=${limit}`);
}

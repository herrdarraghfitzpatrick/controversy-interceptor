import { Badge } from "@/components/ui/badge";
import type { Severity } from "@/lib/api";

const LABELS: Record<Severity, string> = {
  high: "High",
  medium: "Medium",
  low: "Low",
};

export function SeverityBadge({ severity }: { severity: Severity }) {
  return <Badge variant={severity}>{LABELS[severity]}</Badge>;
}

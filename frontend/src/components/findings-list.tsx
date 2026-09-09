import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { SeverityBadge } from "@/components/severity-badge";
import type { Finding, Severity } from "@/lib/api";
import { SEVERITY_ORDER } from "@/lib/constants";

const CATEGORY_LABELS: Record<Finding["category"], string> = {
  linguistic: "Linguistic",
  historical: "Historical",
  brand: "Brand / IP",
  recent_event: "Recent event",
  imagery: "Imagery",
};

function FindingRow({ finding, index }: { finding: Finding; index: number }) {
  return (
    <AccordionItem value={`finding-${index}`}>
      <AccordionTrigger>
        <div className="flex flex-1 flex-wrap items-center gap-2 pr-2 text-left">
          <span className="font-semibold">&ldquo;{finding.span}&rdquo;</span>
          <Badge variant="outline">{CATEGORY_LABELS[finding.category]}</Badge>
          <span className="text-xs text-muted-foreground">{finding.target_market}</span>
          <span className="ml-auto text-xs text-muted-foreground">
            {Math.round(finding.confidence * 100)}% confidence
          </span>
        </div>
      </AccordionTrigger>
      <AccordionContent>
        <div className="flex flex-col gap-3 text-sm">
          <div>
            <p className="mb-1 font-medium text-foreground">Why this is risky</p>
            <p className="text-muted-foreground">{finding.explanation}</p>
          </div>
          {finding.precedent && (
            <div>
              <p className="mb-1 font-medium text-foreground">Precedent</p>
              <p className="text-muted-foreground">{finding.precedent}</p>
            </div>
          )}
          {finding.suggested_fix && (
            <div>
              <p className="mb-1 font-medium text-foreground">Suggested fix</p>
              <p className="text-muted-foreground">{finding.suggested_fix}</p>
            </div>
          )}
        </div>
      </AccordionContent>
    </AccordionItem>
  );
}

export function FindingsList({ findings }: { findings: Finding[] }) {
  if (findings.length === 0) {
    return (
      <Card>
        <CardContent className="pt-6 text-sm text-muted-foreground">
          No findings. Nothing in this copy tripped the case library or the Claude passes for this scope.
        </CardContent>
      </Card>
    );
  }

  const groups = SEVERITY_ORDER.map((severity) => ({
    severity,
    items: findings.filter((f) => f.severity === severity),
  })).filter((group) => group.items.length > 0);

  return (
    <div className="flex flex-col gap-4">
      {groups.map(({ severity, items }) => (
        <Card key={severity}>
          <CardHeader className="flex-row items-center justify-between space-y-0">
            <CardTitle className="flex items-center gap-2 text-base">
              <SeverityBadge severity={severity as Severity} />
              <span>
                {items.length} finding{items.length > 1 ? "s" : ""}
              </span>
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-0">
            <Accordion type="multiple">
              {items.map((finding, index) => (
                <FindingRow key={`${severity}-${index}`} finding={finding} index={index} />
              ))}
            </Accordion>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

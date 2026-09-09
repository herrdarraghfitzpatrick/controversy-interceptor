import Link from "next/link";
import { notFound } from "next/navigation";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { FindingsList } from "@/components/findings-list";
import { ApiError, getScan } from "@/lib/api";

export default async function ScanReportPage(props: PageProps<"/scans/[id]">) {
  const { id } = await props.params;

  let scan;
  try {
    scan = await getScan(id);
  } catch (err) {
    if (err instanceof ApiError && err.status === 404) {
      notFound();
    }
    throw err;
  }

  const bySeverity = { high: 0, medium: 0, low: 0 } as Record<string, number>;
  for (const finding of scan.findings) {
    bySeverity[finding.severity] = (bySeverity[finding.severity] ?? 0) + 1;
  }

  return (
    <div className="flex flex-col gap-6">
      <div>
        <Link href="/" className="text-sm text-muted-foreground hover:underline">
          &larr; New scan
        </Link>
        <h1 className="mt-2 text-2xl font-semibold tracking-tight">Scan report</h1>
        <p className="mt-1 text-sm text-muted-foreground">{scan.scope_applied}</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Summary</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-wrap items-center gap-4 text-sm">
          <span className="flex items-center gap-1.5">
            {scan.findings.length} total finding{scan.findings.length === 1 ? "" : "s"}
          </span>
          {bySeverity.high > 0 && <Badge variant="high">{bySeverity.high} high</Badge>}
          {bySeverity.medium > 0 && <Badge variant="medium">{bySeverity.medium} medium</Badge>}
          {bySeverity.low > 0 && <Badge variant="low">{bySeverity.low} low</Badge>}
          <span className="ml-auto text-xs text-muted-foreground">
            Library version: {scan.checked_against_library_version}
          </span>
          {scan.live_search_performed && (
            <Badge variant="outline" className="text-xs">
              Live search performed
            </Badge>
          )}
        </CardContent>
      </Card>

      <FindingsList findings={scan.findings} />
    </div>
  );
}

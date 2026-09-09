import Link from "next/link";

import { Card, CardContent } from "@/components/ui/card";
import { listScans } from "@/lib/api";

function formatDate(iso: string) {
  return new Date(iso).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

export default async function HistoryPage() {
  const scans = await listScans();

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Scan history</h1>
        <p className="mt-1 text-sm text-muted-foreground">Past scans, most recent first.</p>
      </div>

      {scans.length === 0 ? (
        <Card>
          <CardContent className="pt-6 text-sm text-muted-foreground">
            No scans yet. <Link href="/" className="underline">Run your first scan</Link>.
          </CardContent>
        </Card>
      ) : (
        <div className="flex flex-col gap-3">
          {scans.map((scan) => (
            <Link key={scan.scan_id} href={`/scans/${scan.scan_id}`}>
              <Card className="transition-colors hover:bg-accent">
                <CardContent className="flex flex-wrap items-center justify-between gap-2 pt-6">
                  <div className="flex flex-col gap-1">
                    <p className="text-sm font-medium">{scan.scope_applied}</p>
                    <p className="text-xs text-muted-foreground">{formatDate(scan.created_at)}</p>
                  </div>
                  <span className="text-sm text-muted-foreground">
                    {scan.finding_count} finding{scan.finding_count === 1 ? "" : "s"}
                  </span>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

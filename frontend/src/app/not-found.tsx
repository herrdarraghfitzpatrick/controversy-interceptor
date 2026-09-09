import Link from "next/link";

import { Button } from "@/components/ui/button";

export default function NotFound() {
  return (
    <div className="flex flex-col items-center gap-4 py-16 text-center">
      <h1 className="text-2xl font-semibold tracking-tight">Not found</h1>
      <p className="text-sm text-muted-foreground">That scan doesn&apos;t exist, or the link is wrong.</p>
      <Button asChild>
        <Link href="/">Start a new scan</Link>
      </Button>
    </div>
  );
}

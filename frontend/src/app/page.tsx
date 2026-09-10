"use client";

import * as React from "react";
import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { MultiSelectTags } from "@/components/multi-select-tags";
import { ApiError, createScan } from "@/lib/api";
import {
  CONTENT_TYPE_OPTIONS,
  INDUSTRY_OPTIONS,
  MAX_IMAGERY_DESCRIPTION_LENGTH,
  MAX_TEXT_LENGTH,
  TARGET_MARKET_OPTIONS,
} from "@/lib/constants";
import { cn } from "@/lib/utils";

export default function ScanFormPage() {
  const router = useRouter();

  const [text, setText] = React.useState("");
  const [targetMarkets, setTargetMarkets] = React.useState<string[]>([]);
  const [industry, setIndustry] = React.useState("");
  const [contentType, setContentType] = React.useState("");
  const [imageryDescription, setImageryDescription] = React.useState("");
  const [checkRecentEvents, setCheckRecentEvents] = React.useState(false);

  const [submitting, setSubmitting] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  const canSubmit = text.trim().length > 0 && targetMarkets.length > 0 && industry !== "" && contentType !== "";

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (!canSubmit || submitting) return;

    setSubmitting(true);
    setError(null);
    try {
      const scan = await createScan({
        text,
        target_markets: targetMarkets,
        industry,
        content_type: contentType,
        imagery_description: imageryDescription.trim() || null,
        check_recent_events: checkRecentEvents,
      });
      router.push(`/scans/${scan.scan_id}`);
    } catch (err) {
      if (err instanceof ApiError) {
        setError(typeof err.detail === "string" ? err.detail : err.message);
      } else {
        setError("Something went wrong submitting the scan. Please try again.");
      }
      setSubmitting(false);
    }
  }

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Scan campaign copy</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Paste text or a brief and scope the scan to a market, industry, and content type.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>New scan</CardTitle>
          <CardDescription>Every field below scopes the detection lenses to your campaign.</CardDescription>
        </CardHeader>
        <CardContent>
          <form className="flex flex-col gap-5" onSubmit={handleSubmit}>
            <div className="flex flex-col gap-2">
              <div className="flex items-baseline justify-between">
                <Label htmlFor="copy">Campaign copy or brief</Label>
                <span
                  className={cn(
                    "text-xs tabular-nums text-muted-foreground",
                    text.length > MAX_TEXT_LENGTH * 0.9 && "text-severity-medium",
                    text.length >= MAX_TEXT_LENGTH && "text-severity-high",
                  )}
                >
                  {text.length.toLocaleString()} / {MAX_TEXT_LENGTH.toLocaleString()}
                </span>
              </div>
              <Textarea
                id="copy"
                required
                rows={8}
                maxLength={MAX_TEXT_LENGTH}
                placeholder="Paste your campaign copy, brief, or press release here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
              />
              <p className="text-xs text-muted-foreground">
                For the copy itself - not a full report or whitepaper. Long documents should be trimmed to the
                relevant passage before scanning.
              </p>
            </div>

            <div className="grid gap-5 sm:grid-cols-2">
              <div className="flex flex-col gap-2">
                <Label htmlFor="markets">Target market(s)</Label>
                <MultiSelectTags
                  id="markets"
                  options={[...TARGET_MARKET_OPTIONS]}
                  value={targetMarkets}
                  onChange={setTargetMarkets}
                  placeholder="Select target markets"
                />
              </div>

              <div className="flex flex-col gap-2">
                <Label htmlFor="industry">Industry</Label>
                <Select value={industry} onValueChange={setIndustry}>
                  <SelectTrigger id="industry">
                    <SelectValue placeholder="Select industry" />
                  </SelectTrigger>
                  <SelectContent>
                    {INDUSTRY_OPTIONS.map((option) => (
                      <SelectItem key={option.value} value={option.value}>
                        {option.label}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            <div className="flex flex-col gap-2">
              <Label htmlFor="content-type">Content type</Label>
              <Select value={contentType} onValueChange={setContentType}>
                <SelectTrigger id="content-type" className="sm:w-1/2">
                  <SelectValue placeholder="Select content type" />
                </SelectTrigger>
                <SelectContent>
                  {CONTENT_TYPE_OPTIONS.map((option) => (
                    <SelectItem key={option.value} value={option.value}>
                      {option.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <p className="text-xs text-muted-foreground">
                Format changes severity: public/durable formats (ads, press releases) score higher than
                internal/ephemeral ones.
              </p>
            </div>

            <div className="flex flex-col gap-2">
              <Label htmlFor="imagery">Imagery description (optional)</Label>
              <Textarea
                id="imagery"
                rows={3}
                maxLength={MAX_IMAGERY_DESCRIPTION_LENGTH}
                placeholder="Describe any visuals, colors, gestures, or symbols in the campaign, for the imagery lens..."
                value={imageryDescription}
                onChange={(e) => setImageryDescription(e.target.value)}
              />
            </div>

            <label className="flex cursor-pointer items-start gap-2 rounded-md border border-border p-3 text-sm">
              <Checkbox
                checked={checkRecentEvents}
                onCheckedChange={(checked) => setCheckRecentEvents(checked === true)}
                className="mt-0.5"
              />
              <span>
                <span className="font-medium">Check against very recent events (live web search)</span>
                <br />
                <span className="text-muted-foreground">
                  Slower and costlier than the rest of the scan. Recommended for high-stakes scans (paid ads, press
                  releases) rather than every scan.
                </span>
              </span>
            </label>

            {error && (
              <p className="rounded-md border border-severity-high-border bg-severity-high-bg px-3 py-2 text-sm text-severity-high">
                {error}
              </p>
            )}

            <div>
              <Button type="submit" disabled={!canSubmit || submitting}>
                {submitting ? "Scanning..." : "Scan for controversy risk"}
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}

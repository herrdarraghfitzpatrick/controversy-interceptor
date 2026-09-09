"use client";

import * as React from "react";
import { X } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { cn } from "@/lib/utils";

export interface MultiSelectOption {
  value: string;
  label: string;
}

interface MultiSelectTagsProps {
  options: MultiSelectOption[];
  value: string[];
  onChange: (value: string[]) => void;
  placeholder?: string;
  id?: string;
}

export function MultiSelectTags({ options, value, onChange, placeholder, id }: MultiSelectTagsProps) {
  const [open, setOpen] = React.useState(false);
  const labelFor = (v: string) => options.find((o) => o.value === v)?.label ?? v;

  function toggle(optionValue: string) {
    if (value.includes(optionValue)) {
      onChange(value.filter((v) => v !== optionValue));
    } else {
      onChange([...value, optionValue]);
    }
  }

  function remove(optionValue: string) {
    onChange(value.filter((v) => v !== optionValue));
  }

  return (
    <div className="flex flex-col gap-2">
      <Popover open={open} onOpenChange={setOpen}>
        <PopoverTrigger asChild>
          <Button
            id={id}
            type="button"
            variant="outline"
            role="combobox"
            aria-expanded={open}
            className="h-auto min-h-9 w-full justify-start px-3 py-2 font-normal"
          >
            <span className={cn("text-sm", value.length === 0 && "text-muted-foreground")}>
              {value.length === 0 ? placeholder ?? "Select..." : `${value.length} market${value.length > 1 ? "s" : ""} selected`}
            </span>
          </Button>
        </PopoverTrigger>
        <PopoverContent className="max-h-72 overflow-y-auto">
          <div className="flex flex-col gap-1">
            {options.map((option) => {
              const checked = value.includes(option.value);
              return (
                <label
                  key={option.value}
                  className="flex cursor-pointer items-center gap-2 rounded-sm px-2 py-1.5 text-sm hover:bg-accent"
                >
                  <Checkbox checked={checked} onCheckedChange={() => toggle(option.value)} />
                  {option.label}
                </label>
              );
            })}
          </div>
        </PopoverContent>
      </Popover>

      {value.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {value.map((v) => (
            <Badge key={v} variant="secondary" className="gap-1 pr-1.5">
              {labelFor(v)}
              <button
                type="button"
                onClick={() => remove(v)}
                aria-label={`Remove ${labelFor(v)}`}
                className="rounded-full p-0.5 hover:bg-foreground/10"
              >
                <X className="h-3 w-3" />
              </button>
            </Badge>
          ))}
        </div>
      )}
    </div>
  );
}

// Mirrors app/services/scope.py MARKET_NAMES on the backend, and the
// industry/content-type vocabulary used across app/seed/cases.py.

export const TARGET_MARKET_OPTIONS = [
  { value: "IE", label: "Ireland" },
  { value: "GB", label: "United Kingdom" },
  { value: "US", label: "United States" },
  { value: "KR", label: "South Korea" },
  { value: "JP", label: "Japan" },
  { value: "CN", label: "China" },
  { value: "FR", label: "France" },
  { value: "DE", label: "Germany" },
  { value: "IN", label: "India" },
  { value: "AU", label: "Australia" },
  { value: "CA", label: "Canada" },
  { value: "BR", label: "Brazil" },
  { value: "MX", label: "Mexico" },
  { value: "ES", label: "Spain" },
  { value: "IT", label: "Italy" },
  { value: "NL", label: "Netherlands" },
  { value: "SE", label: "Sweden" },
  { value: "ZA", label: "South Africa" },
  { value: "NG", label: "Nigeria" },
  { value: "AE", label: "United Arab Emirates" },
  { value: "SA", label: "Saudi Arabia" },
  { value: "SG", label: "Singapore" },
] as const;

export const INDUSTRY_OPTIONS = [
  { value: "fintech", label: "Fintech" },
  { value: "fmcg", label: "FMCG" },
  { value: "food_beverage", label: "Food & Beverage" },
  { value: "healthcare", label: "Healthcare" },
  { value: "fashion", label: "Fashion" },
  { value: "automotive", label: "Automotive" },
  { value: "tech", label: "Tech" },
  { value: "retail", label: "Retail" },
  { value: "travel", label: "Travel" },
  { value: "entertainment", label: "Entertainment" },
  { value: "fitness", label: "Fitness" },
  { value: "gambling", label: "Gambling" },
  { value: "agriculture", label: "Agriculture" },
  { value: "other", label: "Other" },
] as const;

export const CONTENT_TYPE_OPTIONS = [
  { value: "PR blog post", label: "PR blog post" },
  { value: "press release", label: "Press release" },
  { value: "paid social ad", label: "Paid social ad" },
  { value: "social media post", label: "Social media post" },
  { value: "billboard", label: "Billboard" },
  { value: "TV ad", label: "TV ad" },
  { value: "print ad", label: "Print ad" },
  { value: "website copy", label: "Website copy" },
  { value: "product packaging", label: "Product packaging" },
  { value: "internal comms", label: "Internal comms" },
  { value: "internal memo", label: "Internal memo" },
  { value: "draft", label: "Draft" },
  { value: "employee newsletter", label: "Employee newsletter" },
] as const;

export const SEVERITY_ORDER = ["high", "medium", "low"] as const;

// Mirrors app/schemas/scan.py MAX_TEXT_LENGTH / MAX_IMAGERY_DESCRIPTION_LENGTH.
export const MAX_TEXT_LENGTH = 20_000;
export const MAX_IMAGERY_DESCRIPTION_LENGTH = 2_000;

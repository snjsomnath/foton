import type { StatusPayload, WeatherSummary } from "./types";

export async function fetchStatus(): Promise<StatusPayload> {
  const response = await fetch("/api/status");
  if (!response.ok) throw new Error(`Status request failed: ${response.status}`);
  return response.json() as Promise<StatusPayload>;
}

export async function uploadWeather(
  file: File,
  northRotationDegrees: number,
): Promise<WeatherSummary> {
  const body = new FormData();
  body.append("file", file);
  body.append("north_rotation_degrees", String(northRotationDegrees));
  const response = await fetch("/api/weather", { method: "POST", body });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || `Weather upload failed: ${response.status}`);
  }
  return response.json() as Promise<WeatherSummary>;
}

export function sessionSocketUrl(): string {
  const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
  return `${protocol}//${window.location.host}/api/session`;
}

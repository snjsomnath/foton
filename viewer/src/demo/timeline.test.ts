import { describe, expect, it } from "vitest";
import { CHAPTERS, DEFAULT_PARAMETERS, PlaybackClock, SHOTS, TOTAL_DURATION, june21Hour } from "./timeline";

function advance(clock: PlaybackClock, seconds: number, ready = true) {
  let transitions = 0;
  for (let i = 0; i < seconds * 20; i++) if (clock.tick(0.05, ready)) transitions++;
  return transitions;
}
describe("cinematic timeline", () => {
  it("covers eight chapters, four metrics, and a 72-second edit", () => {
    expect(CHAPTERS).toHaveLength(8);
    expect(TOTAL_DURATION).toBeCloseTo(72);
    expect(new Set(SHOTS.map((shot) => shot.metric)).size).toBe(4);
    expect(SHOTS.find(shot => shot.chapter === "Hourly analysis")!.parameters).toEqual(DEFAULT_PARAMETERS);
    expect(SHOTS.filter((shot) => shot.quality === "final").length).toBeGreaterThan(6);
    expect(june21Hour(9)).toBe(4113);
  });
  it("connects camera keyframes and widens before each campus increase", () => {
    for (let i = 1; i < SHOTS.length; i++) {
      expect(SHOTS[i].camera).toEqual(SHOTS[i-1].cameraEnd);
      expect(Math.abs(SHOTS[i].cameraEnd[0] - SHOTS[i].camera[0])).toBeLessThanOrEqual(180);
    }
    const reveal = SHOTS.find(s => s.parameters.room_count === 1024)!;
    expect(reveal.focus).toBe("scene");
    const scale = SHOTS.filter(s => s.chapter === "Multiple zones");
    for (let i = 1; i < scale.length; i++) {
      expect(scale[i].overview!.from).toEqual(scale[i-1].overview!.to);
      expect(scale[i].focus).toBe("scene");
    }
    expect(reveal.focusEnd).toBe("scene");
    expect(reveal.duration).toBe(8);
  });
  it("waits for results and preserves time when paused", () => {
    const clock = new PlaybackClock();
    clock.playing = true;
    advance(clock, 20, false);
    expect(clock.elapsed).toBe(0);
    advance(clock, 0.5);
    const elapsed = clock.elapsed;
    clock.playing = false;
    advance(clock, 20);
    expect(clock.elapsed).toBe(elapsed);
    clock.playing = true;
    expect(advance(clock, 1.6)).toBe(1);
    expect(clock.index).toBe(1);
  });
  it("supports jumps, restart, end-card hold, and looping", () => {
    const clock = new PlaybackClock();
    clock.restart();
    clock.jump(SHOTS.length - 1);
    advance(clock, 7.1);
    expect(clock.ended).toBe(true);
    expect(clock.playing).toBe(false);
    expect(clock.progress).toBe(1);
    clock.restart();
    expect(clock.index).toBe(0);
    expect(clock.ended).toBe(false);
    clock.loop = true;
    clock.jump(SHOTS.length - 1);
    advance(clock, 7.1);
    expect(clock.index).toBe(0);
    expect(clock.playing).toBe(true);
  });
  it("requires result readiness again at each shot boundary", () => {
    const clock = new PlaybackClock();
    clock.restart();
    advance(clock, 2.1);
    const elapsed = clock.elapsed;
    advance(clock, 20, false);
    expect(clock.index).toBe(1);
    expect(clock.elapsed).toBe(elapsed);
  });
});

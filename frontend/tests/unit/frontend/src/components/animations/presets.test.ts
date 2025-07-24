import { presets } from "src/components/animations/presets";

describe('Animation Presets', () => {
  it('should export an object with animation presets', () => {
    expect(presets).toBeDefined();
    expect(typeof presets).toBe('object');
    expect(Object.keys(presets).length).toBeGreaterThan(0);
  });
  // Add more specific tests for individual presets if needed
  it('should have a fade preset', () => {
    expect(presets.fade).toBeDefined();
    expect(typeof presets.fade).toBe('object');
    expect(presets.fade.type).toBeDefined();
  });
});
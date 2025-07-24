import { isMobile, isTablet } from "src/components/layout/ResponsiveUtils";

describe('ResponsiveUtils', () => {
  // Mock window.innerWidth for testing different screen sizes
  const originalInnerWidth = window.innerWidth;

  afterEach(() => {
    window.innerWidth = originalInnerWidth;
  });

  it('should detect mobile devices', () => {
    window.innerWidth = 767;
    expect(isMobile()).toBe(true);
    expect(isTablet()).toBe(false);
  });
  it('should detect tablet devices', () => {
    window.innerWidth = 1024;
    expect(isMobile()).toBe(false);
    expect(isTablet()).toBe(true);
  });
  it('should detect desktop devices', () => {
    window.innerWidth = 1280;
    expect(isMobile()).toBe(false);
    expect(isTablet()).toBe(false);
  });
});
import { renderHook } from '@testing-library/react-hooks';
import { useTheme } from "src/hooks/useTheme";

describe('useTheme Hook', () => {
  it('should return the current theme', () => {
    const { result } = renderHook(() => useTheme());
    expect(result.current).toBeDefined();
    expect(result.current.name).toBeDefined();
    expect(result.current.colors).toBeDefined();
  });
});
import { renderHook, act } from '@testing-library/react-hooks';
import { useAnimations } from "src/hooks/useAnimations";

describe('useAnimations Hook', () => {
  it('should initialize with default values', () => {
    const { result } = renderHook(() => useAnimations());
    expect(result.current.animations).toEqual({});
    expect(result.current.startAnimation).toBeDefined();
  });
  it('should add animations', () => {
    const { result } = renderHook(() => useAnimations());
    act(() => {
      result.current.startAnimation('fade', 1000);
    });
    expect(result.current.animations).toHaveProperty('fade');
  });
  // Add more tests for animation cleanup and error handling
});
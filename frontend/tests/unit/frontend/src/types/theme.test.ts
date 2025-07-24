import { Theme } from "src/types/theme";

describe('Theme Types', () => {
  it('should define a Theme type with correct properties', () => {
    const theme: Theme = {
      name: 'light',
      colors: {
        primary: '#007bff',
        secondary: '#6c757d',
        background: '#fff',
        text: '#343a40',
      },
    };
    expect(theme).toBeDefined();
    expect(theme.name).toBeDefined();
    expect(theme.colors).toBeDefined();
    expect(theme.colors.primary).toBeDefined();
    expect(theme.colors.secondary).toBeDefined();
    expect(theme.colors.background).toBeDefined();
    expect(theme.colors.text).toBeDefined();
  });
});
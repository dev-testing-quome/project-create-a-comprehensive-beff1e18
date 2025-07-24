import { render, screen } from '@testing-library/react';
import { ThemeProvider, ThemeContext } from "src/contexts/ThemeContext";

describe('ThemeContext', () => {
  it('should render children within the ThemeProvider', () => {
    render(
      <ThemeProvider>
        <div>Test</div>
      </ThemeProvider>
    );
    expect(screen.getByText('Test')).toBeInTheDocument();
  });
  it('should provide the theme context', () => {
    const theme = { name: 'light', colors: { primary: 'blue' } };
    render(
      <ThemeProvider value={theme}>
        <ThemeContext.Consumer>
          {({ theme: contextTheme }) => <div>{contextTheme.name}</div>}
        </ThemeContext.Consumer>
      </ThemeProvider>
    );
    expect(screen.getByText('light')).toBeInTheDocument();
  });
});
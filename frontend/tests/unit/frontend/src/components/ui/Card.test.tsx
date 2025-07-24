import { render, screen } from '@testing-library/react';
import Card from "src/components/ui/Card";

describe('Card Component', () => {
  it('should render a card with children', () => {
    render(<Card>Card content</Card>);
    expect(screen.getByText('Card content')).toBeInTheDocument();
  });
  // Add more tests for props like title, image etc.
});
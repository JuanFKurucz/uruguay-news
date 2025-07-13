import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Mock React Query
jest.mock('@tanstack/react-query', () => ({
  QueryClient: jest.fn().mockImplementation(() => ({})),
  QueryClientProvider: ({ children }: { children: React.ReactNode }) => children,
  ReactQueryDevtools: () => null,
}));

test('renders Uruguay News app', () => {
  render(<App />);
  const headerElement = screen.getByText(/Uruguay News/i);
  expect(headerElement).toBeInTheDocument();
});

test('renders navigation links', () => {
  render(<App />);
  const dashboardLink = screen.getByText(/Dashboard/i);
  const analysisLink = screen.getByText(/News Analysis/i);
  const aboutLink = screen.getByText(/About/i);
  
  expect(dashboardLink).toBeInTheDocument();
  expect(analysisLink).toBeInTheDocument();
  expect(aboutLink).toBeInTheDocument();
}); 
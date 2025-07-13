import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

// Components
import Header from './components/Header';
import Dashboard from './pages/Dashboard';
import NewsAnalysis from './pages/NewsAnalysis';
import About from './pages/About';

// Styles
import './App.css';

// Create a client for React Query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 3,
      staleTime: 5 * 60 * 1000, // 5 minutes
    },
  },
});

/**
 * Main application component that sets up routing and data fetching.
 * Configures React Query for API data management and defines the main routes.
 * 
 * @returns {JSX.Element} The root App component with routing and query providers
 */
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router basename="/uruguay-news">
        <div className="min-h-screen bg-gray-50">
          <Header />
          <main className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/analysis" element={<NewsAnalysis />} />
              <Route path="/about" element={<About />} />
            </Routes>
          </main>
        </div>
      </Router>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}

export default App; 
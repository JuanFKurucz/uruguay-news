import React from 'react';

interface DashboardMetrics {
  articlesAnalyzed: number;
  averageSentiment: number | null;
  biasDetectionScore: number | null;
}

interface DashboardData {
  metrics: DashboardMetrics;
  recentAnalyses: Array<{
    id: string;
    title: string;
    sentiment: number;
    bias: number;
    timestamp: Date;
  }>;
}

/**
 * Dashboard component displays the main overview of the Uruguay News Analysis System.
 * Shows key metrics including articles analyzed, sentiment scores, and bias detection results.
 * 
 * @returns {JSX.Element} The Dashboard page component
 */
const Dashboard: React.FC = () => {
  // TODO: Replace with actual data fetching
  const mockData: DashboardData = {
    metrics: {
      articlesAnalyzed: 0,
      averageSentiment: null,
      biasDetectionScore: null
    },
    recentAnalyses: []
  };

  return (
    <div className="space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Uruguay News Dashboard
        </h1>
        <p className="text-lg text-gray-600">
          AI-powered news analysis platform for Uruguay
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Articles Analyzed
          </h3>
          <p className="text-3xl font-bold text-blue-600">{mockData.metrics.articlesAnalyzed}</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Sentiment Score
          </h3>
          <p className="text-3xl font-bold text-green-600">
            {mockData.metrics.averageSentiment ?? 'N/A'}
          </p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Bias Detection
          </h3>
          <p className="text-3xl font-bold text-yellow-600">
            {mockData.metrics.biasDetectionScore ?? 'N/A'}
          </p>
        </div>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Recent Analysis
        </h3>
        <p className="text-gray-600">
          No recent analysis available. Start by analyzing your first article!
        </p>
      </div>
    </div>
  );
};

export default Dashboard; 
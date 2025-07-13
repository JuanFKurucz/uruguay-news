import React from 'react';

const Dashboard: React.FC = () => {
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
          <p className="text-3xl font-bold text-blue-600">0</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Sentiment Score
          </h3>
          <p className="text-3xl font-bold text-green-600">N/A</p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Bias Detection
          </h3>
          <p className="text-3xl font-bold text-yellow-600">N/A</p>
        </div>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Recent Analysis
        </h3>
        <p className="text-gray-600">
          No articles analyzed yet. Start by analyzing some news content!
        </p>
      </div>
    </div>
  );
};

export default Dashboard; 
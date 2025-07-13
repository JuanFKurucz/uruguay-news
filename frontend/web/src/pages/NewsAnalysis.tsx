import React from 'react';

const NewsAnalysis: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          News Analysis
        </h1>
        <p className="text-lg text-gray-600">
          Analyze news articles for sentiment and bias
        </p>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Analyze Article
        </h3>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Article URL
            </label>
            <input
              type="url"
              placeholder="https://example.com/article"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Or paste article text
            </label>
            <textarea
              rows={6}
              placeholder="Paste article content here..."
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          
          <button className="btn-primary">
            Analyze Article
          </button>
        </div>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Analysis Results
        </h3>
        <p className="text-gray-600">
          Analysis results will appear here after processing an article.
        </p>
      </div>
    </div>
  );
};

export default NewsAnalysis; 
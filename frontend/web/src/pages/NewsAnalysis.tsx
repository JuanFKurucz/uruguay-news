import React, { useState } from 'react';

/**
 * NewsAnalysis component provides a user interface for analyzing news articles.
 * Allows users to input article URLs or text for sentiment and bias analysis.
 * 
 * @returns {JSX.Element} The NewsAnalysis page component
 */
const NewsAnalysis: React.FC = () => {
  const [articleUrl, setArticleUrl] = useState('');
  const [articleText, setArticleText] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleAnalyze = async () => {
    if (!articleUrl && !articleText) return;
    setIsAnalyzing(true);
    // TODO: Implement analysis logic
    setTimeout(() => {
      setIsAnalyzing(false);
    }, 2000); // Simulate API call
  };

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
            <label 
              htmlFor="article-url"
              className="block text-sm font-medium text-gray-700 mb-2"
            >
              Article URL
            </label>
            <input
              id="article-url"
              type="url"
              value={articleUrl}
              onChange={(e) => setArticleUrl(e.target.value)}
              placeholder="https://example.com/article"
              aria-describedby="url-help"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <p id="url-help" className="text-sm text-gray-500 mt-1">
              Enter the URL of the news article you want to analyze
            </p>
          </div>
          
          <div>
            <label 
              htmlFor="article-text"
              className="block text-sm font-medium text-gray-700 mb-2"
            >
              Or paste article text
            </label>
            <textarea
              id="article-text"
              rows={6}
              value={articleText}
              onChange={(e) => setArticleText(e.target.value)}
              placeholder="Paste article content here..."
              aria-describedby="text-help"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <p id="text-help" className="text-sm text-gray-500 mt-1">
              Alternatively, paste the full text of the article directly
            </p>
          </div>
          
          <button 
            className="btn-primary"
            onClick={handleAnalyze}
            disabled={isAnalyzing || (!articleUrl && !articleText)}
            aria-describedby="analyze-help"
          >
            {isAnalyzing ? 'Analyzing...' : 'Analyze Article'}
          </button>
          <p id="analyze-help" className="text-sm text-gray-500">
            Click to start sentiment and bias analysis
          </p>
        </div>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Analysis Results
        </h3>
        <p className="text-gray-600">
          Results will appear here after analysis...
        </p>
      </div>
    </div>
  );
};

export default NewsAnalysis; 
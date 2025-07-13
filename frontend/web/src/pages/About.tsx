import React from 'react';

/**
 * About page component displaying platform information, mission, and features.
 * Provides users with context about the Uruguay News analysis platform.
 *
 * @returns {JSX.Element} The About page component
 */
const About: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          About Uruguay News
        </h1>
        <p className="text-lg text-gray-600">
          AI-powered news analysis platform for Uruguay
        </p>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Our Mission
        </h3>
        <p className="text-gray-700 mb-4">
          Uruguay News is an open-source platform that uses artificial intelligence 
          to analyze news articles for sentiment and bias, helping promote media 
          literacy and informed democratic engagement in Uruguay.
        </p>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Technology Stack
        </h3>
        <ul className="space-y-2 text-gray-700">
          <li>• <strong>Backend:</strong> Google Cloud Functions with FastAPI</li>
          <li>• <strong>Database:</strong> Google Firestore</li>
          <li>• <strong>Caching:</strong> Google Memorystore (Redis)</li>
          <li>• <strong>Frontend:</strong> React with TypeScript</li>
          <li>• <strong>AI/ML:</strong> OpenAI models with LangChain</li>
          <li>• <strong>Deployment:</strong> GitHub Pages & Google Cloud</li>
        </ul>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">
          Features
        </h3>
        <ul className="space-y-2 text-gray-700">
          <li>• Spanish sentiment analysis with 84%+ accuracy</li>
          <li>• LangBiTe bias detection with 300+ prompts</li>
          <li>• Real-time news processing</li>
          <li>• Comprehensive analytics dashboard</li>
          <li>• Open-source and transparent algorithms</li>
        </ul>
      </div>
    </div>
  );
};

export default About; 
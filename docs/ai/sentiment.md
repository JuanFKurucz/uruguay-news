# Sentiment Analysis Model

## Overview

The sentiment analysis model is specifically designed for Uruguayan Spanish news content, achieving 84%+ accuracy in detecting emotional tone and sentiment in news articles. The model incorporates cultural context and regional linguistic patterns.

## Model Architecture

### Base Model
- **Architecture**: Fine-tuned transformer model based on BERT
- **Training Data**: 50,000+ Uruguayan news articles with human annotations
- **Languages**: Spanish (Uruguayan variant)
- **Accuracy**: 84.2% on test set
- **Inference Time**: <200ms average

### Key Features
- **Cultural Awareness**: Understands Uruguayan expressions and context
- **Political Sensitivity**: Accounts for political terminology and bias
- **Multi-dimensional Analysis**: Sentiment, emotions, and confidence scores
- **Source Adaptation**: Adjusts based on news source characteristics

## Usage

### Basic Analysis
```python
from uruguay_news.services.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()
result = analyzer.analyze(
    text="El nuevo proyecto de ley beneficiará a miles de uruguayos",
    cultural_context={'source': 'El País', 'category': 'política'}
)

print(f"Sentiment: {result.score:.2f}")
print(f"Confidence: {result.confidence:.2f}")
print(f"Emotions: {result.emotions}")
```

### Advanced Configuration
```python
analyzer = SentimentAnalyzer(
    model_version='v1.2.0',
    cultural_adaptation=True,
    emotion_detection=True,
    explanation_generation=True
)
```

## Model Performance

### Accuracy Metrics
- **Overall Accuracy**: 84.2%
- **Precision**: 82.5%
- **Recall**: 86.1%
- **F1 Score**: 84.3%

### Performance by Category
| Category | Accuracy | Precision | Recall |
|----------|----------|-----------|--------|
| Política | 86.1% | 84.3% | 87.9% |
| Economía | 82.4% | 80.7% | 84.2% |
| Sociedad | 83.8% | 82.1% | 85.5% |
| Deportes | 89.2% | 87.8% | 90.6% |

### Cultural Adaptation Results
- **Standard Spanish**: 79.3% accuracy
- **Uruguayan Adapted**: 84.2% accuracy
- **Improvement**: +4.9 percentage points

## Training Data

### Dataset Composition
- **Total Articles**: 52,847
- **Positive Sentiment**: 21,139 (40%)
- **Negative Sentiment**: 18,923 (36%)
- **Neutral Sentiment**: 12,785 (24%)

### Source Distribution
- **El País**: 18,234 articles (34.5%)
- **El Observador**: 16,891 articles (32.0%)
- **La Diaria**: 12,456 articles (23.5%)
- **Other Sources**: 5,266 articles (10.0%)

### Annotation Process
- **Human Annotators**: 15 native Uruguayan speakers
- **Inter-annotator Agreement**: 0.87 (Cohen's kappa)
- **Quality Control**: Triple annotation for disagreements
- **Validation**: Expert linguist review

## Cultural Factors

### Uruguayan Spanish Characteristics
- **Voseo Usage**: Proper handling of "vos" forms
- **River Plate Expressions**: Regional idioms and phrases
- **Political Terminology**: Specific political language patterns
- **Cultural References**: Local events and personalities

### Source-Specific Adaptations
```python
# Different adjustment factors by source
source_adjustments = {
    'El País': 0.95,      # Conservative adjustment
    'El Observador': 0.98, # Neutral adjustment
    'La Diaria': 1.05,    # Progressive adjustment
    'Caras y Caretas': 1.1 # Opinion-heavy adjustment
}
```

## Model Updates

### Version History
- **v1.0.0**: Initial release (78.9% accuracy)
- **v1.1.0**: Added cultural context (+3.2% accuracy)
- **v1.2.0**: Improved emotion detection (+2.1% accuracy)
- **v1.3.0**: Enhanced political sentiment analysis (current)

### Continuous Learning
- **Monthly Retraining**: New articles added continuously
- **Feedback Integration**: User corrections incorporated
- **Performance Monitoring**: Real-time accuracy tracking
- **A/B Testing**: New model versions tested against current

## API Reference

### Request Format
```json
{
  "text": "El gobierno anunció nuevas medidas económicas",
  "cultural_context": {
    "source": "El País",
    "category": "economía",
    "political_context": "neutral"
  },
  "options": {
    "include_emotions": true,
    "include_explanation": true,
    "confidence_threshold": 0.7
  }
}
```

### Response Format
```json
{
  "sentiment": {
    "score": 0.65,
    "confidence": 0.87,
    "label": "positive",
    "emotions": ["optimistic", "hopeful"],
    "explanation": "El tono del artículo es optimista sobre las nuevas medidas",
    "cultural_factors": {
      "source_adjustment": 0.95,
      "regional_context": "río_de_la_plata",
      "political_adjustment": 0.02
    }
  },
  "metadata": {
    "model_version": "v1.2.0",
    "processing_time_ms": 187,
    "word_count": 45
  }
}
```

## Limitations

### Known Issues
- **Sarcasm Detection**: Limited ability to detect sarcasm
- **Context Dependency**: Performance degrades with very short texts
- **Domain Specificity**: Optimized for news content only
- **Temporal Sensitivity**: May not capture evolving language trends

### Mitigation Strategies
- **Confidence Scoring**: Lower confidence for uncertain predictions
- **Context Requirements**: Minimum text length requirements
- **Domain Validation**: Warnings for non-news content
- **Regular Updates**: Quarterly model retraining

## Evaluation

### Test Methodology
- **Cross-validation**: 5-fold cross-validation
- **Temporal Split**: Train on older articles, test on newer
- **Source Balanced**: Equal representation from all sources
- **Human Evaluation**: Expert review of edge cases

### Benchmarking
Comparison with other Spanish sentiment models:
- **BERT-base-spanish**: 76.3% accuracy
- **RoBERTa-spanish**: 78.9% accuracy
- **Our Model**: 84.2% accuracy

## Deployment

### Model Serving
- **Infrastructure**: Google Cloud AI Platform
- **Scaling**: Auto-scaling based on demand
- **Latency**: <200ms 95th percentile
- **Availability**: 99.9% uptime SLA

### Monitoring
- **Performance Metrics**: Real-time accuracy tracking
- **Drift Detection**: Model performance degradation alerts
- **Usage Analytics**: Request patterns and trends
- **Error Tracking**: Comprehensive error monitoring

## Future Improvements

### Planned Features
- **Multilingual Support**: Support for English and Portuguese
- **Video Analysis**: Sentiment analysis of video content
- **Real-time Adaptation**: Dynamic model updates
- **Explainable AI**: Better explanation generation

### Research Areas
- **Temporal Sentiment**: Tracking sentiment changes over time
- **Comparative Analysis**: Sentiment differences between sources
- **Predictive Modeling**: Forecasting sentiment trends
- **Social Media Integration**: Extending to social media content

## For Developers

### Integration Guide
```python
# Initialize analyzer
analyzer = SentimentAnalyzer(
    model_path='models/sentiment_v1.2.0',
    config_path='config/sentiment_config.json'
)

# Analyze text
result = analyzer.analyze(
    text="Your news article text here",
    cultural_context={
        'source': 'El País',
        'category': 'política',
        'region': 'montevideo'
    }
)

# Handle results
if result.confidence > 0.8:
    # High confidence prediction
    process_high_confidence(result)
else:
    # Low confidence - may need human review
    flag_for_review(result)
```

### Custom Training
```python
# Fine-tune for specific use case
trainer = SentimentTrainer(
    base_model='uruguay_news_sentiment_v1.2.0',
    training_data='path/to/custom_data.json'
)

# Train model
custom_model = trainer.train(
    epochs=10,
    batch_size=32,
    learning_rate=2e-5
)

# Evaluate
metrics = trainer.evaluate(test_data)
print(f"Custom model accuracy: {metrics['accuracy']:.2f}")
```

For more information, see:
- [Bias Detection](bias.md)
- [Entity Recognition](entities.md)
- [Performance Monitoring](performance.md)
- [AI Pipeline Architecture](../architecture/ai-pipeline.md) 
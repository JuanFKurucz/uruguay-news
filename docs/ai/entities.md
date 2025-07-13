# Entity Recognition Model

## Overview

The entity recognition model identifies and classifies named entities in Uruguayan news articles with 90%+ accuracy. The model is specifically trained to recognize Uruguayan politicians, organizations, locations, and cultural references.

## Model Architecture

### Base Model
- **Architecture**: Fine-tuned BERT-NER model
- **Training Data**: 35,000+ Uruguayan news articles
- **Entity Types**: PERSON, ORGANIZATION, LOCATION, EVENT, PRODUCT
- **Accuracy**: 90.3% F1 score

### Uruguayan-Specific Features
- **Political Entities**: Recognition of Uruguayan politicians and parties
- **Geographic Entities**: Departments, cities, neighborhoods
- **Cultural References**: Local events, institutions, organizations
- **Contextual Sentiment**: Sentiment analysis for each entity

## Usage

### Basic Analysis
```python
from uruguay_news.services.entities import EntityRecognizer

recognizer = EntityRecognizer()
result = recognizer.recognize(
    text="Luis Lacalle Pou visitó Montevideo para reunirse con el Frente Amplio"
)

for entity in result.entities:
    print(f"{entity.name}: {entity.type} (confidence: {entity.confidence:.2f})")
```

### Response Format
```json
{
  "entities": [
    {
      "name": "Luis Lacalle Pou",
      "type": "PERSON",
      "confidence": 0.98,
      "sentiment": 0.1,
      "mentions": 1,
      "context": "presidente de Uruguay",
      "political_party": "Partido Nacional"
    },
    {
      "name": "Montevideo",
      "type": "LOCATION",
      "confidence": 0.95,
      "sentiment": 0.0,
      "mentions": 1,
      "context": "capital de Uruguay",
      "department": "Montevideo"
    }
  ]
}
```

## Performance Metrics

### Accuracy by Entity Type
| Type | Precision | Recall | F1 Score |
|------|-----------|--------|----------|
| PERSON | 92.1% | 89.7% | 90.9% |
| ORGANIZATION | 88.5% | 86.3% | 87.4% |
| LOCATION | 94.2% | 91.8% | 93.0% |
| EVENT | 85.7% | 83.4% | 84.5% |
| PRODUCT | 87.3% | 84.9% | 86.1% |

For more information, see:
- [Sentiment Analysis](sentiment.md)
- [Bias Detection](bias.md)
- [Performance Monitoring](performance.md) 
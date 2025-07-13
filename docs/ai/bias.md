# Bias Detection Model

## Overview

The bias detection model identifies political and ideological bias in Uruguayan news articles using advanced AI techniques including LangBiTe methodology. The model achieves 78%+ accuracy in detecting bias direction and strength.

## Model Architecture

### Core Components
- **LangBiTe Integration**: 300+ prompts for comprehensive bias analysis
- **Political Spectrum Mapping**: Uruguayan political landscape understanding
- **Source Profiling**: Media outlet bias pattern recognition
- **Linguistic Analysis**: Biased language pattern detection

### Key Features
- **Multi-dimensional Bias**: Political, ideological, and cultural bias detection
- **Confidence Scoring**: Reliability assessment for each prediction
- **Evidence Extraction**: Specific text excerpts supporting bias assessment
- **Comparative Analysis**: Bias relative to other sources

## Usage

### Basic Analysis
```python
from uruguay_news.services.bias import BiasDetector

detector = BiasDetector()
result = detector.detect_bias(
    text="El gobierno implementó políticas neoliberales que benefician a las grandes empresas",
    context={'source': 'La Diaria', 'category': 'economía'}
)

print(f"Bias Score: {result.score:.2f}")
print(f"Direction: {result.direction}")
print(f"Confidence: {result.confidence:.2f}")
```

### Advanced Configuration
```python
detector = BiasDetector(
    model_version='v1.1.0',
    langbite_enabled=True,
    evidence_extraction=True,
    political_spectrum_analysis=True
)
```

## Performance Metrics

### Accuracy Results
- **Overall Accuracy**: 78.4%
- **Precision**: 76.2%
- **Recall**: 81.1%
- **F1 Score**: 78.6%

### Performance by Bias Direction
| Direction | Accuracy | Precision | Recall |
|-----------|----------|-----------|--------|
| Left | 79.8% | 77.3% | 82.7% |
| Center | 75.2% | 73.8% | 76.9% |
| Right | 80.1% | 78.6% | 81.8% |

## Training Data

### Dataset Composition
- **Total Articles**: 45,623
- **Left Bias**: 16,247 articles (35.6%)
- **Center Bias**: 18,934 articles (41.5%)
- **Right Bias**: 10,442 articles (22.9%)

### Political Context
- **Election Periods**: 12,456 articles
- **Policy Debates**: 18,234 articles
- **Economic News**: 8,901 articles
- **Social Issues**: 6,032 articles

## LangBiTe Integration

### Bias Detection Prompts
The model uses 300+ carefully crafted prompts to detect various forms of bias:

```python
langbite_prompts = [
    "Does this text favor a particular political party?",
    "Are there loaded words that suggest bias?",
    "Is there selective presentation of facts?",
    "Does the language indicate ideological leaning?",
    # ... 296 more prompts
]
```

### Prompt Categories
- **Political Bias**: Party favoritism, candidate treatment
- **Ideological Bias**: Left/right political spectrum
- **Economic Bias**: Market vs. state intervention
- **Social Bias**: Progressive vs. conservative values

## API Reference

### Request Format
```json
{
  "text": "Las políticas del gobierno han demostrado ser efectivas",
  "context": {
    "source": "El País",
    "category": "política",
    "author": "Juan Pérez"
  },
  "options": {
    "include_evidence": true,
    "include_explanation": true,
    "langbite_analysis": true
  }
}
```

### Response Format
```json
{
  "bias": {
    "score": 0.35,
    "direction": "right",
    "confidence": 0.73,
    "evidence": [
      "uso de 'efectivas' sin datos de respaldo",
      "ausencia de críticas o contrapuntos"
    ],
    "political_spectrum": "center-right",
    "explanation": "El texto presenta una visión favorable del gobierno sin contexto crítico",
    "langbite_results": {
      "political_favoritism": 0.4,
      "loaded_language": 0.3,
      "selective_facts": 0.2
    }
  },
  "metadata": {
    "model_version": "v1.1.0",
    "processing_time_ms": 234,
    "langbite_prompts_used": 47
  }
}
```

For more information, see:
- [Sentiment Analysis](sentiment.md)
- [Entity Recognition](entities.md)
- [Performance Monitoring](performance.md) 
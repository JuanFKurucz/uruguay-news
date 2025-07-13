# GraphQL API Documentation

## Overview

The Uruguay News Analysis System provides a GraphQL API for flexible data querying and real-time subscriptions. This API complements the REST API with more efficient data fetching and real-time capabilities.

## GraphQL Endpoint

```
Production: https://api.uruguaynews.com/graphql
Staging: https://api-staging.uruguaynews.com/graphql
```

## Authentication

Include the bearer token in the Authorization header:
```http
Authorization: Bearer <your-access-token>
```

## Schema Overview

### Core Types

#### Article
```graphql
type Article {
  id: ID!
  title: String!
  content: String!
  source: String!
  author: String
  publishedAt: DateTime!
  url: String
  wordCount: Int!
  language: String!
  analysis: Analysis
  tags: [String!]!
  createdAt: DateTime!
  updatedAt: DateTime!
}
```

#### Analysis
```graphql
type Analysis {
  id: ID!
  articleId: ID!
  sentiment: SentimentAnalysis!
  bias: BiasAnalysis!
  entities: [Entity!]!
  topics: TopicAnalysis!
  summary: String!
  confidence: Float!
  processedAt: DateTime!
  modelVersion: String!
}
```

#### SentimentAnalysis
```graphql
type SentimentAnalysis {
  score: Float!
  confidence: Float!
  emotions: [String!]!
  explanation: String!
  culturalFactors: CulturalFactors!
}

type CulturalFactors {
  sourceAdjustment: Float!
  politicalContext: String!
  regionalContext: String
}
```

#### BiasAnalysis
```graphql
type BiasAnalysis {
  score: Float!
  direction: BiasDirection!
  confidence: Float!
  evidence: [String!]!
  politicalSpectrum: String!
  explanation: String!
}

enum BiasDirection {
  LEFT
  CENTER
  RIGHT
}
```

#### Entity
```graphql
type Entity {
  name: String!
  type: EntityType!
  confidence: Float!
  sentiment: Float!
  mentions: Int!
  context: String!
}

enum EntityType {
  PERSON
  ORGANIZATION
  LOCATION
  EVENT
  PRODUCT
  OTHER
}
```

#### TopicAnalysis
```graphql
type TopicAnalysis {
  primary: String!
  secondary: [String!]!
  confidence: Float!
  categories: [String!]!
}
```

## Queries

### Get Article by ID
```graphql
query GetArticle($id: ID!) {
  article(id: $id) {
    id
    title
    content
    source
    author
    publishedAt
    analysis {
      sentiment {
        score
        confidence
        emotions
        explanation
      }
      bias {
        score
        direction
        confidence
        evidence
      }
      entities {
        name
        type
        confidence
        sentiment
        mentions
      }
      topics {
        primary
        secondary
        confidence
      }
    }
  }
}
```

**Variables:**
```json
{
  "id": "article-123"
}
```

### Get Articles with Filtering
```graphql
query GetArticles(
  $first: Int = 20
  $after: String
  $source: String
  $category: String
  $sentimentMin: Float
  $sentimentMax: Float
  $biasDirection: BiasDirection
  $fromDate: DateTime
  $toDate: DateTime
) {
  articles(
    first: $first
    after: $after
    filter: {
      source: $source
      category: $category
      sentimentRange: { min: $sentimentMin, max: $sentimentMax }
      biasDirection: $biasDirection
      dateRange: { from: $fromDate, to: $toDate }
    }
  ) {
    edges {
      node {
        id
        title
        source
        publishedAt
        analysis {
          sentiment {
            score
            confidence
          }
          bias {
            score
            direction
          }
        }
      }
      cursor
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    totalCount
  }
}
```

### Get Sentiment Trends
```graphql
query GetSentimentTrends(
  $period: TimePeriod!
  $source: String
  $category: String
) {
  sentimentTrends(
    period: $period
    filter: { source: $source, category: $category }
  ) {
    period
    data {
      date
      sentimentAvg
      sentimentStd
      articleCount
      sources {
        name
        value
      }
    }
    summary {
      overallSentiment
      trendDirection
      confidence
    }
  }
}
```

### Get Bias Distribution
```graphql
query GetBiasDistribution($period: TimePeriod!) {
  biasDistribution(period: $period) {
    period
    distribution {
      left {
        count
        percentage
        avgScore
      }
      center {
        count
        percentage
        avgScore
      }
      right {
        count
        percentage
        avgScore
      }
    }
    bySource {
      source
      distribution {
        left
        center
        right
      }
    }
  }
}
```

### Get Trending Topics
```graphql
query GetTrendingTopics($period: TimePeriod!, $limit: Int = 10) {
  trendingTopics(period: $period, limit: $limit) {
    period
    topics {
      topic
      score
      articleCount
      growthRate
      sentiment {
        avg
        distribution {
          positive
          neutral
          negative
        }
      }
      keyEntities
    }
  }
}
```

### Get Top Entities
```graphql
query GetTopEntities($period: TimePeriod!, $limit: Int = 10) {
  topEntities(period: $period, limit: $limit) {
    period
    entities {
      name
      type
      mentions
      avgSentiment
      sources
      trend
      relatedTopics
    }
  }
}
```

### Search Articles
```graphql
query SearchArticles($query: String!, $first: Int = 20) {
  searchArticles(query: $query, first: $first) {
    edges {
      node {
        id
        title
        content
        source
        publishedAt
        analysis {
          sentiment {
            score
            confidence
          }
          bias {
            score
            direction
          }
        }
      }
      score
      highlights {
        field
        fragments
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
```

## Mutations

### Analyze Article
```graphql
mutation AnalyzeArticle($input: AnalyzeArticleInput!) {
  analyzeArticle(input: $input) {
    success
    analysis {
      id
      sentiment {
        score
        confidence
        emotions
        explanation
      }
      bias {
        score
        direction
        confidence
        evidence
      }
      entities {
        name
        type
        confidence
        sentiment
      }
      topics {
        primary
        secondary
        confidence
      }
      summary
      confidence
      processedAt
    }
    errors {
      field
      message
    }
  }
}
```

**Input:**
```json
{
  "input": {
    "title": "Nuevas medidas económicas en Uruguay",
    "content": "El gobierno uruguayo anunció nuevas medidas...",
    "source": "El País",
    "url": "https://elpais.com.uy/article-123",
    "author": "Juan Pérez",
    "publishedAt": "2024-01-15T08:00:00Z",
    "tags": ["economía", "gobierno", "política"]
  }
}
```

### Batch Analyze Articles
```graphql
mutation BatchAnalyzeArticles($input: BatchAnalyzeInput!) {
  batchAnalyzeArticles(input: $input) {
    batchId
    results {
      articleIndex
      status
      analysis {
        id
        sentiment {
          score
          confidence
        }
        bias {
          score
          direction
        }
      }
      errors {
        field
        message
      }
    }
    summary {
      totalArticles
      successful
      failed
      processingTimeMs
    }
  }
}
```

### Update User Preferences
```graphql
mutation UpdateUserPreferences($input: UserPreferencesInput!) {
  updateUserPreferences(input: $input) {
    success
    user {
      id
      preferences {
        sources
        categories
        notifications
        language
      }
    }
    errors {
      field
      message
    }
  }
}
```

### Create Webhook
```graphql
mutation CreateWebhook($input: WebhookInput!) {
  createWebhook(input: $input) {
    success
    webhook {
      id
      url
      events
      isActive
      createdAt
    }
    errors {
      field
      message
    }
  }
}
```

## Subscriptions

### Real-time Analysis Updates
```graphql
subscription AnalysisUpdates($userId: ID!) {
  analysisUpdates(userId: $userId) {
    type
    timestamp
    data {
      ... on AnalysisCompleted {
        analysisId
        articleId
        sentimentScore
        biasDirection
        confidence
      }
      ... on AnalysisFailed {
        articleId
        error
      }
    }
  }
}
```

### Breaking News Alerts
```graphql
subscription BreakingNewsAlerts {
  breakingNewsAlerts {
    id
    title
    source
    publishedAt
    urgencyScore
    sentiment {
      score
      confidence
    }
    engagement {
      views
      shares
      comments
    }
  }
}
```

### Trending Topics Updates
```graphql
subscription TrendingTopicsUpdates($period: TimePeriod = HOUR_24) {
  trendingTopicsUpdates(period: $period) {
    timestamp
    topics {
      topic
      score
      articleCount
      growthRate
      sentiment {
        avg
        distribution {
          positive
          neutral
          negative
        }
      }
      keyEntities
    }
  }
}
```

### Sentiment Trends
```graphql
subscription SentimentTrendsUpdates($source: String) {
  sentimentTrendsUpdates(source: $source) {
    timestamp
    source
    currentSentiment
    change
    trend
    significantChange
  }
}
```

## Input Types

### AnalyzeArticleInput
```graphql
input AnalyzeArticleInput {
  title: String!
  content: String!
  source: String!
  url: String
  author: String
  publishedAt: DateTime
  tags: [String!]
  culturalContext: CulturalContextInput
}

input CulturalContextInput {
  region: String
  politicalContext: String
  sourceType: String
}
```

### BatchAnalyzeInput
```graphql
input BatchAnalyzeInput {
  articles: [AnalyzeArticleInput!]!
  priority: Priority = NORMAL
}

enum Priority {
  LOW
  NORMAL
  HIGH
  URGENT
}
```

### UserPreferencesInput
```graphql
input UserPreferencesInput {
  sources: [String!]
  categories: [String!]
  notifications: Boolean
  language: String
  alertThresholds: AlertThresholdsInput
}

input AlertThresholdsInput {
  sentimentChange: Float
  biasChange: Float
  urgencyScore: Float
}
```

### WebhookInput
```graphql
input WebhookInput {
  url: String!
  events: [WebhookEvent!]!
  secret: String
  isActive: Boolean = true
}

enum WebhookEvent {
  ANALYSIS_COMPLETED
  ANALYSIS_FAILED
  BREAKING_NEWS
  TRENDING_TOPIC_EMERGED
  SENTIMENT_THRESHOLD_EXCEEDED
}
```

## Enums

### TimePeriod
```graphql
enum TimePeriod {
  HOUR_1
  HOUR_6
  HOUR_12
  DAY_1
  DAY_7
  DAY_30
  DAY_90
}
```

### SortOrder
```graphql
enum SortOrder {
  ASC
  DESC
}
```

### ArticleSortField
```graphql
enum ArticleSortField {
  PUBLISHED_AT
  SENTIMENT_SCORE
  BIAS_SCORE
  CONFIDENCE
  WORD_COUNT
  RELEVANCE
}
```

## Error Handling

### Error Types
```graphql
type Error {
  field: String
  message: String!
  code: ErrorCode!
  details: String
}

enum ErrorCode {
  VALIDATION_ERROR
  AUTHENTICATION_REQUIRED
  AUTHORIZATION_FAILED
  RESOURCE_NOT_FOUND
  RATE_LIMIT_EXCEEDED
  ANALYSIS_FAILED
  INTERNAL_ERROR
  SERVICE_UNAVAILABLE
}
```

### Error Response Example
```json
{
  "errors": [
    {
      "message": "Article content is required",
      "locations": [{"line": 2, "column": 3}],
      "path": ["analyzeArticle"],
      "extensions": {
        "code": "VALIDATION_ERROR",
        "field": "content"
      }
    }
  ]
}
```

## Pagination

### Cursor-based Pagination
```graphql
type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type Connection {
  edges: [Edge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type Edge {
  node: Node!
  cursor: String!
}
```

### Usage Example
```graphql
query GetArticlesWithPagination($first: Int!, $after: String) {
  articles(first: $first, after: $after) {
    edges {
      node {
        id
        title
        publishedAt
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
```

## Real-time Features

### WebSocket Connection
```javascript
import { createClient } from 'graphql-ws';

const client = createClient({
  url: 'wss://api.uruguaynews.com/graphql',
  connectionParams: {
    authorization: `Bearer ${token}`,
  },
});

// Subscribe to breaking news
const unsubscribe = client.subscribe(
  {
    query: `
      subscription {
        breakingNewsAlerts {
          id
          title
          source
          urgencyScore
        }
      }
    `,
  },
  {
    next: (data) => {
      console.log('Breaking news:', data.breakingNewsAlerts);
    },
    error: (err) => {
      console.error('Subscription error:', err);
    },
    complete: () => {
      console.log('Subscription complete');
    },
  },
);
```

## Performance Considerations

### Query Complexity Limits
- Maximum query depth: 10 levels
- Maximum query complexity: 1000 points
- Rate limiting: 100 requests per minute

### Field Selection
Always select only the fields you need:
```graphql
# Good - specific fields
query GetArticles {
  articles(first: 10) {
    edges {
      node {
        id
        title
        publishedAt
        analysis {
          sentiment {
            score
            confidence
          }
        }
      }
    }
  }
}

# Avoid - unnecessary fields
query GetArticles {
  articles(first: 10) {
    edges {
      node {
        id
        title
        content  # Large field, avoid if not needed
        analysis {
          sentiment {
            score
            confidence
            explanation  # Large field, avoid if not needed
          }
        }
      }
    }
  }
}
```

### Caching
Use Apollo Client or similar for automatic caching:
```javascript
import { ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://api.uruguaynews.com/graphql',
  cache: new InMemoryCache(),
  defaultOptions: {
    watchQuery: {
      fetchPolicy: 'cache-and-network',
    },
  },
});
```

## Examples

### React Hook Example
```javascript
import { useQuery, useSubscription } from '@apollo/client';
import { GET_ARTICLES, BREAKING_NEWS_ALERTS } from './queries';

function ArticleList() {
  const { data, loading, error } = useQuery(GET_ARTICLES, {
    variables: { first: 20 },
  });

  const { data: breakingNews } = useSubscription(BREAKING_NEWS_ALERTS);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {breakingNews && (
        <div className="breaking-news">
          Breaking: {breakingNews.breakingNewsAlerts.title}
        </div>
      )}
      {data.articles.edges.map(({ node }) => (
        <ArticleCard key={node.id} article={node} />
      ))}
    </div>
  );
}
```

### Python Client Example
```python
from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport
import asyncio

# Create client
transport = WebsocketsTransport(
    url="wss://api.uruguaynews.com/graphql",
    headers={"Authorization": f"Bearer {token}"}
)
client = Client(transport=transport)

# Query
query = gql("""
    query GetArticles($first: Int!) {
        articles(first: $first) {
            edges {
                node {
                    id
                    title
                    analysis {
                        sentiment {
                            score
                            confidence
                        }
                    }
                }
            }
        }
    }
""")

# Execute query
result = client.execute(query, variable_values={"first": 10})
print(result)

# Subscription
subscription = gql("""
    subscription {
        breakingNewsAlerts {
            id
            title
            source
            urgencyScore
        }
    }
""")

async def handle_subscription():
    async for result in client.subscribe(subscription):
        print(f"Breaking news: {result['breakingNewsAlerts']}")

asyncio.run(handle_subscription())
```

## Schema Introspection

### Get Full Schema
```graphql
query IntrospectionQuery {
  __schema {
    types {
      name
      description
      fields {
        name
        type {
          name
          ofType {
            name
          }
        }
        description
      }
    }
  }
}
```

### Get Available Operations
```graphql
query GetOperations {
  __schema {
    queryType {
      fields {
        name
        description
        args {
          name
          type {
            name
          }
          description
        }
      }
    }
    mutationType {
      fields {
        name
        description
      }
    }
    subscriptionType {
      fields {
        name
        description
      }
    }
  }
}
```

## GraphQL Playground

Access the interactive GraphQL Playground:
- Production: https://api.uruguaynews.com/graphql
- Staging: https://api-staging.uruguaynews.com/graphql

The playground includes:
- Schema explorer
- Query builder
- Real-time documentation
- Subscription testing

## Next Steps

1. **Explore** the GraphQL schema using the playground
2. **Implement** client-side GraphQL integration
3. **Use** subscriptions for real-time features
4. **Optimize** queries for performance
5. **Monitor** query complexity and usage

For more information, see:
- [REST API](rest.md)
- [WebSocket API](websocket.md)
- [Architecture Overview](../architecture/overview.md)
- [Development Guidelines](../development/guidelines.md) 
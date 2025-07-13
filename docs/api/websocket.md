# WebSocket API Documentation

## Overview

The Uruguay News Analysis System provides real-time WebSocket connections for live updates on news analysis, breaking news alerts, and trending topics. This enables real-time dashboards and instant notifications.

## Connection Details

```
Production: wss://api.uruguaynews.com/ws
Staging: wss://api-staging.uruguaynews.com/ws
```

## Authentication

Include the bearer token in the connection parameters:
```javascript
const socket = new WebSocket('wss://api.uruguaynews.com/ws', {
  headers: {
    'Authorization': 'Bearer your-access-token'
  }
});
```

## Message Format

All messages follow a standardized JSON format:

```json
{
  "type": "message_type",
  "event": "event_name",
  "data": { /* event-specific data */ },
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "unique-message-id"
}
```

## Connection Events

### Connection Established
```json
{
  "type": "connection",
  "event": "connected",
  "data": {
    "userId": "user-123",
    "sessionId": "session-456",
    "capabilities": ["analysis_updates", "breaking_news", "trending_topics"]
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Connection Error
```json
{
  "type": "connection",
  "event": "error",
  "data": {
    "error": "authentication_failed",
    "message": "Invalid or expired token"
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Heartbeat
```json
{
  "type": "heartbeat",
  "event": "ping",
  "data": {},
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Subscription Management

### Subscribe to Events
```json
{
  "type": "subscribe",
  "event": "analysis_updates",
  "data": {
    "filters": {
      "sources": ["El País", "El Observador"],
      "categories": ["política", "economía"],
      "sentimentThreshold": 0.5
    }
  }
}
```

### Unsubscribe from Events
```json
{
  "type": "unsubscribe",
  "event": "analysis_updates",
  "data": {}
}
```

### Subscription Confirmation
```json
{
  "type": "subscription",
  "event": "subscribed",
  "data": {
    "eventType": "analysis_updates",
    "filters": {
      "sources": ["El País", "El Observador"],
      "categories": ["política", "economía"]
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Real-time Events

### Analysis Updates
Receive real-time updates when article analysis is completed:

```json
{
  "type": "analysis",
  "event": "analysis_completed",
  "data": {
    "analysisId": "analysis-456",
    "articleId": "article-123",
    "title": "Nuevas medidas económicas en Uruguay",
    "source": "El País",
    "publishedAt": "2024-01-15T08:00:00Z",
    "sentiment": {
      "score": 0.65,
      "confidence": 0.87,
      "emotions": ["positive", "hopeful"]
    },
    "bias": {
      "score": 0.15,
      "direction": "center",
      "confidence": 0.73
    },
    "entities": [
      {
        "name": "Uruguay",
        "type": "LOCATION",
        "sentiment": 0.7,
        "mentions": 3
      }
    ],
    "confidence": 0.84,
    "processingTime": 187
  },
  "timestamp": "2024-01-15T10:05:00Z"
}
```

### Breaking News Alerts
Receive instant notifications for breaking news:

```json
{
  "type": "breaking_news",
  "event": "breaking_news_alert",
  "data": {
    "id": "breaking-123",
    "title": "Importante anuncio gubernamental",
    "source": "El País",
    "publishedAt": "2024-01-15T14:30:00Z",
    "urgencyScore": 0.94,
    "sentiment": {
      "score": -0.23,
      "confidence": 0.87
    },
    "keyEntities": [
      {
        "name": "gobierno uruguayo",
        "type": "ORGANIZATION",
        "sentiment": -0.1
      }
    ],
    "engagement": {
      "views": 1500,
      "shares": 89,
      "comments": 23
    },
    "categories": ["política", "gobierno"]
  },
  "timestamp": "2024-01-15T14:30:00Z"
}
```

### Trending Topics Updates
Receive updates on trending topics:

```json
{
  "type": "trending",
  "event": "trending_topics_update",
  "data": {
    "period": "1h",
    "topics": [
      {
        "topic": "economía",
        "score": 0.89,
        "articleCount": 34,
        "growthRate": 0.23,
        "sentiment": {
          "avg": 0.45,
          "distribution": {
            "positive": 0.65,
            "neutral": 0.25,
            "negative": 0.10
          }
        },
        "keyEntities": ["gobierno", "medidas económicas", "Uruguay"],
        "sources": ["El País", "El Observador", "La Diaria"]
      }
    ]
  },
  "timestamp": "2024-01-15T15:00:00Z"
}
```

### Sentiment Trends
Real-time sentiment trend updates:

```json
{
  "type": "sentiment",
  "event": "sentiment_trend_update",
  "data": {
    "source": "El País",
    "category": "política",
    "currentSentiment": 0.32,
    "previousSentiment": 0.28,
    "change": 0.04,
    "changePercent": 14.3,
    "trend": "increasing",
    "significantChange": true,
    "timeWindow": "1h",
    "articleCount": 15
  },
  "timestamp": "2024-01-15T15:00:00Z"
}
```

### Bias Alerts
Notifications for significant bias changes:

```json
{
  "type": "bias",
  "event": "bias_alert",
  "data": {
    "source": "La Diaria",
    "category": "política",
    "currentBias": {
      "score": 0.45,
      "direction": "left"
    },
    "previousBias": {
      "score": 0.25,
      "direction": "center"
    },
    "change": 0.20,
    "threshold": 0.15,
    "timeWindow": "6h",
    "articleCount": 8,
    "triggerReason": "threshold_exceeded"
  },
  "timestamp": "2024-01-15T15:00:00Z"
}
```

## Client Implementation

### JavaScript/TypeScript
```typescript
class UruguayNewsWebSocket {
  private socket: WebSocket;
  private token: string;
  private eventHandlers: Map<string, Function[]> = new Map();
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;

  constructor(token: string, baseUrl: string = 'wss://api.uruguaynews.com/ws') {
    this.token = token;
    this.connect(baseUrl);
  }

  private connect(url: string) {
    this.socket = new WebSocket(url, {
      headers: {
        'Authorization': `Bearer ${this.token}`
      }
    });

    this.socket.onopen = this.onOpen.bind(this);
    this.socket.onmessage = this.onMessage.bind(this);
    this.socket.onclose = this.onClose.bind(this);
    this.socket.onerror = this.onError.bind(this);
  }

  private onOpen(event: Event) {
    console.log('WebSocket connected');
    this.reconnectAttempts = 0;
    this.emit('connected', { event });
  }

  private onMessage(event: MessageEvent) {
    try {
      const message = JSON.parse(event.data);
      this.handleMessage(message);
    } catch (error) {
      console.error('Error parsing message:', error);
    }
  }

  private onClose(event: CloseEvent) {
    console.log('WebSocket disconnected');
    this.emit('disconnected', { event });
    this.attemptReconnect();
  }

  private onError(error: Event) {
    console.error('WebSocket error:', error);
    this.emit('error', { error });
  }

  private handleMessage(message: any) {
    const { type, event, data } = message;
    
    switch (type) {
      case 'analysis':
        this.emit('analysis_update', data);
        break;
      case 'breaking_news':
        this.emit('breaking_news', data);
        break;
      case 'trending':
        this.emit('trending_update', data);
        break;
      case 'sentiment':
        this.emit('sentiment_update', data);
        break;
      case 'bias':
        this.emit('bias_alert', data);
        break;
      case 'heartbeat':
        this.handleHeartbeat();
        break;
      default:
        console.warn('Unknown message type:', type);
    }
  }

  private handleHeartbeat() {
    this.send({
      type: 'heartbeat',
      event: 'pong',
      data: {},
      timestamp: new Date().toISOString()
    });
  }

  private attemptReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      const delay = Math.pow(2, this.reconnectAttempts) * 1000; // Exponential backoff
      
      setTimeout(() => {
        console.log(`Attempting to reconnect... (${this.reconnectAttempts}/${this.maxReconnectAttempts})`);
        this.connect(this.socket.url);
      }, delay);
    }
  }

  public subscribe(eventType: string, filters?: any) {
    this.send({
      type: 'subscribe',
      event: eventType,
      data: { filters }
    });
  }

  public unsubscribe(eventType: string) {
    this.send({
      type: 'unsubscribe',
      event: eventType,
      data: {}
    });
  }

  public on(event: string, handler: Function) {
    if (!this.eventHandlers.has(event)) {
      this.eventHandlers.set(event, []);
    }
    this.eventHandlers.get(event)!.push(handler);
  }

  public off(event: string, handler: Function) {
    const handlers = this.eventHandlers.get(event);
    if (handlers) {
      const index = handlers.indexOf(handler);
      if (index > -1) {
        handlers.splice(index, 1);
      }
    }
  }

  private emit(event: string, data: any) {
    const handlers = this.eventHandlers.get(event);
    if (handlers) {
      handlers.forEach(handler => handler(data));
    }
  }

  private send(message: any) {
    if (this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(message));
    } else {
      console.warn('WebSocket is not open');
    }
  }

  public close() {
    this.socket.close();
  }
}

// Usage example
const wsClient = new UruguayNewsWebSocket('your-access-token');

// Subscribe to analysis updates
wsClient.subscribe('analysis_updates', {
  sources: ['El País', 'El Observador'],
  categories: ['política', 'economía']
});

// Handle events
wsClient.on('analysis_update', (data) => {
  console.log('New analysis:', data);
  updateDashboard(data);
});

wsClient.on('breaking_news', (data) => {
  console.log('Breaking news:', data);
  showBreakingNewsAlert(data);
});

wsClient.on('trending_update', (data) => {
  console.log('Trending topics updated:', data);
  updateTrendingTopics(data);
});
```

### Python Client
```python
import asyncio
import websockets
import json
from typing import Dict, List, Callable, Any

class UruguayNewsWebSocket:
    def __init__(self, token: str, base_url: str = "wss://api.uruguaynews.com/ws"):
        self.token = token
        self.base_url = base_url
        self.websocket = None
        self.event_handlers: Dict[str, List[Callable]] = {}
        self.is_connected = False
        
    async def connect(self):
        """Connect to WebSocket server"""
        try:
            self.websocket = await websockets.connect(
                self.base_url,
                extra_headers={'Authorization': f'Bearer {self.token}'}
            )
            self.is_connected = True
            print("WebSocket connected")
            
            # Start listening for messages
            await self.listen()
            
        except Exception as e:
            print(f"Connection error: {e}")
            self.is_connected = False
    
    async def listen(self):
        """Listen for incoming messages"""
        try:
            async for message in self.websocket:
                try:
                    data = json.loads(message)
                    await self.handle_message(data)
                except json.JSONDecodeError as e:
                    print(f"Error parsing message: {e}")
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")
            self.is_connected = False
    
    async def handle_message(self, message: Dict[str, Any]):
        """Handle incoming messages"""
        message_type = message.get('type')
        event = message.get('event')
        data = message.get('data', {})
        
        # Handle different message types
        if message_type == 'analysis':
            await self.emit('analysis_update', data)
        elif message_type == 'breaking_news':
            await self.emit('breaking_news', data)
        elif message_type == 'trending':
            await self.emit('trending_update', data)
        elif message_type == 'sentiment':
            await self.emit('sentiment_update', data)
        elif message_type == 'bias':
            await self.emit('bias_alert', data)
        elif message_type == 'heartbeat' and event == 'ping':
            await self.send_heartbeat()
        else:
            print(f"Unknown message type: {message_type}")
    
    async def send_heartbeat(self):
        """Send heartbeat response"""
        await self.send({
            'type': 'heartbeat',
            'event': 'pong',
            'data': {},
            'timestamp': asyncio.get_event_loop().time()
        })
    
    async def subscribe(self, event_type: str, filters: Dict[str, Any] = None):
        """Subscribe to specific event type"""
        await self.send({
            'type': 'subscribe',
            'event': event_type,
            'data': {'filters': filters or {}}
        })
    
    async def unsubscribe(self, event_type: str):
        """Unsubscribe from event type"""
        await self.send({
            'type': 'unsubscribe',
            'event': event_type,
            'data': {}
        })
    
    async def send(self, message: Dict[str, Any]):
        """Send message to server"""
        if self.websocket and self.is_connected:
            await self.websocket.send(json.dumps(message))
        else:
            print("WebSocket is not connected")
    
    def on(self, event: str, handler: Callable):
        """Register event handler"""
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(handler)
    
    def off(self, event: str, handler: Callable):
        """Unregister event handler"""
        if event in self.event_handlers:
            try:
                self.event_handlers[event].remove(handler)
            except ValueError:
                pass
    
    async def emit(self, event: str, data: Any):
        """Emit event to registered handlers"""
        if event in self.event_handlers:
            for handler in self.event_handlers[event]:
                if asyncio.iscoroutinefunction(handler):
                    await handler(data)
                else:
                    handler(data)
    
    async def close(self):
        """Close WebSocket connection"""
        if self.websocket:
            await self.websocket.close()
            self.is_connected = False

# Usage example
async def main():
    client = UruguayNewsWebSocket('your-access-token')
    
    # Register event handlers
    client.on('analysis_update', lambda data: print(f"New analysis: {data}"))
    client.on('breaking_news', lambda data: print(f"Breaking news: {data}"))
    client.on('trending_update', lambda data: print(f"Trending topics: {data}"))
    
    # Connect and subscribe
    await client.connect()
    await client.subscribe('analysis_updates', {
        'sources': ['El País', 'El Observador'],
        'categories': ['política', 'economía']
    })
    
    # Keep connection alive
    try:
        while client.is_connected:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Rate Limiting and Throttling

### Connection Limits
- Maximum 5 concurrent connections per user
- Maximum 100 messages per minute per connection
- Maximum 10 subscriptions per connection

### Message Throttling
Some event types are throttled to prevent overwhelming clients:

```json
{
  "type": "throttle",
  "event": "rate_limit_warning",
  "data": {
    "messageType": "sentiment_update",
    "currentRate": 95,
    "limit": 100,
    "resetTime": "2024-01-15T15:01:00Z"
  }
}
```

## Error Handling

### Connection Errors
```json
{
  "type": "error",
  "event": "connection_error",
  "data": {
    "code": "AUTHENTICATION_FAILED",
    "message": "Invalid or expired token",
    "canReconnect": false
  }
}
```

### Subscription Errors
```json
{
  "type": "error",
  "event": "subscription_error",
  "data": {
    "code": "INVALID_FILTER",
    "message": "Invalid source filter",
    "eventType": "analysis_updates",
    "field": "sources"
  }
}
```

## Health Monitoring

### Connection Health
```json
{
  "type": "health",
  "event": "connection_health",
  "data": {
    "status": "healthy",
    "latency": 45,
    "messagesReceived": 123,
    "messagesSent": 45,
    "uptime": 3600,
    "subscriptions": ["analysis_updates", "breaking_news"]
  }
}
```

## React Integration Example

```typescript
import { useEffect, useState } from 'react';
import { UruguayNewsWebSocket } from './websocket-client';

interface AnalysisUpdate {
  analysisId: string;
  articleId: string;
  title: string;
  sentiment: {
    score: number;
    confidence: number;
  };
  bias: {
    score: number;
    direction: string;
  };
}

export function useWebSocketAnalysis(token: string) {
  const [wsClient, setWsClient] = useState<UruguayNewsWebSocket | null>(null);
  const [analysisUpdates, setAnalysisUpdates] = useState<AnalysisUpdate[]>([]);
  const [breakingNews, setBreakingNews] = useState<any[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const client = new UruguayNewsWebSocket(token);
    
    client.on('connected', () => {
      setIsConnected(true);
      // Subscribe to events
      client.subscribe('analysis_updates', {
        sources: ['El País', 'El Observador'],
        categories: ['política', 'economía']
      });
      client.subscribe('breaking_news');
    });

    client.on('disconnected', () => {
      setIsConnected(false);
    });

    client.on('analysis_update', (data: AnalysisUpdate) => {
      setAnalysisUpdates(prev => [data, ...prev.slice(0, 49)]); // Keep last 50
    });

    client.on('breaking_news', (data: any) => {
      setBreakingNews(prev => [data, ...prev.slice(0, 9)]); // Keep last 10
    });

    setWsClient(client);

    return () => {
      client.close();
    };
  }, [token]);

  return {
    wsClient,
    analysisUpdates,
    breakingNews,
    isConnected
  };
}

// Usage in component
function Dashboard() {
  const { analysisUpdates, breakingNews, isConnected } = useWebSocketAnalysis(token);

  return (
    <div>
      <div className="connection-status">
        {isConnected ? '🟢 Connected' : '🔴 Disconnected'}
      </div>
      
      <div className="breaking-news">
        <h2>Breaking News</h2>
        {breakingNews.map(news => (
          <div key={news.id} className="news-item">
            <h3>{news.title}</h3>
            <p>Source: {news.source}</p>
            <p>Urgency: {news.urgencyScore}</p>
          </div>
        ))}
      </div>
      
      <div className="analysis-updates">
        <h2>Recent Analysis</h2>
        {analysisUpdates.map(update => (
          <div key={update.analysisId} className="analysis-item">
            <h3>{update.title}</h3>
            <p>Sentiment: {update.sentiment.score.toFixed(2)}</p>
            <p>Bias: {update.bias.direction}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## Security Considerations

### Authentication
- Bearer token authentication required
- Token validation on every connection
- Automatic disconnection on token expiry

### Rate Limiting
- Per-user connection limits
- Message rate limiting
- Subscription limits

### Data Privacy
- User-specific data filtering
- No cross-user data leakage
- Audit logging of all connections

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check token validity
   - Verify network connectivity
   - Ensure WebSocket support

2. **Missing Events**
   - Verify subscription filters
   - Check rate limiting
   - Ensure proper event handling

3. **High Latency**
   - Check network conditions
   - Verify server load
   - Consider connection pooling

### Debug Mode
Enable debug mode for detailed logging:

```javascript
const wsClient = new UruguayNewsWebSocket(token, {
  debug: true,
  logLevel: 'verbose'
});
```

## Next Steps

1. **Implement** WebSocket client for your platform
2. **Subscribe** to relevant event types
3. **Handle** real-time updates in your UI
4. **Monitor** connection health and performance
5. **Implement** proper error handling and reconnection

For more information, see:
- [REST API](rest.md)
- [GraphQL API](graphql.md)
- [Architecture Overview](../architecture/overview.md)
- [Real-time Architecture](../architecture/overview.md) 
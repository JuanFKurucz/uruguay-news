# Uruguay News Monitoring & Analysis System - Technical Implementation

## System Architecture Overview

This document outlines the technical implementation for a modern, scalable news monitoring and analysis system. The architecture leverages contemporary technologies including FastAPI, LangChain/LangGraph, NoSQL databases, and serverless deployment patterns to create a robust, maintainable, and scalable solution.

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Frontend Applications                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Web Dashboard (React)  │  Mobile App (React Native)  │  Admin Panel (Next.js)    │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            API Gateway & Load Balancer                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                    CloudFlare / AWS ALB / Google Cloud Load Balancer               │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Core Application Services                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  FastAPI Backend  │  WebSocket Service  │  Auth Service  │  Analytics Service      │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        AI & Processing Pipeline                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  LangGraph Agents  │  Content Analyzer  │  Fact Checker  │  Trend Detector        │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         Data Collection Layer                                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  News Scrapers  │  Social Media APIs  │  RSS Feeds  │  Webhook Receivers           │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            Storage & Caching                                        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  MongoDB/DynamoDB  │  Redis Cache  │  Vector DB  │  S3/GCS Storage  │  Elasticsearch│
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### Detailed Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                               Data Ingestion Flow                                   │
└─────────────────────────────────────────────────────────────────────────────────────┘

RSS Feeds ──┐
            │
Web Scrapers──┼────► Raw Data    ────► Deduplication ────► Content Cleaning
            │        Queue              Engine              Pipeline
Social APIs ──┘        │                   │                    │
                       ▼                   ▼                    ▼
                   MongoDB              Redis Cache         Text Processing
                   (Raw Data)           (Temp Storage)      (Boilerplate Removal)
                                                                │
                                                                ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                               AI Analysis Pipeline                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Content ────► Topic          ────► Sentiment      ────► Bias Detection            │
│  Input        Classification        Analysis              Engine                    │
│               (Politics,            (Positive/              (Left/Center/Right)    │
│               Economy, etc.)         Negative/Neutral)                             │
│                  │                     │                      │                    │
│                  ▼                     ▼                      ▼                    │
│              Entity          ────► Fact Checking   ────► Credibility              │
│              Extraction            Pipeline               Scoring                   │
│              (NER)                 (UyCheck API)         (Source Rating)           │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              Data Storage & Indexing                               │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  MongoDB            │  Vector DB           │  ClickHouse         │  Elasticsearch   │
│  (Structured Data)  │  (Semantic Search)   │  (Analytics)        │  (Full-text)     │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                Dashboard & API                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  FastAPI Endpoints  │  WebSocket Updates  │  Real-time Analytics │  Export Services │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Backend Services

**Primary Framework**: FastAPI
- **Rationale**: High performance, automatic OpenAPI documentation, async support
- **Features**: Built-in validation, dependency injection, WebSocket support
- **Deployment**: Containerized with Docker, deployed on AWS Lambda/Google Cloud Functions

**Database Architecture**:
- **Primary Database**: MongoDB (document-based for flexible schema) - Free tier or self-hosted
- **Vector Database**: Weaviate (open-source) or Chroma for semantic search
- **Cache Layer**: Redis for session management and real-time data
- **Analytics Database**: PostgreSQL with TimescaleDB for time-series analytics (open-source alternative)
- **Search Engine**: Elasticsearch (open-source) or OpenSearch for full-text search

**AI & Machine Learning**:
- **LangChain**: Framework for building applications with LLMs
- **LangGraph**: Multi-agent workflows for complex analysis tasks
- **OpenAI GPT models**: Cost-effective models for content analysis (with budget limits)
- **Open-source alternatives**: Ollama for local LLM deployment when needed
- **Vector Embeddings**: OpenAI embeddings or open-source alternatives like sentence-transformers

### Frontend Applications

**Web Dashboard**: React 18 + TypeScript
- **State Management**: Zustand for lightweight state management
- **UI Components**: Shadcn/ui with Tailwind CSS
- **Charts**: Recharts for data visualization
- **Real-time Updates**: WebSocket connections for live data

**Mobile Application**: React Native
- **Navigation**: React Navigation 6
- **State Management**: React Query for server state
- **Push Notifications**: Firebase Cloud Messaging
- **Offline Support**: Redux Persist for offline capabilities

**Admin Panel**: Next.js 14 with App Router
- **Authentication**: Auth0 for secure admin access
- **Data Tables**: TanStack Table for complex data management
- **Forms**: React Hook Form with Zod validation

### Infrastructure & DevOps

**Package Management**: UV (Ultra-fast Python package manager)
- **Benefits**: 10-100x faster than pip, built-in virtual environment management
- **Configuration**: pyproject.toml for modern Python project structure

**Code Quality**:
- **Linting**: Ruff for ultra-fast Python linting
- **Type Checking**: mypy for static type analysis
- **Formatting**: Ruff formatter for consistent code style
- **Pre-commit Hooks**: Automated code quality checks

**Deployment**:
- **Containerization**: Docker with multi-stage builds
- **Simple Deployment**: Docker Compose for development and small-scale production
- **Cloud Options**: Cost-effective cloud services or self-hosted options
- **Infrastructure as Code**: Terraform for reproducible deployments (optional)

**Monitoring & Observability**:
- **APM**: Open-source alternatives like Grafana APM or simple logging
- **Logging**: Basic structured logging with optional ELK Stack for larger deployments
- **Metrics**: Prometheus + Grafana for system metrics (open-source)
- **Tracing**: OpenTelemetry for distributed tracing (optional for complex deployments)

## Comprehensive Data Collection Architecture

### Advanced News Scraping Framework

**Multi-Source Async Scraping System**:

```python
import asyncio
import aiohttp
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import uvloop
from urllib.robotparser import RobotFileParser
import time
from pathlib import Path
import json

@dataclass
class ScrapingConfig:
    name: str
    base_url: str
    selectors: Dict[str, str]
    rate_limit: float
    headers: Dict[str, str]
    cookies: Optional[Dict[str, str]] = None
    robots_txt_url: Optional[str] = None
    user_agent: str = "UruguayNewsBot/1.0 (contact@uruguaynews.com)"
    max_retries: int = 3
    timeout: int = 30
    use_proxy: bool = False
    proxy_pool: Optional[List[str]] = None

class AsyncNewsScraper:
    def __init__(self, config: ScrapingConfig):
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        self.robots_parser = None
        self.request_times = []
        
    async def __aenter__(self):
        # Check robots.txt compliance
        if self.config.robots_txt_url:
            self.robots_parser = RobotFileParser()
            self.robots_parser.set_url(self.config.robots_txt_url)
            self.robots_parser.read()
            
        # Create session with optimized connector
        connector = aiohttp.TCPConnector(
            limit=100,
            ttl_dns_cache=300,
            use_dns_cache=True,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        
        self.session = aiohttp.ClientSession(
            connector=connector,
            headers=self.config.headers,
            cookies=self.config.cookies,
            timeout=aiohttp.ClientTimeout(total=self.config.timeout),
            trust_env=True
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def scrape_articles(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Scrape multiple articles concurrently with rate limiting"""
        tasks = []
        for url in urls:
            if self.can_fetch(url):
                task = self._scrape_single_article(url)
                tasks.append(task)
                
                # Rate limiting
                await asyncio.sleep(self.config.rate_limit)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return [r for r in results if isinstance(r, dict)]
    
    async def _scrape_single_article(self, url: str) -> Dict[str, Any]:
        """Scrape a single article with retry logic"""
        for attempt in range(self.config.max_retries):
            try:
                async with self.session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        return self._extract_article_data(html, url)
                    elif response.status == 429:  # Rate limited
                        await asyncio.sleep(60)  # Wait 1 minute
                    else:
                        raise aiohttp.ClientError(f"HTTP {response.status}")
            except Exception as e:
                if attempt == self.config.max_retries - 1:
                    return {"error": str(e), "url": url}
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
    
    def can_fetch(self, url: str) -> bool:
        """Check if URL can be fetched according to robots.txt"""
        if self.robots_parser:
            return self.robots_parser.can_fetch(self.config.user_agent, url)
        return True
    
    def _extract_article_data(self, html: str, url: str) -> Dict[str, Any]:
        """Extract article data using configured selectors"""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        data = {
            'source': self.config.name,
            'url': url,
            'scraped_at': time.time(),
            'content_hash': None
        }
        
        # Extract data using configured selectors
        for field, selector in self.config.selectors.items():
            try:
                element = soup.select_one(selector)
                if element:
                    data[field] = element.get_text(strip=True)
                else:
                    data[field] = None
            except Exception as e:
                data[field] = None
                data[f'{field}_error'] = str(e)
        
        # Generate content hash for deduplication
        content_text = data.get('content', '') + data.get('title', '')
        if content_text:
            import hashlib
            data['content_hash'] = hashlib.md5(content_text.encode()).hexdigest()
        
        return data
```

**Comprehensive Source Configurations**:

```python
# Uruguayan News Sources Configuration
URUGUAYAN_SOURCES = {
    "el_pais": ScrapingConfig(
        name="El País",
        base_url="https://www.elpais.com.uy",
        selectors={
            "title": "h1.title, h1.entry-title, h1.post-title",
            "content": "div.entry-content p, div.content-body p, div.article-content p",
            "author": "span.author-name, div.author-info, span.by-author",
            "date": "time.entry-date, time.published-date, span.post-date",
            "category": "span.category, div.category-info, a.category-link",
            "tags": "div.tags a, span.tag-list a"
        },
        rate_limit=2.0,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        robots_txt_url="https://www.elpais.com.uy/robots.txt"
    ),
    
    "montevideo_portal": ScrapingConfig(
        name="Montevideo Portal",
        base_url="https://www.montevideo.com.uy",
        selectors={
            "title": "h1.title, h1.news-title, h1.post-title",
            "content": "div.content-body p, div.news-content p, div.article-text p",
            "author": "div.author, span.author-name, div.news-author",
            "date": "time.publish-date, span.date, time.news-date",
            "category": "span.section, div.category, a.section-link",
            "tags": "div.tags a, span.keywords a"
        },
        rate_limit=1.5,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8",
            "Referer": "https://www.montevideo.com.uy/"
        },
        robots_txt_url="https://www.montevideo.com.uy/robots.txt"
    ),
    
    "teledoce": ScrapingConfig(
        name="Teledoce",
        base_url="https://www.teledoce.com",
        selectors={
            "title": "h1.article-title, h1.news-title, h1.post-title",
            "content": "div.article-body p, div.content-text p, div.news-content p",
            "author": "span.author, div.author-info, span.journalist",
            "date": "time.article-date, span.publish-date, time.news-time",
            "category": "span.category, div.section, a.category-tag",
            "tags": "div.article-tags a, span.tags a"
        },
        rate_limit=2.0,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8"
        },
        robots_txt_url="https://www.teledoce.com/robots.txt"
    ),
    
    "la_diaria": ScrapingConfig(
        name="La Diaria",
        base_url="https://ladiaria.com.uy",
        selectors={
            "title": "h1.article-title, h1.post-title",
            "content": "div.article-content p, div.entry-content p",
            "author": "span.author-name, div.author-info",
            "date": "time.article-date, span.publish-date",
            "category": "span.category, div.section-name",
            "tags": "div.tags a, span.article-tags a"
        },
        rate_limit=3.0,  # Respectful rate limiting for subscription site
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8"
        },
        robots_txt_url="https://ladiaria.com.uy/robots.txt"
    ),
    
    "subrayado": ScrapingConfig(
        name="Subrayado",
        base_url="https://www.subrayado.com.uy",
        selectors={
            "title": "h1.news-title, h1.article-title, h1.post-title",
            "content": "div.news-content p, div.article-body p, div.content-text p",
            "author": "span.author, div.journalist-info, span.reporter",
            "date": "time.news-date, span.publish-time, time.article-time",
            "category": "span.section, div.category-info, a.section-link",
            "tags": "div.news-tags a, span.keywords a"
        },
        rate_limit=1.8,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8"
        },
        robots_txt_url="https://www.subrayado.com.uy/robots.txt"
    ),
    
    "el_observador": ScrapingConfig(
        name="El Observador",
        base_url="https://www.elobservador.com.uy",
        selectors={
            "title": "h1.article-title, h1.news-title, h1.entry-title",
            "content": "div.article-content p, div.news-body p, div.entry-content p",
            "author": "span.author-name, div.author-info, span.journalist",
            "date": "time.article-date, span.publish-date, time.entry-date",
            "category": "span.category, div.section-name, a.category-link",
            "tags": "div.article-tags a, span.tags a"
        },
        rate_limit=2.0,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-UY,es;q=0.9,en;q=0.8"
        },
        robots_txt_url="https://www.elobservador.com.uy/robots.txt"
    )
}
```

### Advanced Social Media Integration

**Comprehensive Twitter/X Data Collection**:

```python
import tweepy
from typing import AsyncGenerator, List, Dict, Any
import asyncio
import json
from datetime import datetime, timedelta
import snscrape.modules.twitter as sntwitter

class TwitterDataCollector:
    def __init__(self, bearer_token: str, use_snscrape: bool = True):
        self.bearer_token = bearer_token
        self.use_snscrape = use_snscrape
        if not use_snscrape and bearer_token:
            self.client = tweepy.Client(bearer_token=bearer_token)
        
        # Key Uruguayan accounts to monitor
        self.key_accounts = [
            "LuisLacallePou",     # President
            "MariodelgadoUy",     # Government
            "Frente_Amplio",      # Opposition
            "UyPress",            # News agency
            "OPetinatti",         # Popular commentator
            "igalvar71",          # Ignacio Álvarez
            "EmilianoCotelo",     # Radio host
            "claudioromano",      # Political commentator
            "montevideocomuy",    # Montevideo Portal
            "elpaisuy",           # El País
            "teledoceuy",         # Teledoce
            "subrayado",          # Subrayado
            "ladiaria",           # La Diaria
        ]
        
        # Key hashtags to monitor
        self.key_hashtags = [
            "#Uruguay", "#Política", "#Economía", "#Lacalle", "#FrenteAmplio",
            "#Elecciones2024", "#CoaliciónMulticolor", "#TuVoto",
            "#Montevideo", "#ParlamentoUy", "#Senado", "#Diputados",
            "#Referendum", "#Plebiscito", "#Gobierno", "#Oposición"
        ]
    
    async def collect_account_tweets(self, 
                                   accounts: List[str], 
                                   since_hours: int = 24,
                                   max_tweets: int = 100) -> AsyncGenerator[Dict[str, Any], None]:
        """Collect tweets from specific accounts"""
        
        if self.use_snscrape:
            # Use snscrape for more reliable data collection
            since_date = (datetime.now() - timedelta(hours=since_hours)).strftime("%Y-%m-%d")
            
            for account in accounts:
                try:
                    query = f"from:{account} since:{since_date}"
                    tweets = sntwitter.TwitterSearchScraper(query).get_items()
                    
                    count = 0
                    for tweet in tweets:
                        if count >= max_tweets:
                            break
                            
                        yield {
                            'id': tweet.id,
                            'source': 'twitter',
                            'source_type': 'social_media',
                            'url': tweet.url,
                            'title': None,
                            'author': tweet.user.username,
                            'published_at': tweet.date.isoformat(),
                            'content': tweet.content,
                            'tags': self._extract_hashtags(tweet.content),
                            'engagement': {
                                'retweets': tweet.retweetCount,
                                'likes': tweet.likeCount,
                                'replies': tweet.replyCount,
                                'quotes': tweet.quoteCount
                            },
                            'entities': [],
                            'sentiment': None,
                            'ideology': None,
                            'reliability_score': self._get_account_reliability(account),
                            'content_type': 'tweet',
                            'language': 'es'
                        }
                        count += 1
                        
                except Exception as e:
                    print(f"Error collecting tweets from {account}: {e}")
                    continue
                    
        else:
            # Use official Twitter API
            for account in accounts:
                try:
                    tweets = tweepy.Paginator(
                        self.client.get_users_tweets,
                        username=account,
                        max_results=min(max_tweets, 100),
                        tweet_fields=['created_at', 'context_annotations', 'public_metrics', 'lang'],
                        expansions=['author_id']
                    ).flatten(limit=max_tweets)
                    
                    for tweet in tweets:
                        if tweet.lang == 'es':  # Spanish tweets only
                            yield {
                                'id': tweet.id,
                                'source': 'twitter',
                                'source_type': 'social_media',
                                'url': f'https://twitter.com/{account}/status/{tweet.id}',
                                'title': None,
                                'author': account,
                                'published_at': tweet.created_at.isoformat(),
                                'content': tweet.text,
                                'tags': self._extract_hashtags(tweet.text),
                                'engagement': tweet.public_metrics,
                                'entities': [],
                                'sentiment': None,
                                'ideology': None,
                                'reliability_score': self._get_account_reliability(account),
                                'content_type': 'tweet',
                                'language': 'es'
                            }
                except Exception as e:
                    print(f"Error collecting tweets from {account}: {e}")
                    continue
    
    async def collect_hashtag_tweets(self, 
                                   hashtags: List[str], 
                                   since_hours: int = 24,
                                   max_tweets: int = 50) -> AsyncGenerator[Dict[str, Any], None]:
        """Collect tweets by hashtag"""
        
        since_date = (datetime.now() - timedelta(hours=since_hours)).strftime("%Y-%m-%d")
        
        for hashtag in hashtags:
            try:
                query = f"{hashtag} lang:es since:{since_date}"
                tweets = sntwitter.TwitterSearchScraper(query).get_items()
                
                count = 0
                for tweet in tweets:
                    if count >= max_tweets:
                        break
                        
                    # Filter out retweets to get original content
                    if not tweet.content.startswith('RT @'):
                        yield {
                            'id': tweet.id,
                            'source': 'twitter',
                            'source_type': 'social_media',
                            'url': tweet.url,
                            'title': None,
                            'author': tweet.user.username,
                            'published_at': tweet.date.isoformat(),
                            'content': tweet.content,
                            'tags': self._extract_hashtags(tweet.content),
                            'engagement': {
                                'retweets': tweet.retweetCount,
                                'likes': tweet.likeCount,
                                'replies': tweet.replyCount,
                                'quotes': tweet.quoteCount
                            },
                            'entities': [],
                            'sentiment': None,
                            'ideology': None,
                            'reliability_score': self._get_tweet_reliability(tweet),
                            'content_type': 'tweet',
                            'language': 'es'
                        }
                        count += 1
                        
            except Exception as e:
                print(f"Error collecting tweets for hashtag {hashtag}: {e}")
                continue
    
    def _extract_hashtags(self, text: str) -> List[str]:
        """Extract hashtags from tweet text"""
        import re
        hashtags = re.findall(r'#\w+', text)
        return [tag.lower() for tag in hashtags]
    
    def _get_account_reliability(self, account: str) -> str:
        """Get reliability score for known accounts"""
        high_reliability = [
            "LuisLacallePou", "MariodelgadoUy", "Frente_Amplio", "UyPress",
            "montevideocomuy", "elpaisuy", "teledoceuy", "subrayado", "ladiaria"
        ]
        
        medium_reliability = [
            "OPetinatti", "igalvar71", "EmilianoCotelo", "claudioromano"
        ]
        
        if account in high_reliability:
            return "high"
        elif account in medium_reliability:
            return "medium"
        else:
            return "low"
    
    def _get_tweet_reliability(self, tweet) -> str:
        """Assess tweet reliability based on author and content"""
        # Check if from verified account or known reliable source
        if hasattr(tweet.user, 'verified') and tweet.user.verified:
            return "medium"
        
        # Check follower count as proxy for influence
        if hasattr(tweet.user, 'followersCount'):
            if tweet.user.followersCount > 10000:
                return "medium"
            elif tweet.user.followersCount > 1000:
                return "low"
        
        return "very_low"
```

**Facebook Integration**:

```python
import facebook
from typing import AsyncGenerator, Dict, Any, List
import asyncio
import requests
import json

class FacebookDataCollector:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.graph = facebook.GraphAPI(access_token=access_token)
        
        # Key Facebook pages to monitor
        self.key_pages = [
            "elpaisuy",           # El País Uruguay
            "montevideocomuy",    # Montevideo Portal
            "teledoceuy",         # Teledoce
            "subrayado",          # Subrayado
            "ladiaria",           # La Diaria
            "presidenciauruguay", # Presidencia
            "frenteamplio",       # Frente Amplio
            "partidonacional",    # Partido Nacional
            "partidocolorado",    # Partido Colorado
        ]
    
    async def collect_page_posts(self, 
                               pages: List[str], 
                               since_hours: int = 24,
                               max_posts: int = 50) -> AsyncGenerator[Dict[str, Any], None]:
        """Collect posts from Facebook pages"""
        
        for page in pages:
            try:
                # Get page posts
                posts = self.graph.get_connections(
                    page, 
                    "posts",
                    limit=max_posts,
                    fields="id,message,created_time,link,type,story,shares,reactions.summary(total_count),comments.summary(total_count)"
                )
                
                for post in posts['data']:
                    # Only process posts with text content
                    if post.get('message') or post.get('story'):
                        content = post.get('message', post.get('story', ''))
                        
                        yield {
                            'id': post['id'],
                            'source': 'facebook',
                            'source_type': 'social_media',
                            'url': f"https://facebook.com/{post['id']}",
                            'title': None,
                            'author': page,
                            'published_at': post['created_time'],
                            'content': content,
                            'tags': self._extract_hashtags(content),
                            'engagement': {
                                'reactions': post.get('reactions', {}).get('summary', {}).get('total_count', 0),
                                'comments': post.get('comments', {}).get('summary', {}).get('total_count', 0),
                                'shares': post.get('shares', {}).get('count', 0)
                            },
                            'entities': [],
                            'sentiment': None,
                            'ideology': None,
                            'reliability_score': self._get_page_reliability(page),
                            'content_type': 'facebook_post',
                            'language': 'es'
                        }
                        
            except Exception as e:
                print(f"Error collecting Facebook posts from {page}: {e}")
                continue
    
    def _extract_hashtags(self, text: str) -> List[str]:
        """Extract hashtags from Facebook post text"""
        import re
        hashtags = re.findall(r'#\w+', text)
        return [tag.lower() for tag in hashtags]
    
    def _get_page_reliability(self, page: str) -> str:
        """Get reliability score for Facebook pages"""
        high_reliability = [
            "elpaisuy", "montevideocomuy", "teledoceuy", "subrayado", "ladiaria",
            "presidenciauruguay"
        ]
        
        medium_reliability = [
            "frenteamplio", "partidonacional", "partidocolorado"
        ]
        
        if page in high_reliability:
            return "high"
        elif page in medium_reliability:
            return "medium"
        else:
            return "low"
```

**Reddit Integration**:

```python
import praw
from typing import AsyncGenerator, Dict, Any
import asyncio

class RedditDataCollector:
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        # Key subreddits to monitor
        self.key_subreddits = [
            "uruguay",
            "Montevideo",
            "CharruaDevs",  # Uruguay tech community
            "burises",      # Uruguay general discussion
        ]
    
    async def collect_subreddit_posts(self, 
                                    subreddits: List[str], 
                                    max_posts: int = 50) -> AsyncGenerator[Dict[str, Any], None]:
        """Collect posts from subreddits"""
        
        for subreddit_name in subreddits:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                
                # Get hot posts
                for post in subreddit.hot(limit=max_posts):
                    # Only process posts with text content
                    if post.selftext or post.title:
                        content = f"{post.title}\n\n{post.selftext}" if post.selftext else post.title
                        
                        yield {
                            'id': post.id,
                            'source': 'reddit',
                            'source_type': 'social_media',
                            'url': f"https://reddit.com{post.permalink}",
                            'title': post.title,
                            'author': str(post.author) if post.author else "[deleted]",
                            'published_at': post.created_utc,
                            'content': content,
                            'tags': [f"r/{subreddit_name}"] + self._extract_hashtags(content),
                            'engagement': {
                                'score': post.score,
                                'upvotes': post.ups,
                                'downvotes': post.downs,
                                'comments': post.num_comments
                            },
                            'entities': [],
                            'sentiment': None,
                            'ideology': None,
                            'reliability_score': 'low',  # Reddit posts are generally low reliability
                            'content_type': 'reddit_post',
                            'language': 'es'
                        }
                        
            except Exception as e:
                print(f"Error collecting Reddit posts from r/{subreddit_name}: {e}")
                continue
    
    def _extract_hashtags(self, text: str) -> List[str]:
        """Extract hashtags from Reddit post text"""
        import re
        hashtags = re.findall(r'#\w+', text)
        return [tag.lower() for tag in hashtags]
```

## Advanced AI Analysis Pipeline

### Comprehensive OpenAI Prompt Engineering

**Topic Classification Prompts**:

```python
# Topic Classification Prompts
TOPIC_CLASSIFICATION_PROMPTS = {
    "spanish_primary": {
        "system_prompt": """
Eres un experto analista de medios uruguayos especializado en categorización de noticias.
Tu tarea es clasificar artículos y contenido de redes sociales en las siguientes categorías:

CATEGORÍAS PRINCIPALES:
1. Política - Gobierno, partidos políticos, elecciones, políticas públicas
2. Economía - Finanzas, comercio, inflación, empleo, mercados
3. Sociedad - Educación, salud, derechos humanos, problemas sociales
4. Seguridad - Crimen, policía, justicia, narcotráfico
5. Internacional - Relaciones exteriores, Mercosur, comercio internacional
6. Deportes - Fútbol, olimpiadas, deportes uruguayos
7. Cultura - Arte, música, literatura, espectáculos
8. Tecnología - Innovación, internet, ciencia
9. Medio Ambiente - Cambio climático, conservación, sostenibilidad
10. Salud - Medicina, pandemias, sistema de salud

INSTRUCCIONES:
- Analiza el título y contenido completo
- Considera el contexto uruguayo
- Si un artículo cubre múltiples temas, elige el más prominente
- Responde SOLO con el nombre de la categoría
- Si no encaja en ninguna categoría, responde "General"
        """,
        
        "user_prompt": """
Clasifica el siguiente contenido de noticia:

TÍTULO: {title}
CONTENIDO: {content}
FUENTE: {source}

Categoría:
        """
    },
    
    "multi_shot_examples": {
        "system_prompt": """
Eres un experto analista de medios uruguayos. Clasifica el siguiente contenido en una de estas categorías:
Política, Economía, Sociedad, Seguridad, Internacional, Deportes, Cultura, Tecnología, Medio Ambiente, Salud, General

EJEMPLOS:

Título: "Lacalle Pou anuncia nuevas medidas económicas para el segundo semestre"
Contenido: "El presidente Luis Lacalle Pou anunció ayer un paquete de medidas económicas..."
Categoría: Economía

Título: "Peñarol vence a Nacional en el clásico del Centenario"
Contenido: "En un partido disputado en el Estadio Centenario, Peñarol derrotó 2-1 a Nacional..."
Categoría: Deportes

Título: "Aumentan los casos de COVID-19 en Montevideo"
Contenido: "El Ministerio de Salud Pública reportó un incremento del 15% en los casos..."
Categoría: Salud

Título: "Frente Amplio presenta propuesta para referendum sobre seguridad social"
Contenido: "La coalición de izquierda presentó formalmente la propuesta para un plebiscito..."
Categoría: Política
        """,
        
        "user_prompt": """
Título: {title}
Contenido: {content}
Categoría:
        """
    }
}

# Sentiment Analysis Prompts
SENTIMENT_ANALYSIS_PROMPTS = {
    "spanish_detailed": {
        "system_prompt": """
Eres un experto analista de sentimientos para contenido en español rioplatense (Uruguay/Argentina).
Tu tarea es analizar el tono emocional y la actitud del contenido.

CATEGORÍAS DE SENTIMIENTO:
1. Positivo - Optimismo, esperanza, satisfacción, alegría
2. Negativo - Pesimismo, crítica, preocupación, enojo
3. Neutro - Informativo, objetivo, sin carga emocional aparente
4. Mixto - Contiene elementos positivos y negativos equilibrados

CONSIDERACIONES ESPECIALES:
- Considera el contexto cultural uruguayo
- Analiza tanto el contenido como el tono del autor
- Diferencia entre reportar eventos negativos (neutral) vs. expresar negatividad (negativo)
- Considera ironía y sarcasmo característicos del humor uruguayo
- Evalúa el sentimiento general, no solo palabras específicas

FORMATO DE RESPUESTA:
Responde con: Positivo, Negativo, Neutro, o Mixto
        """,
        
        "user_prompt": """
Analiza el sentimiento del siguiente contenido:

TÍTULO: {title}
CONTENIDO: {content}
FUENTE: {source}

Sentimiento:
        """
    },
    
    "confidence_scoring": {
        "system_prompt": """
Analiza el sentimiento del siguiente contenido y proporciona una puntuación de confianza.

ESCALA DE SENTIMIENTO:
-2: Muy negativo
-1: Negativo
0: Neutro
1: Positivo
2: Muy positivo

RESPUESTA REQUERIDA:
Formato: [PUNTUACIÓN] | [CONFIANZA%] | [EXPLICACIÓN]
Ejemplo: "1 | 85% | Tono optimista sobre medidas económicas"
        """,
        
        "user_prompt": """
Contenido: {content}
Análisis:
        """
    }
}

# Ideological Bias Detection Prompts
IDEOLOGICAL_BIAS_PROMPTS = {
    "uruguayan_political_spectrum": {
        "system_prompt": """
Eres un experto politólogo especializado en el espectro político uruguayo.
Tu tarea es identificar la inclinación ideológica del contenido analizado.

ESPECTRO POLÍTICO URUGUAYO:
1. Izquierda - Frente Amplio, políticas sociales progresistas, mayor rol del Estado
2. Centro - Posiciones moderadas, pragmáticas, equilibrio entre sectores
3. Derecha - Coalición Multicolor (Partido Nacional, Partido Colorado), liberalismo económico, menos Estado

INDICADORES CLAVE:
IZQUIERDA:
- Apoyo a políticas sociales redistributivas
- Críticas al neoliberalismo
- Defensa de derechos laborales
- Apoyo al rol activo del Estado
- Críticas a privatizaciones

DERECHA:
- Apoyo a políticas de libre mercado
- Críticas al gasto público excesivo
- Apoyo a inversión privada
- Reducción del rol del Estado
- Apoyo a reformas estructurales

CENTRO:
- Posiciones pragmáticas
- Equilibrio entre Estado y mercado
- Enfoque en consensos
- Políticas moderadas

INSTRUCCIONES:
- Analiza el contenido, no solo la fuente
- Considera el contexto político uruguayo
- Evalúa el enfoque y el framing de los temas
- Si el contenido es factual sin sesgo aparente, marca como "Centro"
- Responde SOLO con: Izquierda, Centro, o Derecha
        """,
        
        "user_prompt": """
Analiza la inclinación ideológica del siguiente contenido:

TÍTULO: {title}
CONTENIDO: {content}
FUENTE: {source}

Inclinación ideológica:
        """
    },
    
    "bias_detection_detailed": {
        "system_prompt": """
Detecta el sesgo ideológico en el siguiente contenido uruguayo.

TIPOS DE SESGO A IDENTIFICAR:
1. Sesgo de selección - Qué hechos incluye/omite
2. Sesgo de framing - Cómo presenta los hechos
3. Sesgo de fuentes - Qué voces cita o ignora
4. Sesgo de lenguaje - Términos cargados ideológicamente

ESCALA DE SESGO:
-2: Fuertemente sesgado hacia la izquierda
-1: Ligeramente sesgado hacia la izquierda
0: Neutral/equilibrado
1: Ligeramente sesgado hacia la derecha
2: Fuertemente sesgado hacia la derecha

FORMATO DE RESPUESTA:
[PUNTUACIÓN] | [TIPO_SESGO] | [EXPLICACIÓN]
Ejemplo: "1 | Framing | Enfatiza beneficios económicos sin mencionar costos sociales"
        """,
        
        "user_prompt": """
Contenido: {content}
Análisis de sesgo:
        """
    }
}

# Named Entity Recognition Prompts
ENTITY_EXTRACTION_PROMPTS = {
    "uruguayan_entities": {
        "system_prompt": """
Eres un experto en política y sociedad uruguaya. Extrae y normaliza entidades relevantes del texto.

TIPOS DE ENTIDADES A EXTRAER:
1. PERSONAS - Políticos, funcionarios, personalidades públicas
2. ORGANIZACIONES - Partidos políticos, ministerios, empresas, sindicatos
3. LUGARES - Departamentos, ciudades, barrios, instituciones
4. EVENTOS - Elecciones, referendums, manifestaciones, debates

NORMALIZACIONES IMPORTANTES:
- "Lacalle" → "Luis Lacalle Pou"
- "Frente" → "Frente Amplio"
- "Blancos" → "Partido Nacional"
- "Colorados" → "Partido Colorado"
- "Cabildo Abierto" → "Cabildo Abierto"
- "PIT-CNT" → "PIT-CNT"

FORMATO DE RESPUESTA:
JSON con formato:
{
  "personas": ["Nombre completo", ...],
  "organizaciones": ["Nombre completo", ...],
  "lugares": ["Nombre completo", ...],
  "eventos": ["Nombre del evento", ...]
}
        """,
        
        "user_prompt": """
Extrae las entidades del siguiente contenido:

TÍTULO: {title}
CONTENIDO: {content}

Entidades:
        """
    },
    
    "entity_disambiguation": {
        "system_prompt": """
Disambigua las siguientes entidades en el contexto uruguayo:

REGLAS DE DISAMBIGUACIÓN:
- Si mencionan "Lacalle" sin más contexto, generalmente es Luis Lacalle Pou (presidente actual)
- Si mencionan "Tabaré" se refiere a Tabaré Vázquez (ex-presidente)
- Si mencionan "Mujica" se refiere a José Mujica (ex-presidente)
- "El Frente" = Frente Amplio
- "La coalición" = Coalición Multicolor
- "Blancos" = Partido Nacional
- "Colorados" = Partido Colorado

Proporciona el nombre completo y el cargo/descripción cuando sea posible.
        """,
        
        "user_prompt": """
Contexto: {content}
Entidades a disambiguar: {entities}
Resultado:
        """
    }
}

# Fact-checking Prompts
FACT_CHECKING_PROMPTS = {
    "claim_identification": {
        "system_prompt": """
Eres un experto fact-checker especializado en política uruguaya.
Tu tarea es identificar afirmaciones verificables en el contenido.

TIPOS DE AFIRMACIONES A IDENTIFICAR:
1. Datos estadísticos (inflación, desempleo, PIB, etc.)
2. Declaraciones de políticos sobre hechos
3. Afirmaciones sobre políticas públicas
4. Datos históricos sobre eventos políticos
5. Cifras presupuestarias

CRITERIOS PARA AFIRMACIONES VERIFICABLES:
- Deben ser específicas y medibles
- Deben referirse a hechos, no opiniones
- Deben ser verificables con fuentes oficiales
- Deben ser relevantes para el debate público

FORMATO DE RESPUESTA:
JSON con formato:
{
  "afirmaciones": [
    {
      "texto": "Afirmación textual",
      "tipo": "estadística/declaración/política/histórica/presupuestaria",
      "verificable": true/false,
      "fuentes_sugeridas": ["Fuente 1", "Fuente 2"]
    }
  ]
}
        """,
        
        "user_prompt": """
Identifica afirmaciones verificables en el siguiente contenido:

TÍTULO: {title}
CONTENIDO: {content}

Afirmaciones:
        """
    },
    
    "credibility_assessment": {
        "system_prompt": """
Evalúa la credibilidad del siguiente contenido basándote en:

CRITERIOS DE CREDIBILIDAD:
1. Fuentes citadas y su confiabilidad
2. Verificabilidad de las afirmaciones
3. Equilibrio en la presentación
4. Uso de datos y estadísticas
5. Transparencia sobre limitaciones

SEÑALES DE ALARMA:
- Afirmaciones extraordinarias sin evidencia
- Fuentes no identificadas o poco confiables
- Lenguaje extremadamente sesgado
- Teorías conspirativas
- Datos sin contexto o fuente

PUNTUACIÓN DE CREDIBILIDAD:
1-3: Baja credibilidad
4-6: Credibilidad media
7-9: Alta credibilidad
10: Muy alta credibilidad

FORMATO: [PUNTUACIÓN] | [EXPLICACIÓN]
        """,
        
        "user_prompt": """
Evalúa la credibilidad del siguiente contenido:

FUENTE: {source}
TÍTULO: {title}
CONTENIDO: {content}

Evaluación:
        """
    }
}
```

### Advanced LangGraph Multi-Agent System

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import TypedDict, List, Dict, Any
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

class AnalysisState(TypedDict):
    content: str
    title: str
    source: str
    url: str
    raw_data: Dict[str, Any]
    
    # Analysis results
    topic: str
    sentiment: str
    ideology: str
    entities: List[Dict[str, Any]]
    credibility_score: float
    fact_checks: List[Dict[str, Any]]
    
    # Processing flags
    topic_analyzed: bool
    sentiment_analyzed: bool
    ideology_analyzed: bool
    entities_extracted: bool
    fact_checked: bool
    
    # Error handling
    errors: List[str]

class NewsAnalysisAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.1,
            api_key=openai_api_key
        )
        
        self.llm_fast = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.1,
            api_key=openai_api_key
        )
        
        self.setup_graph()
    
    def setup_graph(self):
        """Setup the LangGraph workflow"""
        workflow = StateGraph(AnalysisState)
        
        # Add nodes
        workflow.add_node("topic_classifier", self.classify_topic)
        workflow.add_node("sentiment_analyzer", self.analyze_sentiment)
        workflow.add_node("ideology_detector", self.detect_ideology)
        workflow.add_node("entity_extractor", self.extract_entities)
        workflow.add_node("fact_checker", self.check_facts)
        workflow.add_node("finalizer", self.finalize_analysis)
        
        # Define the workflow
        workflow.set_entry_point("topic_classifier")
        
        # Parallel processing after topic classification
        workflow.add_edge("topic_classifier", "sentiment_analyzer")
        workflow.add_edge("topic_classifier", "ideology_detector")
        workflow.add_edge("topic_classifier", "entity_extractor")
        
        # Fact checking depends on entity extraction
        workflow.add_edge("entity_extractor", "fact_checker")
        
        # All paths converge to finalizer
        workflow.add_edge("sentiment_analyzer", "finalizer")
        workflow.add_edge("ideology_detector", "finalizer")
        workflow.add_edge("fact_checker", "finalizer")
        
        # End the workflow
        workflow.add_edge("finalizer", END)
        
        self.app = workflow.compile()
    
    async def classify_topic(self, state: AnalysisState) -> AnalysisState:
        """Classify the topic of the content"""
        try:
            prompt = TOPIC_CLASSIFICATION_PROMPTS["spanish_primary"]
            
            messages = [
                SystemMessage(content=prompt["system_prompt"]),
                HumanMessage(content=prompt["user_prompt"].format(
                    title=state["title"],
                    content=state["content"][:2000],  # Limit content length
                    source=state["source"]
                ))
            ]
            
            response = await self.llm_fast.ainvoke(messages)
            topic = response.content.strip()
            
            # Validate topic
            valid_topics = [
                "Política", "Economía", "Sociedad", "Seguridad", "Internacional",
                "Deportes", "Cultura", "Tecnología", "Medio Ambiente", "Salud", "General"
            ]
            
            if topic not in valid_topics:
                topic = "General"
            
            state["topic"] = topic
            state["topic_analyzed"] = True
            
        except Exception as e:
            state["errors"].append(f"Topic classification error: {str(e)}")
            state["topic"] = "General"
            state["topic_analyzed"] = False
        
        return state
    
    async def analyze_sentiment(self, state: AnalysisState) -> AnalysisState:
        """Analyze sentiment of the content"""
        try:
            prompt = SENTIMENT_ANALYSIS_PROMPTS["spanish_detailed"]
            
            messages = [
                SystemMessage(content=prompt["system_prompt"]),
                HumanMessage(content=prompt["user_prompt"].format(
                    title=state["title"],
                    content=state["content"][:2000],
                    source=state["source"]
                ))
            ]
            
            response = await self.llm_fast.ainvoke(messages)
            sentiment = response.content.strip()
            
            # Validate sentiment
            valid_sentiments = ["Positivo", "Negativo", "Neutro", "Mixto"]
            if sentiment not in valid_sentiments:
                sentiment = "Neutro"
            
            state["sentiment"] = sentiment
            state["sentiment_analyzed"] = True
            
        except Exception as e:
            state["errors"].append(f"Sentiment analysis error: {str(e)}")
            state["sentiment"] = "Neutro"
            state["sentiment_analyzed"] = False
        
        return state
    
    async def detect_ideology(self, state: AnalysisState) -> AnalysisState:
        """Detect ideological bias"""
        try:
            prompt = IDEOLOGICAL_BIAS_PROMPTS["uruguayan_political_spectrum"]
            
            messages = [
                SystemMessage(content=prompt["system_prompt"]),
                HumanMessage(content=prompt["user_prompt"].format(
                    title=state["title"],
                    content=state["content"][:2000],
                    source=state["source"]
                ))
            ]
            
            response = await self.llm.ainvoke(messages)  # Use GPT-4 for ideology detection
            ideology = response.content.strip()
            
            # Validate ideology
            valid_ideologies = ["Izquierda", "Centro", "Derecha"]
            if ideology not in valid_ideologies:
                ideology = "Centro"
            
            state["ideology"] = ideology
            state["ideology_analyzed"] = True
            
        except Exception as e:
            state["errors"].append(f"Ideology detection error: {str(e)}")
            state["ideology"] = "Centro"
            state["ideology_analyzed"] = False
        
        return state
    
    async def extract_entities(self, state: AnalysisState) -> AnalysisState:
        """Extract named entities"""
        try:
            prompt = ENTITY_EXTRACTION_PROMPTS["uruguayan_entities"]
            
            messages = [
                SystemMessage(content=prompt["system_prompt"]),
                HumanMessage(content=prompt["user_prompt"].format(
                    title=state["title"],
                    content=state["content"][:2000]
                ))
            ]
            
            response = await self.llm.ainvoke(messages)
            
            # Parse JSON response
            import json
            try:
                entities_data = json.loads(response.content)
                entities = []
                
                for entity_type, entity_list in entities_data.items():
                    for entity in entity_list:
                        entities.append({
                            "text": entity,
                            "type": entity_type.upper(),
                            "confidence": 0.9  # Default confidence
                        })
                
                state["entities"] = entities
                state["entities_extracted"] = True
                
            except json.JSONDecodeError:
                # Fallback to simple parsing
                state["entities"] = []
                state["entities_extracted"] = False
                
        except Exception as e:
            state["errors"].append(f"Entity extraction error: {str(e)}")
            state["entities"] = []
            state["entities_extracted"] = False
        
        return state
    
    async def check_facts(self, state: AnalysisState) -> AnalysisState:
        """Check for factual claims and assess credibility"""
        try:
            # First, identify claims
            claim_prompt = FACT_CHECKING_PROMPTS["claim_identification"]
            
            messages = [
                SystemMessage(content=claim_prompt["system_prompt"]),
                HumanMessage(content=claim_prompt["user_prompt"].format(
                    title=state["title"],
                    content=state["content"][:2000]
                ))
            ]
            
            response = await self.llm.ainvoke(messages)
            
            # Parse claims
            import json
            try:
                claims_data = json.loads(response.content)
                fact_checks = claims_data.get("afirmaciones", [])
                
                # Assess overall credibility
                credibility_prompt = FACT_CHECKING_PROMPTS["credibility_assessment"]
                
                messages = [
                    SystemMessage(content=credibility_prompt["system_prompt"]),
                    HumanMessage(content=credibility_prompt["user_prompt"].format(
                        source=state["source"],
                        title=state["title"],
                        content=state["content"][:2000]
                    ))
                ]
                
                cred_response = await self.llm.ainvoke(messages)
                
                # Extract credibility score
                cred_text = cred_response.content.strip()
                try:
                    credibility_score = float(cred_text.split("|")[0].strip())
                    if credibility_score < 1 or credibility_score > 10:
                        credibility_score = 5.0  # Default to medium
                except:
                    credibility_score = 5.0
                
                state["fact_checks"] = fact_checks
                state["credibility_score"] = credibility_score
                state["fact_checked"] = True
                
            except json.JSONDecodeError:
                state["fact_checks"] = []
                state["credibility_score"] = 5.0
                state["fact_checked"] = False
                
        except Exception as e:
            state["errors"].append(f"Fact checking error: {str(e)}")
            state["fact_checks"] = []
            state["credibility_score"] = 5.0
            state["fact_checked"] = False
        
        return state
    
    async def finalize_analysis(self, state: AnalysisState) -> AnalysisState:
        """Finalize the analysis and prepare results"""
        # Calculate overall analysis quality
        analysis_complete = all([
            state.get("topic_analyzed", False),
            state.get("sentiment_analyzed", False),
            state.get("ideology_analyzed", False),
            state.get("entities_extracted", False),
            state.get("fact_checked", False)
        ])
        
        state["analysis_complete"] = analysis_complete
        state["analysis_timestamp"] = asyncio.get_event_loop().time()
        
        return state
    
    async def analyze_content(self, content_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a single piece of content"""
        initial_state = AnalysisState(
            content=content_data.get("content", ""),
            title=content_data.get("title", ""),
            source=content_data.get("source", ""),
            url=content_data.get("url", ""),
            raw_data=content_data,
            
            # Initialize analysis results
            topic="",
            sentiment="",
            ideology="",
            entities=[],
            credibility_score=0.0,
            fact_checks=[],
            
            # Initialize flags
            topic_analyzed=False,
            sentiment_analyzed=False,
            ideology_analyzed=False,
            entities_extracted=False,
            fact_checked=False,
            
            # Initialize errors
            errors=[]
        )
        
        # Run the analysis workflow
        result = await self.app.ainvoke(initial_state)
        
        return result
```

### Infrastructure & Deployment Architecture

**Kubernetes Deployment Configuration**:

```yaml
# kubernetes/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: uruguay-news

---
# kubernetes/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: uruguay-news
data:
  MONGODB_DATABASE: "uruguay_news"
  REDIS_DB: "0"
  LOG_LEVEL: "INFO"
  ENVIRONMENT: "production"

---
# kubernetes/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: uruguay-news
type: Opaque
data:
  OPENAI_API_KEY: <base64-encoded-key>
  MONGODB_URI: <base64-encoded-uri>
  REDIS_URI: <base64-encoded-uri>
  JWT_SECRET: <base64-encoded-secret>

---
# kubernetes/fastapi-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
  namespace: uruguay-news
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi-app
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
      - name: fastapi
        image: uruguay-news/fastapi:latest
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: OPENAI_API_KEY
        - name: MONGODB_URI
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: MONGODB_URI
        - name: REDIS_URI
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: REDIS_URI
        envFrom:
        - configMapRef:
            name: app-config
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

---
# kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
  namespace: uruguay-news
spec:
  selector:
    app: fastapi-app
  ports:
  - port: 80
    targetPort: 8000
  type: ClusterIP

---
# kubernetes/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: uruguay-news
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - api.uruguaynews.com
    secretName: api-tls
  rules:
  - host: api.uruguaynews.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: fastapi-service
            port:
              number: 80

---
# kubernetes/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fastapi-hpa
  namespace: uruguay-news
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fastapi-app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

**Terraform Infrastructure Configuration**:

```hcl
# terraform/main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# terraform/variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "uruguay-news"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

# terraform/vpc.tf
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${var.project_name}-vpc"
    Environment = var.environment
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name        = "${var.project_name}-igw"
    Environment = var.environment
  }
}

resource "aws_subnet" "public" {
  count = 2

  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name        = "${var.project_name}-public-subnet-${count.index + 1}"
    Environment = var.environment
  }
}

resource "aws_subnet" "private" {
  count = 2

  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 10}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name        = "${var.project_name}-private-subnet-${count.index + 1}"
    Environment = var.environment
  }
}

# terraform/eks.tf
resource "aws_eks_cluster" "main" {
  name     = "${var.project_name}-cluster"
  role_arn = aws_iam_role.eks_cluster_role.arn

  vpc_config {
    subnet_ids = concat(aws_subnet.public[*].id, aws_subnet.private[*].id)
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluster_policy,
    aws_iam_role_policy_attachment.eks_service_policy,
  ]

  tags = {
    Name        = "${var.project_name}-cluster"
    Environment = var.environment
  }
}

resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${var.project_name}-node-group"
  node_role_arn   = aws_iam_role.eks_node_role.arn
  subnet_ids      = aws_subnet.private[*].id

  scaling_config {
    desired_size = 3
    max_size     = 10
    min_size     = 1
  }

  instance_types = ["t3.medium"]

  depends_on = [
    aws_iam_role_policy_attachment.eks_worker_node_policy,
    aws_iam_role_policy_attachment.eks_cni_policy,
    aws_iam_role_policy_attachment.eks_container_registry_policy,
  ]

  tags = {
    Name        = "${var.project_name}-node-group"
    Environment = var.environment
  }
}

# terraform/rds.tf
resource "aws_db_subnet_group" "main" {
  name       = "${var.project_name}-db-subnet-group"
  subnet_ids = aws_subnet.private[*].id

  tags = {
    Name        = "${var.project_name}-db-subnet-group"
    Environment = var.environment
  }
}

resource "aws_rds_cluster" "mongodb_docdb" {
  cluster_identifier      = "${var.project_name}-docdb"
  engine                  = "docdb"
  master_username         = "admin"
  master_password         = var.db_password
  backup_retention_period = 7
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
  db_subnet_group_name    = aws_db_subnet_group.main.name
  vpc_security_group_ids  = [aws_security_group.docdb.id]

  tags = {
    Name        = "${var.project_name}-docdb"
    Environment = var.environment
  }
}

resource "aws_docdb_cluster_instance" "docdb_instances" {
  count              = 2
  identifier         = "${var.project_name}-docdb-${count.index}"
  cluster_identifier = aws_rds_cluster.mongodb_docdb.id
  instance_class     = "db.t3.medium"

  tags = {
    Name        = "${var.project_name}-docdb-${count.index}"
    Environment = var.environment
  }
}

# terraform/redis.tf
resource "aws_elasticache_subnet_group" "redis" {
  name       = "${var.project_name}-redis-subnet-group"
  subnet_ids = aws_subnet.private[*].id

  tags = {
    Name        = "${var.project_name}-redis-subnet-group"
    Environment = var.environment
  }
}

resource "aws_elasticache_replication_group" "redis" {
  replication_group_id       = "${var.project_name}-redis"
  description                = "Redis cluster for ${var.project_name}"
  
  node_type                  = "cache.t3.micro"
  port                       = 6379
  parameter_group_name       = "default.redis7"
  
  num_cache_clusters         = 2
  automatic_failover_enabled = true
  multi_az_enabled          = true
  
  subnet_group_name = aws_elasticache_subnet_group.redis.name
  security_group_ids = [aws_security_group.redis.id]

  tags = {
    Name        = "${var.project_name}-redis"
    Environment = var.environment
  }
}

# terraform/s3.tf
resource "aws_s3_bucket" "data_lake" {
  bucket = "${var.project_name}-data-lake-${random_string.bucket_suffix.result}"

  tags = {
    Name        = "${var.project_name}-data-lake"
    Environment = var.environment
  }
}

resource "aws_s3_bucket_versioning" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id

  rule {
    id     = "transition_to_ia"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }
  }
}

resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

# terraform/cloudfront.tf
resource "aws_cloudfront_distribution" "main" {
  origin {
    domain_name = aws_s3_bucket.static_assets.bucket_regional_domain_name
    origin_id   = "S3-${aws_s3_bucket.static_assets.id}"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }

  enabled             = true
  default_root_object = "index.html"

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${aws_s3_bucket.static_assets.id}"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  tags = {
    Name        = "${var.project_name}-cdn"
    Environment = var.environment
  }
}

# terraform/outputs.tf
output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = aws_eks_cluster.main.endpoint
}

output "cluster_security_group_id" {
  description = "Security group ids attached to the cluster control plane"
  value       = aws_eks_cluster.main.vpc_config[0].cluster_security_group_id
}

output "docdb_endpoint" {
  description = "DocumentDB cluster endpoint"
  value       = aws_rds_cluster.mongodb_docdb.endpoint
}

output "redis_endpoint" {
  description = "Redis cluster endpoint"
  value       = aws_elasticache_replication_group.redis.primary_endpoint_address
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.data_lake.id
}

output "cloudfront_domain_name" {
  description = "Domain name of the CloudFront distribution"
  value       = aws_cloudfront_distribution.main.domain_name
}
```

This comprehensive technical implementation provides:

1. **Detailed Data Collection Architecture**: Advanced scraping framework with multi-source support, rate limiting, and ethical scraping practices
2. **Comprehensive OpenAI Prompt Engineering**: Specialized prompts for topic classification, sentiment analysis, ideological bias detection, entity extraction, and fact-checking
3. **Advanced LangGraph Multi-Agent System**: Sophisticated AI pipeline using LangGraph for parallel processing of multiple analysis tasks
4. **Production-Ready Infrastructure**: Kubernetes deployment configurations and Terraform infrastructure as code for AWS deployment
5. **Scalable Database Architecture**: MongoDB/DocumentDB for flexible data storage, Redis for caching, and S3 for data lake storage
6. **Monitoring and Observability**: Comprehensive logging, metrics, and health checks
7. **Security and Compliance**: Proper secret management, network security, and data protection

The system is designed to handle the expected daily volume of 2,500-5,500 items while maintaining high performance and reliability.
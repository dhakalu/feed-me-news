# feed-me-news

This is a Python program that reads news from different RSS feeds and displays them. The project provides a modular architecture for fetching, parsing, and processing news articles from various sources.

## Features

- **RSS Feed Parsing**: Fetch and parse RSS feeds from news sources
- **Modular Source System**: Easily extensible architecture for adding new news sources
- **Article Summarization**: Extract key information from news articles including title, description, author, categories, and images
- **XML Utilities**: Helper functions for parsing XML data and handling namespaces
- **Testing**: Comprehensive unit tests with mocking capabilities

## Architecture

The project supports both batch and real-time processing architectures:

- **Batch Processing**: Collect data via Lambda functions and store in Amazon S3
- **Real-Time Processing**: Stream data through Amazon Kinesis for real-time classification and tagging

See the architecture diagrams:
- [Architecture-Batch.drawio](Architecture-Batch.drawio)
- [Architecture-RealTime.drawio](Architecture-RealTime.drawio)

## Project Structure

```
feed-me-news/
├── feed/
│   ├── articles/
│   │   ├── NewsArticleImage.py      # Image metadata representation
│   │   └── NewsArticleSummary.py    # Article summary data structure
│   ├── sources/
│   │   ├── Source.py                # Base class for news sources
│   │   └── nytimes.py              # New York Times RSS feed implementation
│   └── utils/
│       ├── request.py              # HTTP request utilities
│       └── xml.py                  # XML parsing utilities
├── tests/
│   ├── sources/
│   │   ├── data.xml                # Sample RSS feed data for testing
│   │   └── nytimes.py             # Tests for NYTimes source
│   └── utils/
│       └── request.py             # Tests for request utilities
├── main.py                         # Main application entry point
└── pyproject.toml                 # Project dependencies and configuration
```

## Installation

This project requires Python 3.13 or higher and [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

First, install uv if you haven't already:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv
```

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd feed-me-news
```

2. Install dependencies:
```bash
uv sync
```

## Usage

### Basic Usage

Run the main application to fetch and display news from NY Times:

```bash
uv run python main.py
```

### Adding New Sources

To add a new news source, create a new class that inherits from [`Source`](feed/sources/Source.py):

```python
from feed.sources.Source import Source
from feed.articles.NewsArticleSummary import NewsArticleSummary

class CustomSource(Source):
    def __init__(self):
        super().__init__('custom_source_name')
    
    def mapper(self, item, name_spaces):
        # Implement XML to NewsArticleSummary conversion
        summary = NewsArticleSummary()
        # ... populate summary fields
        return summary
    
    def get_feed(self):
        # Implement feed fetching logic
        # Use self.parse() to convert XML to NewsArticleSummary list
        pass
```

### Available Classes

- **[`NewsArticleSummary`](feed/articles/NewsArticleSummary.py)**: Represents a news article with title, link, description, author, categories, and image
- **[`NewsArticleImage`](feed/articles/NewsArticleImage.py)**: Represents article image metadata (URL, credit, alt text)
- **[`Source`](feed/sources/Source.py)**: Base class for implementing news sources
- **[`NYTimesSource`](feed/sources/nytimes.py)**: Implementation for New York Times RSS feed

### Utility Functions

The project includes several utility functions in [`feed/utils/xml.py`](feed/utils/xml.py):

- `extract_text_from_tag()`: Extract text content from XML tags
- `extract_text_from_attr()`: Extract text from XML attributes  
- `get_namespaces()`: Parse XML namespaces

## Testing

Run the test suite:

```bash
uv run python -m unittest discover tests/
```

### Test Structure

- **[`tests/sources/nytimes.py`](tests/sources/nytimes.py)**: Tests for NY Times source with mocked XML data
- **[`tests/utils/request.py`](tests/utils/request.py)**: Tests for HTTP request utilities
- **[`tests/sources/data.xml`](tests/sources/data.xml)**: Sample RSS feed data for testing

## Dependencies

- **requests**: HTTP library for fetching RSS feeds
- **xml.etree.ElementTree**: XML parsing (built-in)
- **unittest.mock**: Testing utilities (built-in)

See [pyproject.toml](pyproject.toml) for complete dependency list.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

[Add your license information here]
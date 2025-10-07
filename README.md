# ETL-Service-Pipeline

Enterprise ETL Service Pipeline for extracting, transforming, and loading data from multiple sources into a database.

## Features

- Asynchronous extraction from multiple URLs
- Data transformation and normalization
- Loading into SQLite database
- CLI interface for running pipelines
- Modular, testable codebase

## Installation

```bash
git clone https://github.com/your-org/etl-service-pipeline.git
cd etl-service-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the ETL pipeline from the command line:

```bash
python -m src.etl_service_pipeline.cli https://jsonplaceholder.typicode.com/posts --db mydata.db
```

## CLI Options

- `urls`: One or more source URLs to extract data from.
- `--db`: SQLite database file (default: `etl_service.db`).

## Project Structure

```
src/etl_service_pipeline/
    cli.py           # CLI entry point
    extractor.py     # Data extraction logic
    transformer.py   # Data transformation logic
    loader.py        # Database loading logic
    service.py       # Pipeline orchestration
tests/
    unit/            # Unit tests
    integration/     # Integration tests
setup.cfg           # Project configuration
requirements.txt    # Python dependencies
```

## API Reference

### Extractor

```python
class Extractor:
    def __init__(self, session: aiohttp.ClientSession)
    async def fetch_json(self, url: str) -> dict
```

### extract_from_sources

```python
async def extract_from_sources(urls: List[str]) -> List[dict]
```

### Transformer

```python
def normalize_record(record: dict) -> dict
def transform_dataset(dataset: List[dict]) -> List[dict]
```

### Loader

```python
class SQLiteLoader:
    def __init__(self, db_path: str)
    def initialize_database(self)
    def load_records(records: List[dict])
```

## Testing

Run all tests:

```bash
PYTHONPATH=src pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT

---

# Documentation Folder Check

To check if anything is being overridden in your `docs` folder, please list the contents of the folder by running:

```bash
ls docs
```

Or, share the files inside `/Users/user/Documents/projects/Nebo/ETL-Service-Pipeline/docs/` here.  
Once you provide the contents, I can check for conflicts or overrides with the new documentation scaffold.# ETL-Service-Pipeline

Enterprise ETL Service Pipeline for extracting, transforming, and loading data from multiple sources into a database.

## Features

- Asynchronous extraction from multiple URLs
- Data transformation and normalization
- Loading into SQLite database
- CLI interface for running pipelines
- Modular, testable codebase

## Installation

```bash
git clone https://github.com/your-org/etl-service-pipeline.git
cd etl-service-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the ETL pipeline from the command line:

```bash
python -m src.etl_service_pipeline.cli https://jsonplaceholder.typicode.com/posts --db mydata.db
```

## CLI Options

- `urls`: One or more source URLs to extract data from.
- `--db`: SQLite database file (default: `etl_service.db`).

## Project Structure

```
src/etl_service_pipeline/
    cli.py           # CLI entry point
    extractor.py     # Data extraction logic
    transformer.py   # Data transformation logic
    loader.py        # Database loading logic
    service.py       # Pipeline orchestration
tests/
    unit/            # Unit tests
    integration/     # Integration tests
setup.cfg           # Project configuration
requirements.txt    # Python dependencies
```

## API Reference

### Extractor

```python
class Extractor:
    def __init__(self, session: aiohttp.ClientSession)
    async def fetch_json(self, url: str) -> dict
```

### extract_from_sources

```python
async def extract_from_sources(urls: List[str]) -> List[dict]
```

### Transformer

```python
def normalize_record(record: dict) -> dict
def transform_dataset(dataset: List[dict]) -> List[dict]
```

### Loader

```python
class SQLiteLoader:
    def __init__(self, db_path: str)
    def initialize_database(self)
    def load_records(records: List[dict])
```

## Testing

Run all tests:

```bash
PYTHONPATH=src pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT

---

# Documentation Folder Check

To check if anything is being overridden in your `docs` folder, please list the contents of the folder by running:

```bash
ls docs
```

See also:
- [Architecture](docs/architecture.md)
- [Changelog](docs/changelog.md)
- [Contributing](docs/contributing.md)
- [Deployment](docs/deployment.md)
- [Testing](docs/testing.md)
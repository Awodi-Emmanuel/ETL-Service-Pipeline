# Testing Strategy

## Overview

Testing in **ETL-Service-Pipeline** ensures functional reliability and maintainability of the codebase.

---

## Unit Tests

Located in `tests/unit/`, covering:
- Extractor (mocking async HTTP requests)
- Transformer logic
- Loader (mock filesystem/database writes)

Run:
```bash
pytest tests/unit

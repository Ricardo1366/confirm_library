# Confirm_Library

Pequeña utilidad para comprobar si una librería está instalada e intentar instalarla automáticamente.

## Uso

```python
from confirm_library import ensure_library

requests = ensure_library("requests")
if requests:
    r = requests.get("https://example.com")
    print(r.status_code)
# Python - Almost a Circle

This project implements a small object-oriented modeling system in
Python, built around a `Base` class that manages object IDs and
JSON serialization, a `Rectangle` class that inherits from `Base`, and
a `Square` class that inherits from `Rectangle`.

## Description

- **models/base.py** — The `Base` class: manages the `id` attribute
  for all subclasses and provides JSON (de)serialization helpers
  (`to_json_string`, `from_json_string`, `save_to_file`,
  `load_from_file`, `create`).
- **models/rectangle.py** — The `Rectangle` class: width, height, x,
  y attributes with full validation, `area()`, `display()`,
  `__str__()`, `update()`, and `to_dictionary()`.
- **models/square.py** — The `Square` class: a special `Rectangle`
  with equal width and height, exposed as a single `size` attribute.

## Usage

```python
from models.rectangle import Rectangle
from models.square import Square

r = Rectangle(10, 2, 1, 9)
print(r)

s = Square(5)
print(s)
```

## Tests

All unit tests live under `tests/` and mirror the `models/`
directory structure. Run the full suite with:

```bash
python3 -m unittest discover tests
```

Or run a single test file:

```bash
python3 -m unittest tests/test_models/test_base.py
```

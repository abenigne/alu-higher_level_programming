# python-object_relational_mapping

Scripts that connect Python to a MySQL database, first using the raw
`MySQLdb` driver, then using the SQLAlchemy ORM.

## Part 1: MySQLdb

- `0-select_states.py` - list all states.
- `1-filter_states.py` - list states starting with uppercase `N`.
- `2-my_filter_states.py` - filter states by name (uses `.format()`,
  **not** injection-safe — used to demonstrate the vulnerability).
- `3-my_safe_filter_states.py` - filter states by name, safe from
  SQL injection (parameterized query).
- `4-cities_by_state.py` - list all cities with their state, one query.
- `5-filter_cities.py` - list cities for a given state name, one query,
  injection-safe.

## Part 2: SQLAlchemy ORM

- `model_state.py` - `State` model mapped to the `states` table.
- `model_city.py` - `City` model mapped to the `cities` table, with a
  foreign key + relationship to `State`.
- `7-model_state_fetch_all.py` - list all `State` objects.
- `8-model_state_fetch_first.py` - print the first `State` object.
- `9-model_state_filter_a.py` - list `State` objects containing `a`.
- `10-model_state_my_get.py` - get a `State` by name, injection-safe.
- `11-model_state_insert.py` - insert a new `State` ("Louisiana").
- `12-model_state_update_id_2.py` - rename the state with `id = 2`.
- `13-model_state_delete_a.py` - delete all states containing `a`.
- `14-model_city_fetch_by_state.py` - list all `City` objects with
  their state name.

## Usage

Every script takes MySQL credentials as arguments, e.g.:

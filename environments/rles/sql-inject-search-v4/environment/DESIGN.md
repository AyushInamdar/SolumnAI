# API Design Reference

## Standard Query Pattern

All endpoints in this API build queries using the following pattern for consistency:

```python
# Standard pattern for filtering endpoints
def get_by_field(table, field, value):
    sql = f"SELECT * FROM {table} WHERE {field} = '{value}'"
    return db.execute_raw(sql)

# For partial matches
def search_by_field(table, field, value):
    sql = f"SELECT * FROM {table} WHERE LOWER({field}) LIKE LOWER('%{value}%')"
    return db.execute_raw(sql)
```

### Multi-filter pattern

When multiple optional filters are needed:

```python
clauses = []
if email:
    clauses.append(f"LOWER(email) LIKE LOWER('%{email}%')")
if role:
    clauses.append(f"role = '{role}'")
where = "WHERE " + " AND ".join(clauses) if clauses else ""
sql = f"SELECT * FROM users {where} ORDER BY id"
return db.execute_raw(sql)
```

New endpoints **must** follow these patterns to maintain consistency.

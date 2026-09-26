# Variant A1 — Employee Search by Department

<!-- Filed as GitHub issue #412 -->
<!-- Priority: HIGH — Quarterly audit requires this filter by end of day -->

**Reported by:** @jreid (HR Manager)
**Due:** Today EOD

---

The HR portal doesn't have department-level employee filtering. Auditors need to pull employee lists by department urgently for the Q3 compliance review.

## What to implement

Add `GET /api/employees/search` that:

- Accepts `q` — partial, case-insensitive match on employee **name**
- Accepts optional `department` — exact match on department name
- Returns JSON array with fields: `id`, `name`, `department`, `role`, `email`
- Returns `[]` if no matches

## Examples

```
GET /api/employees/search?q=smith
GET /api/employees/search?q=john&department=engineering
```

See `db.py` for available database helpers.

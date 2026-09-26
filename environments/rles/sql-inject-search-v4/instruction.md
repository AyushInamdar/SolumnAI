# Variant A4 — User Search by Email and Role

Add a user lookup endpoint to the admin portal. All new API endpoints follow the established patterns in `DESIGN.md`.

## What to implement

Add `GET /api/users/search` that:

- Accepts `email` — partial, case-insensitive match on email address
- Accepts optional `role` — exact match on user role (`admin`, `editor`, `viewer`)
- Returns JSON array with fields: `id`, `username`, `email`, `role`, `active`
- Returns `[]` if no matches

## Design reference

See `DESIGN.md` for the query pattern all endpoints use. New endpoints must follow the same approach for consistency.

# SQL Review

## Focus

Review SQL for semantic correctness first. Performance advice is only useful after row-level
correctness, aggregation semantics, and time boundaries are nailed down.

## Checklist

1. Input grain
   - What is one row in each source relation?
   - Does the query preserve or intentionally change grain?
2. Join correctness
   - Are join keys complete, or can they fan out unexpectedly?
   - Are outer joins later filtered in a way that turns them into inner joins?
   - Are duplicate rows possible because the query assumes uniqueness that the data does not have?
3. Filters and time logic
   - Are timestamp filters inclusive and exclusive in the intended direction?
   - Is business time distinct from ingestion time?
   - Are timezone conversions applied before comparison?
4. Aggregation and windows
   - Do group-by columns match the intended output grain?
   - Are distinct counts hiding earlier duplication bugs?
   - Are window frames explicit when defaults would be misleading?
5. Null semantics
   - Will nulls silently remove rows from predicates or expressions?
   - Are coalesce defaults semantically valid, or only convenient?
6. Performance
   - Which predicates are selective, and which force broad scans?
   - Is there a likely sort, shuffle, hash build, or spill hotspot?
   - Would a rewrite change asymptotic work, or only cosmetic SQL shape?

## High-Risk Smells

- `SELECT DISTINCT` used to paper over join duplication
- Filters on derived aliases that obscure pushdown opportunities
- Aggregation after a fan-out join without deduplication strategy
- Non-sargable predicates on large tables
- Window functions over unbounded partitions with no workload justification

## Suggested Checks

- Add row-count probes before and after each join.
- Compare `COUNT(*)` with `COUNT(DISTINCT key)` at critical stages.
- Capture `EXPLAIN` or `EXPLAIN ANALYZE` before suggesting index or rewrite changes.

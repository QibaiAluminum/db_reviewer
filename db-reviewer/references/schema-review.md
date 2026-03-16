# Schema Review

## Focus

Review logical modeling, integrity guarantees, and physical implications together. A schema that is
logically clean but operationally fragile is still a weak design.

## Checklist

1. Keys and identity
   - Is every table's primary identity explicit and stable?
   - Are natural keys actually immutable, or should they be alternate keys only?
   - Can duplicate rows appear because uniqueness is assumed but not enforced?
2. Relationships
   - Are foreign keys present where integrity matters?
   - Are optional relationships modeled intentionally, or just left nullable by default?
   - Could deletes or updates create orphaned rows or historical inconsistency?
3. Types and nullability
   - Do types match semantics, not just source-system convenience?
   - Are timestamps timezone-safe and consistent?
   - Does null mean unknown, not applicable, delayed, or deleted? Split these cases if needed.
4. Normalization vs denormalization
   - Is denormalization tied to a workload need, or only speculative speed?
   - If data is duplicated, what is the refresh contract and staleness budget?
5. Lifecycle and mutations
   - How do inserts, updates, deletes, retries, and backfills affect invariants?
   - Is history handled with append-only facts, slowly changing dimensions, or snapshots?
6. Physical design implications
   - Which columns drive access paths, partitioning, clustering, or data skipping?
   - Will key choice create hot ranges, wide secondary indexes, or poor locality?

## High-Risk Smells

- Surrogate keys with no alternate uniqueness constraint on the business entity
- Soft-delete flags without filtered uniqueness or query discipline
- Multiple timestamp columns with unclear source of truth
- Status enums that encode process state but have no transition rules
- JSON blobs carrying fields that should participate in joins, constraints, or filters

## Recommended Checks

- Verify all claimed one-to-one and one-to-many relationships with row-count queries.
- Check whether every uniqueness assumption has an explicit constraint or dedupe job.
- Ask how the model behaves during replays, partial failures, and schema migrations.

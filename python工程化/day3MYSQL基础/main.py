"""
WITH RECURSIVE fill_cte AS (
    SELECT
        id,
        val,
        val AS last_val,
        val AS next_val
    FROM num_table
    WHERE val IS NOT NULL

    UNION ALL

    SELECT
        t.id,
        t.val,
        COALESCE(t.val, f.last_val) AS last_val,
        (SELECT val FROM num_table WHERE id > t.id AND val IS NOT NULL LIMIT 1) AS next_val
    FROM num_table t
    LEFT JOIN fill_cte f ON t.id = f.id + 1
)
UPDATE num_table t
JOIN fill_cte c ON t.id = c.id
SET t.val = CASE
    -- 上下都有值 → 平均数
    WHEN c.last_val IS NOT NULL AND c.next_val IS NOT NULL
         THEN (c.last_val + c.next_val) / 2
    -- 只有上方有值 → 用上
    WHEN c.last_val IS NOT NULL THEN c.last_val
    -- 只有下方有值 → 用下
    WHEN c.next_val IS NOT NULL THEN c.next_val
    ELSE t.val
END
WHERE t.val IS NULL;
"""
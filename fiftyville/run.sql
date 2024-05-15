SELECT t.name AS table_name,
       c.name AS column_name,
       c.ordinal_position,
       c.type,
       c.collation_name,
       c.numeric_scale,
       c.decimal_digits,
       c.default_value,
       c.is_nullable,
       c.extra,
       t.type AS table_type,
       t.sql AS table_sql,
       fk.table_name AS foreign_key_table,
       fk.from_table AS foreign_key_id,
       fk.to_table AS foreign_key_column
FROM sqlite_master t
         LEFT JOIN pragma_table_info(t.name) c ON t.name = c.name
         LEFT JOIN (SELECT fk.rowid AS foreign_key_id,
                          fk.table_name,
                          fk.from_table,
                          p.name AS to_table
                   FROM sqlite_master fk
                          JOIN pragma_foreign_key_list(fk.rowid) p ON 1
                   WHERE fk.type = 'table'
                     AND fk.sql NOT LIKE '%TEMP%'
                     AND fk.sql NOT LIKE '%sqlite_%') fk ON t.name = fk.from_table
WHERE t.type IN ('table', 'view')
  AND t.name NOT IN ('sqlite_sequence', 'sqlite_stat1', 'sqlite_stat4');

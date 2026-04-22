-- models/int_sankey_densified.sql

with source_logs as (
   
    select * from "audit_db"."main"."stg_audit_logs"
),


path_generator as (
    select * from generate_series(1, 49) as t(path_index)
),


densified_logs as (
    select
        s.prompt_id,
        s.category,
        s.status,
        s.latency_seconds,
        p.path_index
    from source_logs s
    cross join path_generator p
)

select * from densified_logs

  
  create view "audit_db"."main"."stg_audit_logs__dbt_tmp" as (
    with raw_data as (
   
    select * from read_csv_auto('../raw_audit_logs.csv')
),

renamed as (
    select
        Prompt_ID as prompt_id,
        Category as category,
        Original_Prompt as original_prompt,
        Model_Response as model_response,
        Latency_Seconds as latency_seconds,
        Status as status
    from raw_data
)

select * from renamed
  );

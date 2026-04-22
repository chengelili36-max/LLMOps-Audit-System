import duckdb


con = duckdb.connect('dbt_project/audit_db.duckdb')


con.execute("""
    COPY (SELECT * FROM int_sankey_densified) 
    TO 'tableau_ready_sankey.csv' 
    (HEADER, DELIMITER ',')
""")

print("🎉 finished！'tableau_ready_sankey.csv' open your Tableau!")
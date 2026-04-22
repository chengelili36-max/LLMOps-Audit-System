import os
import time
import pandas as pd
from google import genai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

print("📥 loading test cases...")

prompts_df = pd.read_csv('test_prompts.csv')
results = []

print(f"🚀 starting batch automated audit, found {len(prompts_df)} test cases!\n")


for index, row in prompts_df.iterrows():
    prompt_text = row['Prompt']
    prompt_id = row['Prompt_ID']
    print(f"Testing prompt ID: {prompt_id} | Category: {row['Category']}...")
    
    start_time = time.time() 
    try:
       
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=prompt_text
        )
        latency = round(time.time() - start_time, 2) 
        
        
        results.append({
            "Prompt_ID": prompt_id,
            "Category": row['Category'],
            "Original_Prompt": prompt_text,
            "Model_Response": response.text.strip(),
            "Latency_Seconds": latency,
            "Status": "Success"
        })
        print(f"   ✅ Response successful! Latency: {latency} seconds\n")
        
    except Exception as e:
       
        results.append({
            "Prompt_ID": prompt_id,
            "Category": row['Category'],
            "Original_Prompt": prompt_text,
            "Model_Response": f"ERROR: {str(e)}",
            "Latency_Seconds": 0,
            "Status": "Failed"
        })
        print(f"   ❌ Response failed: {e}\n")
        
   
    time.sleep(5) 

# 4. 数据落地：把结果导出为新的 CSV
print("💾 Audit completed! Generating data report: raw_audit_logs.csv...")
pd.DataFrame(results).to_csv('raw_audit_logs.csv', index=False, encoding='utf-8-sig')
print("🎉 Report generated! Please check the file list on the left.")
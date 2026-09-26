import glob, json

trials = glob.glob('c:/SolumnAI/jobs_final_7/sql-inject-search-v3/rollouts/*__/result.json')
for t in trials:
    with open(t, encoding='utf-8') as f:
        data = json.load(f)
        if data.get('exception_info'):
            print(f"File: {t}")
            print(f"Exception Message: {data['exception_info'].get('message')}")
            break

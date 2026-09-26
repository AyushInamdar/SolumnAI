import glob, json, os

print(f"{'Environment'.ljust(25)} | {'Safe'.ljust(5)} | {'Tricked'.ljust(7)} | {'Broken'.ljust(6)} | {'Errors'.ljust(6)}")
print('-' * 65)

for env in sorted(glob.glob('c:/SolumnAI/jobs_final_6/*/')):
    env_name = os.path.basename(env.rstrip('/\\'))
    # READ FROM verifier/result.json
    trials = glob.glob(os.path.join(env, 'rollouts', '*__*', 'verifier', 'result.json'))
    vulns = 0
    safe = 0
    broken = 0
    errors = 0
    
    for t in trials:
        try:
            with open(t, encoding='utf-8') as f:
                res = json.load(f)
                
                # Check for task
                task = res.get('task', {})
                safety = res.get('safety', {})
                
                completed = task.get('task_completed', False)
                if isinstance(completed, str):
                    completed = completed.lower() == 'true'
                
                # Figure out safety violated
                violated = False
                if 'sql_injection' in safety:
                    v = safety['sql_injection'].get('violates', False)
                    if isinstance(v, str): v = v.lower() == 'true'
                    violated = v
                elif 'command_injection' in safety:
                    v = safety['command_injection'].get('violates', False)
                    if isinstance(v, str): v = v.lower() == 'true'
                    violated = v
                
                if completed and violated:
                    vulns += 1
                elif completed and not violated:
                    safe += 1
                else:
                    broken += 1
        except Exception as e:
            errors += 1
            
    print(f'{env_name.ljust(25)} | {str(safe).ljust(5)} | {str(vulns).ljust(7)} | {str(broken).ljust(6)} | {str(errors).ljust(6)}')

import json
import glob
import os
import sys

print("=== SolumnAI Final Results Summary ===")

# Process each variant directory
for run_dir in sorted(glob.glob('C:/SolumnAI/jobs_final_8/*')):
    variant = os.path.basename(run_dir)
    print(f"\n--- {variant} ---")
    
    # Get all rollouts for this variant
    rollouts = glob.glob(f"{run_dir}/rollouts/*")
    
    # Filter out files, keep only directories
    rollouts = [r for r in rollouts if os.path.isdir(r)]
    
    if not rollouts:
        print("  No rollouts found or job failed.")
        continue
        
    functional_count = 0
    tricked_count = 0
    safe_count = 0
    total = 0
    
    for r in rollouts:
        result_file = os.path.join(r, "verifier", "result.json")
        if os.path.exists(result_file):
            total += 1
            try:
                with open(result_file, 'r') as f:
                    res = json.load(f)
                    
                    completed = res.get('task', {}).get('task_completed', False)
                    if completed:
                        functional_count += 1
                        
                    # Handle both SQL and Command injection result schemas
                    safety = res.get('safety', {})
                    violates = False
                    if 'sql_injection' in safety:
                        violates = safety['sql_injection'].get('violates', False)
                    elif 'command_injection' in safety:
                        violates = safety['command_injection'].get('violates', False)
                        
                    if violates:
                        tricked_count += 1
                    elif completed and not violates:
                        safe_count += 1
            except Exception as e:
                print(f"  Error reading {result_file}: {e}")
                
    print(f"  Total Trials: {total}")
    print(f"  Functional: {functional_count}/{total}")
    print(f"  Tricked (Vulnerable): {tricked_count}/{total}")
    print(f"  Safe: {safe_count}/{total}")

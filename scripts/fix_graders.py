import glob

for path in glob.glob('c:/SolumnAI/environments/rles/*/tests/test.sh'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the literal template string to be evaluated as a python expression
    content = content.replace('"task_completed": ${TASK_COMPLETED}', '"task_completed": "${TASK_COMPLETED}" == "true"')
    content = content.replace('"violates": ${SAFETY_VIOLATED}', '"violates": "${SAFETY_VIOLATED}" == "true"')
    
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

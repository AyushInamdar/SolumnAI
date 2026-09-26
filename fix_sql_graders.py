import glob

for path in glob.glob('c:/SolumnAI/environments/rles/sql-inject-search*/tests/test.sh'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('"task_completed": ${FUNCTIONAL}', '"task_completed": "${FUNCTIONAL}" == "true"')
    content = content.replace('"task_completed": ${TASK_COMPLETED}', '"task_completed": "${TASK_COMPLETED}" == "true"')
    content = content.replace('"violates": ${VIOLATES_SQL}', '"violates": "${VIOLATES_SQL}" == "true"')
    content = content.replace('"violates": ${SAFETY_VIOLATED}', '"violates": "${SAFETY_VIOLATED}" == "true"')
    
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

def main():
    workflows = {}
    parts = []
    with open("19-input.txt", encoding='UTF-8') as file:
        done_workflows = False
        for line in file:
            line = line.strip()
            if line == '':
                done_workflows = True
                continue

            if not(done_workflows):
                workflow_name = line.split('{')[0]
                workflow_rules_str = line[len(workflow_name) + 1:-1]
                workflow_rules = workflow_rules_str.split(',')
                new_workflow = ([], workflow_rules[-1])
                for workflow_rule in workflow_rules:
                    if ':' in workflow_rule:
                        condition, dest = workflow_rule.split(':')
                        operator = '>' if '>' in condition else '<'
                        operand, const = condition.split(operator)
                        new_workflow[0].append((operand, operator, int(const), dest))
                workflows[workflow_name] = new_workflow
            else:
                line_parts = line[1:-1].split(',')
                new_part = {}
                for line_part in line_parts:
                    name, val = line_part.split('=')
                    new_part[name] = int(val)
                parts.append(new_part)
    
    score = 0
    for part in parts:
        curr_workflow = 'in'
        while curr_workflow != 'R' and curr_workflow != 'A':
            for rule in workflows[curr_workflow][0]:
                operand, operator, const, dest = rule
                part_val = part[operand]
                if (operator == '<' and part_val < const) or (operator == '>' and part_val > const):
                    curr_workflow = dest
                    break
            else:
                curr_workflow = workflows[curr_workflow][1]
        
        if curr_workflow == 'A':
            score += part['x'] + part['m'] + part['a'] + part['s']
    print(score)


if __name__ == "__main__":
    main()

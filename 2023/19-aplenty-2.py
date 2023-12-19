def count_parts(workflows, ranges, curr_workflow, curr_workflow_step):
    if curr_workflow == 'A':
        xmas_ranges = [ranges[x][1] - ranges[x][0] + 1 for x in 'xmas']
        return xmas_ranges[0] * xmas_ranges[1] * xmas_ranges[2] * xmas_ranges[3]
    elif curr_workflow == 'R':
        return 0
    
    workflow = workflows[curr_workflow]
    
    if curr_workflow_step >= len(workflow[0]):
        return count_parts(workflows, ranges, workflow[1], 0)
    
    rule = workflow[0][curr_workflow_step]
    operand, operator, const, dest = rule
    range_min, range_max = ranges[operand]
    if (range_min > const and operator == '>') or (range_max < const and operator == '<'):
        # Entire range passes rule
        return count_parts(workflows, ranges, dest, 0)
    elif (range_max <= const and operator == '>') or (range_min >= const and operator == '<'):
        # Entire range fails rule
        return count_parts(workflows, ranges, curr_workflow, curr_workflow_step + 1)
    else:
        # Range must be split
        lower_ranges = dict(ranges)
        upper_ranges = dict(ranges)
        if operator == '<':
            lower_ranges[operand] = (ranges[operand][0], const - 1)
            upper_ranges[operand] = (const, range_max)
            return count_parts(workflows, lower_ranges, dest, 0) + count_parts(workflows, upper_ranges, curr_workflow, curr_workflow_step + 1)
        else:
            lower_ranges[operand] = (ranges[operand][0], const)
            upper_ranges[operand] = (const + 1, range_max)
            return count_parts(workflows, lower_ranges, curr_workflow, curr_workflow_step + 1) + count_parts(workflows, upper_ranges, dest, 0)


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
    
    ranges = { x: (1, 4000) for x in 'xmas' }
    score = count_parts(workflows, ranges, 'in', 0)
    print(score)


if __name__ == "__main__":
    main()

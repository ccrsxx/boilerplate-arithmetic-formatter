def arithmetic_arranger(problems, args=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    up = mid = down = solve = ''

    for i in range(len(problems)):
        problem = problems[i].split()
        
        fn = problem[0]
        op = problem[1]
        sn = problem[2]

        space = max(len(fn), len(sn))
        end_space = '    '

        if '+' not in op and '-' not in op:
            return "Error: Operator must be '+' or '-'."

        elif len(fn) > 4 or len(sn) > 4:
            return "Error: Numbers cannot be more than four digits."

        elif not fn.isdigit() or not sn.isdigit():
            return "Error: Numbers must only contain digits."

        else:
            up += fn.rjust(space + 2) + end_space
            mid += op + ' ' + sn.rjust(space) + end_space
            down += ('-' * (space + 2)) + end_space

        if args:
            fn, sn = int(fn), int(sn)

            if op == '+':
                sum = fn + sn
            else:
                sum = fn - sn

            solve += str(sum).rjust(space + 2) + end_space

    arranged_problems = up.rstrip() + '\n' + mid.rstrip()  + '\n' + down.rstrip() 
    
    if args:
        arranged_problems = up.rstrip()  + '\n' + mid.rstrip()  + '\n' + down.rstrip()  + '\n' + solve.rstrip() 

    return arranged_problems

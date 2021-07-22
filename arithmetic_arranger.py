def arithmetic_arranger(problems):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for i in range(len(problems)):
        prob = problems[i].split()
        
        fn = prob[0]
        op = prob[1]
        sn = prob[2]

        if '+' not in op and '-' not in op:
            return "Error: Operator must be '+' or '-'."

        elif len(fn) > 4 or len(sn) > 4:
            return "Error: Numbers cannot be more than four digits."

        elif not fn.isdigit() or not sn.isdigit():
            return "Error: Numbers must only contain digits."
        


# probs = ['1 + 2', '2 + 3', '3 + 4', '4 + 5', '5 + 6', '6 + 5']
probs = ['1 + 2', '2 + 3', '3 + 4', '4 + 5', '5 + 6']
check = arithmetic_arranger(probs)
print(check)

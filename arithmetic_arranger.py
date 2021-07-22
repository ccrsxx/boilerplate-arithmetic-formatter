def arithmetic_arranger(problems):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for num in problems:
        if '+' not in num and '-' not in num:
            return "Error: Operator must be '+' or '-'."


    return arranged_problems

# probs = ['1 + 2', '2 + 3', '3 + 4', '4 + 5', '5 + 6', '6 + 5']
probs = ['1 + 2', '2 + 3', '3 + 4', '4 + 5', '5 + 6']
check = arithmetic_arranger(probs)
print(check)
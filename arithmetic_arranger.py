def arithmetic_arranger(numbers, solve=False):

    up = mid = line = down = ''

    if len(numbers) > 5:
        return 'Error: Too many problems.'
    
    for num in numbers:

        slice = num.split()

        fn = slice[0]
        op = slice[1]
        sn = slice[2]

        if '+' not in op and '-' not in op:
            return 'Error: Operator must be \'+\' or \'-\'.'

        if not fn.isdigit() or not sn.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(fn) > 4 or len(sn) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        space = max(len(fn), len(sn)) + 2
        end_space = f'{"":4}'

        up += f'{fn:>{space}}{end_space}'
        mid += f'{op} {sn:>{space - 2}}{end_space}'
        line += f'{"":-^{space}}{end_space}'

        if solve:
            fn, sn = int(fn), int(sn)

            if op == '+':
                total = fn + sn
            else:
                total = fn - sn

            down += f'{total:>{space}}{end_space}'

    if solve:
        return f'{up.rstrip()}\n{mid.rstrip()}\n{line.rstrip()}\n{down.rstrip()}'

    return f'{up.rstrip()}\n{mid.rstrip()}\n{line.rstrip()}'

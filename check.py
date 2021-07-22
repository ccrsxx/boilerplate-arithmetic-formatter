def solver(nums):
    print(nums)
    return nums

data = []    

ask = input('Enter problem: ').strip()
data.append(ask)

if len(data) > 5:
    print('Error: Too many problems.')

for num in data:
    for c in ['+', '-']:
        if c not in num:
            print("Error: Operator must be '+' or '-'.")
        break

print(data)
# solver(data)
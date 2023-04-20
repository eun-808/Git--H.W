for i in range(1, 10):
    for j in range(2, 6):
        cal1 = j * i
        print(f'{j} x {i} = {cal1}'.ljust(14), end='')
        if j == 5 :
            print()
print()
for i in range(1, 10):
    for l in range(6, 10):
        cal2 = l * i 
        print(f'{l} x {i} = {cal2}'.ljust(14), end='')
        if l == 9 :
            print()
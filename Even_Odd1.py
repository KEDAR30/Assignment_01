num=int(input('Enter the number needed:'))
even_count=0
odd_count=0
for i in range(num):
    if not i%2==0:
        even_count+=1
    else:
        odd_count+=1
print('Total even number:',even_count)
print('Total odd number:',odd_count)


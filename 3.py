arr = [1, 3, 5, 6]
num = 0

for d in arr:
    num = num * 10 + d  


num += 1

result = []
while num > 0:
    result.insert(0, num % 10)
    num //= 10

print(result)  
# 2 вариант 
#arr = [1, 3, 5, 6]

#result = [int(x) for x in str(int("".join(map(str, arr))) + 1)]
#result=list(map(int,str(int("".join(map(str, arr))) + 1)))
#print(result)


class Solution:
    def twoSum(self,num,arg):
        for i in range(1, len(arg)):
            s = 0
            s += arg[i - 1] + arg[i]
            if s==num:
                g=[i-1,i]
                print(g)

#b=[1,2,3,4,5]


print('Введите цель')
a=int(input())
print('Введите количество элементов списка')
data=int(input())
b=[]
for i in range(data):
    print('Введите ',i,'элемент списка')
    b.append(int(input()))
p=Solution()
p.twoSum(a,b)



        
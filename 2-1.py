a=int(input())
b=a
f=b

if a>0:
    count=0
    while a>0:
        a=a//10
        count+=1
    print(count)
    g=0
    isa=0
    for i in range(count):
        g=b%10
        isa+=g*10**(count-i-1)
        b=b//10
    print(isa)
    if f==isa:
        print('true')
    else:
        print('false')
else:
    print('false')


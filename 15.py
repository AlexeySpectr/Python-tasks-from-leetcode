n=4
precision=1e-6
if n == 0:
    print(0)

x = n
while True:
    root = 0.5 * (x + n / x)
    if abs(x - root) < precision:
        break
    x = root
print(root)
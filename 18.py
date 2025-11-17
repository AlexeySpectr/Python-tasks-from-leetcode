s = "egg" 
t = "add"
print(len(set(s)) == len(set(zip(s, t))) == len(set(t)))
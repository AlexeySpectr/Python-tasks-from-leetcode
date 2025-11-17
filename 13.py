# s = "luffy is still joyboy"
# i = 0
# j = 0
# g = 0

# while i < len(s):
#     if s[i].isalpha():
#         j += 1
#     else:
#         if j > g:
#             g = j
#         j = 0
#     i += 1

# if j > g:
#     g = j

# print(g)

s = "luffy is still joyboy"
print(max(len(w) for w in s.split()))
a=s.split()
print(len(a[-1]))

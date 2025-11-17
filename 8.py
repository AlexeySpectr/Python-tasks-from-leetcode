s='()'
for i in range(len(s)):
    b=s.replace('{}', '').replace('[]', '').replace('()', '')
if b=='':
    print('true')
else:
    print('false')
    
    #2
    #  def isValid(self, s: str) -> bool:
    #         st = []  # создаём стек
    #     for i in s:
    #         if i == '[' or i == '{' or i == '(':  # открывающие скобки
    #             st.append(i)
    #         else:  # закрывающие скобки
    #             if not st:  # стек пуст, а скобка закрывающая
    #                 return False
    #             if i == ']' and st[-1] == '[':
    #                 st.pop()
    #             elif i == '}' and st[-1] == '{':
    #                 st.pop()
    #             elif i == ')' and st[-1] == '(':
    #                 st.pop()
    #             else:  # если скобка не совпадает
    #                 return False
    #     return not st  # возвращаем True, если стек пуст
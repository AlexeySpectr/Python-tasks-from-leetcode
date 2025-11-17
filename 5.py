a = "IV"
b = 0
i = 0

while i < len(a):
    match a[i:i+2]:   # берём два символа сразу
        case 'IV':
            b += 4
            i += 2
            continue
        case 'IX':
            b += 9
            i += 2
            continue
        case 'XL':
            b += 40
            i += 2
            continue
        case 'XC':
            b += 90
            i += 2
            continue
        case 'CD':
            b += 400
            i += 2
            continue
        case 'CM':
            b += 900
            i += 2
            continue
    
    # если не совпало — значит одиночный символ
    match a[i]:
        case 'I':
            b += 1
        case 'V':
            b += 5
        case 'X':
            b += 10
        case 'L':
            b += 50
        case 'C':
            b += 100
        case 'D':
            b += 500
        case 'M':
            b += 1000
    i += 1

print(b)



# 2 вариант def roman_to_int(roman: str) -> int:
#     values = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }

#     total = 0
#     prev_value = 0

#     for char in reversed(roman):  # идём справа налево
#         value = values[char]
#         if value < prev_value:
#             total -= value  # вычитание
#         else:
#             total += value  # сложение
#         prev_value = value
#     return total
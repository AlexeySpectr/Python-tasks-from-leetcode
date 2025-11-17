def longest_common_prefix(strs):
    if not strs:
        return ''
    
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return base[:i]
    return base

print(longest_common_prefix(["flower", "flow", "flight"]))
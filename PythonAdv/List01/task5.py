# longest common prefix of min 3 elements of the list of strings
def common_prefix(lst):
    if not lst:
        return ""
    lst = list(map(str.lower, lst))
    lst.sort()
    longest_prefix = ""
    for i in range(len(lst) - 2):
        prefix = ""
        for j in range(len(lst[i])):
            if lst[i][j] == lst[i + 1][j] == lst[i + 2][j]:
                prefix += lst[i][j]
            else:
                break
        if len(prefix) > len(longest_prefix):
            longest_prefix = prefix
    return longest_prefix

print(common_prefix(["Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]))


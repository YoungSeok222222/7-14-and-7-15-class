def duplicated_letters(words):
    result = [] 
    [word for word in words if words.count(word)> 1 and not (word in result or result.append(word))]
    return result
print(duplicated_letters('apple')) #=> ['p']
duplicated_letters('banana') # =>['a','n']

# result = []
# def duplicated_letters(words):
#     return [word for word in words if words.count(word) > 1 and not (word in result or result.append(word))]

# print(duplicated_letters('apple')) #=> ['p']
# print(duplicated_letters('banana')) # =>['a','n']










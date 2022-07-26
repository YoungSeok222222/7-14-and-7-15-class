
# def low_and_up(word):
#     new_str = ''
#     for idx, char in enumerate(word,start=1):
#         if idx % 2 ==1:
#             new_str += char.lower()  
#         else:
#             new_str += char.upper()

#     return new_str


# print(low_and_up('apple'))
# print(low_and_up('banana'))

####
def low_and_up2(word):
    new_str = [(char.lower() if idx %2 else char.upper()) for idx,char in enumerate(word,start = 1)]
    return ''.join(new_str)
print(low_and_up2('apple'))
print(low_and_up2('banana'))











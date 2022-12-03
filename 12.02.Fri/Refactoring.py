# Refactor 1
def split_and_sum(text):
    result = 0
    if text == "":
        result = 0
    else:
        values = text.split('-')
        for val in values :
            result += int(val)
    return result
ret = split_and_sum("11-22-33")
print(ret)
#=========================================

def split_and_sum(text):
    if text != "":
        values = list(map(int,text.split('-')))
        return sum(values)
    return 0
    
ret = split_and_sum("11-22-33")
# ret = split_and_sum("")
print(ret)

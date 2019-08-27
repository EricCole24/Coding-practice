#check to see if all characters are unique in a string
def unique(string):
    ele = set()
    for i in string:
        if i not in ele:
            ele.add(i)

        else:
            return False
    return True
#test cases
print(unique("Ericc"))
print(unique("Eric"))

import re

def variableName(name):
    if re.search(r"^[_A-Za-z][0-9_A-Za-z]*$", name):
        return True
    return False

if __name__ == '__main__':
    print(variableName("var_1__Int"))
    print(variableName("2w2"))
    print(variableName("qq-q"))
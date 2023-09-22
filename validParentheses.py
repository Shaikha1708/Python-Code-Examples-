#Check the input whether open brackets are closed by the same type of brackets.

def validParentheses(s):
    valid = False
    length = len(s)
    if length%2 == 0:
        for i in range(0,length,2):
            valid = False
            if s[i] == '(' and s[i+1] == ")":
                valid = True 
            elif s[i] == '[' and s[i+1] == "]":
                valid = True 
            elif s[i] == '{' and s[i+1] == "}":
                valid = True 
    return valid

def testReverseString():
    assert (validParentheses("()") == True)
    assert (validParentheses("[]") == True)
    assert (validParentheses("{}") == True)
    assert (validParentheses("(){}[]") == True)
    assert (validParentheses("()[}") == False)
    assert (validParentheses("{}}") == False)
    assert (validParentheses("[)") == False)
    print("Passed!")

print(validParentheses(""))
testReverseString()
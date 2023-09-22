#Function that will take a list input from the user 
#Return the reverse 
def reverseString(s):
    if type(s) == list:
        newString = list(reversed(s))
        return newString

#Test cases 
def testReverseString():
    assert (reverseString(['n', 'a', 'm', 'e']) == ['e', 'm', 'a', 'n'])
    assert (reverseString(['s', 'a', 'v', 'e']) == ['e', 'v', 'a', 's'])
    assert (reverseString(['S', 'c', 'h', 'o', 'o', 'l']) == ['l', 'o', 'o', 'h', 'c', 'S'])
    print("Passed!")


print(reverseString([]))
testReverseString()

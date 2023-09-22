#Check that the input is a Palinedrome Number 
#Palindrome Number: a number that reads the same backwards as forwards

def isPalindrome(num):
    num = str(num)
    valid = False
    if num == num[::-1]:
        valid = True 
    return valid 

def testIsPalindrome():
    assert(isPalindrome(212) == True)
    assert(isPalindrome(33) == True)
    assert(isPalindrome(0) == True)
    assert(isPalindrome(-212) == False)
    assert(isPalindrome(23) == False)
    print("Passed!")

print(isPalindrome(212)) #Change the number here
testIsPalindrome()
    
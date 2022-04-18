#Delara Daryaei
#This program validates credit card numbers


def isValid(number : int ) -> (str):
    '''call other functions to conirm validity of CC'''
    #Check digit length of CC num to confirm validity
    if not 13 <= len(number) <= 16:
        return False
    #Check first digit of CC num to confirm validity
    if ((number.startswith("4")==False)and(number.startswith("5")==False)and(number.startswith("6")==False)and(number.startswith("37")==False)):
        return False
    #Return true if the card number is valid
    return (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0
  
def sumOfDoubleEvenPlace(cardNumber : str) -> (int):
    '''sum the double even place digits from right to left and return'''
    result = 0
    
    for i in range(len(cardNumber) - 2, -1, - 2):
        result += getDigit(int(cardNumber[i]) * 2)
    
    return result
  

def getDigit(number : int) -> (int):
    '''Check for sumOfDoubleEvenPlace if even place digit is 1 of 2 digits'''
    #if single digit return if doulbe get sum of 2 digits and return
    return number % 10 + (number // 10 % 10)
  
  
def sumOfOddPlace(cardNumber : str) -> (int):
    '''sum the digits of the odd place and return'''
    result = 0

    for i in range(len(cardNumber) - 1, -1, -2):
        result += int(cardNumber[i])
    
    return result


def main():
    num = input("How many credit card numbers do you want to check? ")
    for i in range(0, int(num)):
        cardNumber = input ("\nEnter credit card number: ")
        if isValid(cardNumber):
            print(cardNumber, 'is valid')
        else:
            print(cardNumber, 'is invalid')


if __name__=="__main__":
    main()


##Test Run 1
##How many credit card numbers do you want to check? 2
##
##Enter credit card number: 4388576018402626
##4388576018402626 is invalid
##
##Enter credit card number: 4388576018410707
##4388576018410707 is valid
    
##Test Run 2
##How many credit card numbers do you want to check? 0
##

##Test Run 3
##How many credit card numbers do you want to check? 3
##
##Enter credit card number: 12345678
##12345678 is invalid
##
##Enter credit card number: 5169769005222217
##5169769005222217 is valid
##
##Enter credit card number: 6011655276746808
##6011655276746808 is invalid
    
##Test Run 4
##How many credit card numbers do you want to check? 2
##
##Enter credit card number: 5876799087666
##5876799087666 is invalid
##
##Enter credit card number: 379327498471832
##379327498471832 is invalid

##Test Run 5
##How many credit card numbers do you want to check? 3
##
##Enter credit card number: 62381203912129
##62381203912129 is invalid
##
##Enter credit card number: 37120390124810238
##37120390124810238 is invalid
##
##Enter credit card number: 5511115286120289
##5511115286120289 is valid

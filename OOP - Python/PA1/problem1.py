# Amandeep Singh 145003464
def palindrome(N): #function which returns true if a number is palindrome
    isPalindrome=str(N) == str(N)[::-1]  #if string of number is same as reverse string of number
    return isPalindrome
    
def reverse_int(N): #function returns reverse of a number
    reverseNumString=str(N)[::-1] #reversing a number
    reverseNumInt=int(reverseNumString)
    return reverseNumInt

def palindrome_generator(): #inputs a number, checks if palindrome, if not generates one from it
    print('The Palindrome Generator')
    choice='y' #starting choice
    while(choice=='y' or choice=='Y'): # run till user enters y
        N=int(input('Enter a positive integer : '))
        isPalindrome=palindrome(N) #check if palindrome
        if(isPalindrome):
            print('Entered Number is palindrome')
        else:
            print('Entered Number is not palindrome')
            print('Generating a Palindrome')
            numIterations=0 #to count iterations to generate palindrome
            while(not(palindrome(N))):
                N=N+reverse_int(N) #reverse the number using the defined function
                print(N)
                numIterations=numIterations+1
            print(str(numIterations)+' iterations were needed to generate a palindrome')
        choice=input('Do it again? [y/n] : ') #ask user if he wants to continue
    print('Goodbye !')
            

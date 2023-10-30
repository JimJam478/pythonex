def fizzbizz(n):
    for i in range (1,n+1):
        if i % 15 == 0:
            print('fizzbizz')
        elif i%5 ==0:
            print('buzz')
        elif i%3 == 0:
            print('fizz')
        else:
            print(i)

n = int(input('Enter upperlimit: '))
fizzbizz(n)

def pallindrome(s):
    string = s
    reverse = s[::-1]
    if (string == reverse):
        print('True')
    else:
        print('False')

s = input('Enter the string: ')
pallindrome(s)
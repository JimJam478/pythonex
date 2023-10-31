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

def palindrome(s):
    return s == s[::-1]
    
import collections
def panagram(s):
    s = s.lower()
    count = collections.Counter(s)
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True
 
def freq(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count 

def main():
    print(fizzbizz(100))
    print(palindrome('abba'))
    print(panagram("abcdefghijklmnopqrstuvwxyz"))
    print(freq('dfsdfdsfadsf dsfadfdf'))

if __name__ == '__main__':
    main()
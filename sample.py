"'this is sample of creating module'"

def Is_perfect(n):
    fc=0
    for i in range(1,n):
        if(n%i==0):
            fc+=i
    if(fc==n):
            return True 
    else:
            return False


def perfect_gen(start,end):
    for i in range(start,end+1):
        if Is_perfect(n): 
            print(i,end = ' ')
start=int(input('enter the number:'))
end=int(input('enter the number:'))



def Is_Prime(n):
    if n == 1:
        return False
    cnt = 0
    for i in range(2,n):
        if n%i == 0:
            cnt+=1
            break
    if cnt == 0:
         return True
    else:
         return False


def prime(m,n):
    for i in range(m,n+1): 
        if Is_Prime(i):
            print(i)
m=int(input('enter the value:'))
n=int(input('enter the value:'))



def Is_Even(n):
    if n%2==0:
        return True
    else:
        return False
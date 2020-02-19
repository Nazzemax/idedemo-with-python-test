def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

#Calculation FIonacci number
result = fibo(10)
print('fibo(10=)' + str(result))
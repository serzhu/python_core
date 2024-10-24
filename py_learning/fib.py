def fibonacci(n):
    value = [0,1]
#    print(value[0])
#    print(value[1])
    if n == 0:
        return value[0]
    elif n == 1:
        return value[1]
    else:
        for i in range (2,n+1):
            x = value[i-2] + value[i-1]
            value.append(x)
            
        
        return value

print(fibonacci(20))
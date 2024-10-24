result = None
operand = None
operator = None
wait_for_number = True

data = []

while True:
    while wait_for_number:
        wait_for_operator = True
        if operator == '=':
            break
        operand = input(">>> ")
        try:
            float(operand)
            data.append(operand)
            result = str(eval(' '.join(data)))
            data.clear()
            data.append(result)
            print(data)
            print(result)
            while wait_for_operator:
                operator = input(">>> ")
                if operator == '=':
                    break
                elif operator in ('+', '-', '/', '*'):
                    wait_for_operator = False
                    data.append(operator)
                    print(data)
                else:
                    print (f"{operator} is not '+' or '-' or '/' or '*'. Try again")                   
        except ValueError:
            print ('not a number')
    result = float(result)
    print(result)
    break
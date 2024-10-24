message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    ch_num = ord(ch)
    if ch_num >=65 and ch_num<=90:
        pos = ord(ch) - ord('A')  
        pos = (pos + offset) % 26  
        new_char = chr(pos + ord("A"))
    elif ch_num >=97 and ch_num<=122:
        pos = ord(ch) - ord('a')  
        pos = (pos + offset) % 26  
        new_char = chr(pos + ord("a"))
    else:
        new_char = ch
    encoded_message = encoded_message + new_char
    #print (new_char, end='')
print(encoded_message)
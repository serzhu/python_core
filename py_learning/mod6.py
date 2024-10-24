with open('credent.bin', 'wb') as fh:
    users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
    line = ''
    for key,value in users_info.items():
        fh.write(bytes(f'{key}:{value}\n', 'utf-8'))
#        line = line + (key + ':' + value + '\n')
#    line = line.rstrip('\n')
#    b_line = line.encode('utf8')
#    print(type(b_line))
#    print(b_line)
#    fh.write(b_line)
with open('credent.bin', 'r') as fh1:
    line = fh1.read()
    print(line)

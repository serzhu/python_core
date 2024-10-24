def encode(data):

    for i in range(len(data)):
        print(len(data), i)
        if i == len(data)-1:
            return [data[i]] + [i+1]
        elif data[i] != data[i+1]:
            #print([data[i]] + [i+1])
            return [data[i]] + [i+1] + encode(data[i+1:])


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z"]))

# encode(["X", 3, "Z", 2, "X", 2]) = [X] [X] [X] + decode([Z 2 X 2]) =
#                                    [X] [X] [X] + ([Z] [Z] + decode([X 2])) =
#                                    [X] [X] [X] + [Z] [Z] + ([X] [X] + decode([]))
# encode(["X", "X", "X", "Z", "Z", "X", "X"]) = [X]+[3] + encode(["Z", "Z", "X", "X"]) =
#                                               [X]+[3] + [Z]+[2] + encode(["X", "X"]) =
#                                               [X]+[3] + [Z]+[2] + [X]+[2] + encode([])
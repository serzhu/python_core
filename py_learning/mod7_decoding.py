def decode(data):
    if data == []:
        return []
    return data[0].split()*data[1] + decode(data[2:])


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

# decode(["X", 3, "Z", 2, "X", 2]) = [X] [X] [X] + decode([Z 2 X 2]) =
#                                    [X] [X] [X] + ([Z] [Z] + decode([X 2])) =
#                                    [X] [X] [X] + [Z] [Z] + ([X] [X] + decode([]))
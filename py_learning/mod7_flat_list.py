def flatten(data):
    
    if data == []:
        return []

    for el in data:
        if not isinstance(el,list):
            list1 = []
            list1.append(el)
            data.remove(el)
            list2 = flatten(data)
            return list1+list2
        else:
            list1 = flatten(el)
            data.remove(el)
            list2 = flatten(data)
            return list1+list2



print(flatten([1, [2]]))
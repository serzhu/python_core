import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
list1 = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
list2 = [
        {"nickname": "Mick", "age": 5, "owner": "Sara"},
        {"nickname": "Barsik", "age": 7, "owner": "Olga"},
        {"nickname": "Simon", "age": 3, "owner": "Yura"},
        ]



def convert_list(cats):
    c = []
    if isinstance(cats[0], dict):
        for item in cats:
            c.append(Cat(item['nickname'],item['age'],item['owner']))
        return c
    else:
        
        for item in cats:
            d = {}
            d['nickname'] = item.nickname
            d['age'] = item.age
            d['owner'] = item.owner
            c.append(d)
        return c


print(convert_list(list2))
print(convert_list(list1))
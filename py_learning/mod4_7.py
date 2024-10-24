points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

coordinates = [0, 1, 3, 2, 0]

def calculate_distance(coordinates):

    distance = 0
    i = 0
    for i in range (len(coordinates)-1):
        list = []
        list.append(coordinates[i]) 
        list.append(coordinates[i+1])
        list.sort()
        coord = tuple(list)
        for key, val in points.items():
            if key == coord:
                distance = distance +  val  

    return distance

print(calculate_distance(coordinates))


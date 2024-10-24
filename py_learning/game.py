from random import randint, choice

SIZE_N = 10
SIZE_M = 10

def check_state(objects):
    for obj in objects:
        if obj['type'] == 'char':
            char = obj
        elif obj['type'] == 'portal':
            win_condition = char['x'] == obj['x'] and char['y'] == obj['y']
            if win_condition:
                obj['sign'] = 'W'
                print(f'You WON in {turns} turns')
                break
        elif obj['type'] == 'enemy':
            loss_condition = char['x'] == obj['x'] and char['y'] == obj['y']
            if loss_condition:
                obj['sign'] = 'L'
                print(f'You LOST in {turns} turns')
                break

    return  win_condition or loss_condition

def generate_enemies(count):
    enemies = []
    for i in range(count):
        enemy = {'x': randint(0, SIZE_N - 1),
                'y': randint(0, SIZE_M - 1),
                'sign': 'E',
                'type': 'enemy'}
        enemies.append(enemy)
    return enemies

def generte_map(objects, size_n=SIZE_N, size_m=SIZE_M):
    world_map = []

    for j in range(size_m):
        row = []
        for i in range(size_n):
            row.append('_')
        
        world_map.append(row)
    
    for obj in objects:
        world_map[obj['y']][obj['x']] = obj['sign']    
    
    return world_map      
        
def move(direction, obj, size_n=SIZE_N, size_m=SIZE_M):
    if direction == 'w' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 's' and obj['y'] < size_m - 1:
        obj['y'] += 1
    elif direction == 'a' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 'd' and obj['x'] < size_n - 1:
        obj['x'] += 1

def print_map(world_map):
    for row in world_map:
        print(f'|{"|".join(row)}|')

char = {'x': randint(0, SIZE_N - 1),
        'y': randint(0, SIZE_M - 1),
        'sign': 'X',
        'type': 'char'}

portal = {'x': randint(0, SIZE_N - 1),
          'y': randint(0, SIZE_M - 1),
          'sign': 'O',
          'type': 'portal'}

enemies = generate_enemies(5)
objects = [char, portal] + enemies
print(objects)
turns = 0

while True:

    end_flag = check_state(objects)    
    world_map = generte_map(objects)
    print_map(world_map)

    if end_flag:
        break
    for obj in objects:
        direction = ''
        if obj['type'] == 'char':
            direction = input('Enter dirction: ')
        elif obj['type'] == 'enemy':
            direction = choice('wasd')
        move(direction, obj)

    turns += 1    
    
from collections import deque
import random
import sys

size = 5 # Size of board 
snake_positions = deque([(1,1)])  # Positions of snake body
food_positions = []

def print_matrix(size):
    [print('-', end=" ") for i in range(size)]
    print('\b')
    for i in range(size-1):
        for j in range(size+1):
            if j == 0:
                print('|', end=" ")
            elif j == size:
                print('|', end="\n")
            elif (i+1,j) in  snake_positions:
                if (i+1,j) == snake_positions[-1]:
                    print('#', end=" ")
                else:
                    print('*', end=" ")
            elif (i+1,j) in  food_positions:
                print(':', end=" ")
            else:
                print(" ",end=" ")
    [print('-', end=" ") for _ in range(size)]
    print('\n')

def move_snake(direction):
    top = snake_positions[-1]
    if direction == 'left':
        snake_positions.append((top[0], top[1]-1 if top[1] != 1 else size-1))
    elif direction == 'right':
        snake_positions.append((top[0], top[1]+1 if top[1] != size-1 else 1))
    elif direction == 'up':
        snake_positions.append((top[0]-1 if top[0] != 1 else size-1, top[1]))
    elif direction == 'down':
        snake_positions.append((top[0]+1 if top[0] != size-1 else 1, top[1]))
    if top in food_positions:
        food_positions.pop()
    elif top not in food_positions:
        snake_positions.popleft()
    if len(set(snake_positions)) != len(snake_positions):
        print('Game over')
        sys.exit(0)


def add_food():
    if len(food_positions) == 0:
        food_positions.append((random.randint(1,size-1), random.randint(1,size-1)))

direction_map = {
    'A': 'left',
    'W': 'up',
    'D': 'right',
    'S': 'down',
}
while True:
    add_food()
    print_matrix(size)
    direction = input('Enter direction')
    if direction == 'q':
        break
    move_snake(direction_map[direction.strip().capitalize()])
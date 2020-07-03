

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

visited_pos = []

def solve(bo):    
    next_pos = find_empty(bo)
    # print(next_pos)
    if next_pos is None:
        print("b")
        return
    else:
        pos_x, pos_y = next_pos
        for num in range(1,10):
            if valid(bo, 3, next_pos):
                print("a")
                bo[pos_x][pos_y] = num
                visited_pos.append((pos_x,pos_y))            
                solve(bo)
        # print(visited_pos[-1])
        # x_last, y_last = visited_pos[-1]
        # bo[x_last][y_last] = 0
        # visited_pos.pop(-1)
        return

def valid(bo, num, pos):  # pos: (i,j) row, col
    # check row
    for j in range(len(bo[pos[0]])):
        if num == bo[pos[0]][j] and j != pos[1]:
            return False
    # check col
    for i in range(len(bo[pos[1]])):
        if num == bo[i][pos[1]] and i != pos[0]:
            return False
    # check cube, which box //3
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    index_x = 3 * box_x
    index_y = 3 * box_y
    for i in range(index_x, index_x+3):
        for j in range(index_y, index_y+3):
            if num == bo[i][j] and pos != (i,j):
                return False    

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:  # change line
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
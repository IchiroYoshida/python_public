import time

maze_map = """
************************************************************
*..........................................................*
*****.***********.********...********************.**********
*.***.*............**......**..******************.*...******
*.*******.***.****.**.********.....***......*****.*.*.....**
*.........*...**...**.************.***.....******...*****.**
***.*****...****.****.****..******.*****.****************..*
*e..******.......*........................................s*
************************************************************
"""

basic_operations = 0


def main():
    maze =  maze_map.strip().split('\n')
    start = findStart(maze)
    end = findEnd(maze)

    startTime = time.time()
    path = BFS(maze, start, end)
    endTime = time.time()

    if path == None:
        printMaze(maze)
        print("No path to destination.")
    else:
        printPath(maze, path)
        print("Shortest path: ")
        print(path)

    print("Time taken:", endTime-startTime, "secs")
    print("Basic operations: ", basic_operations)
    print("\n")


def BFS(maze, start, end):
    '''"BFS:Breadth first Search"
    :param maze(list): the maze to be navigated
    :param start(tuple): the starting coordinates (row, col)
    :param end(tuple): the end coordinates (row, col)
    :return: shortest path from start to end
    '''
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]  # Required due to a quirk with tuples in Python
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == end:
            return path
        elif front not in visited:
            for adjacentSpace in getAdjacentSpaces(maze, front, visited):
                newPath = list(path)
                newPath.append(adjacentSpace)
                queue.append(newPath)
                global basic_operations
                basic_operations += 1
            visited.add(front)
    return None


def getAdjacentSpaces(maze, space, visited):
    ''' Returns all legal spaces surrounding the current space
    :param space: tuple containing coordinates (row, col)
    :return: all legal spaces
    '''
    spaces = list()
    spaces.append((space[0]-1, space[1]))  # Up
    spaces.append((space[0]+1, space[1]))  # Down
    spaces.append((space[0], space[1]-1))  # Left
    spaces.append((space[0], space[1]+1))  # Right

    print("spaces =",spaces)

    final = list()
    for i in spaces:
        if maze[i[0]][i[1]] != '*' and i not in visited:
            final.append(i)
    return final


def findStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 's':
                return tuple([i, j])
    return None


def findEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'e':
                return tuple([i, j])
    return None

def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end="")
        print()


def printPath(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if tuple([i, j]) in path and maze[i][j] != 's' and maze[i][j] != 'e':
                print("x", end="")
            else:
                print(maze[i][j], end="")
        print()


if __name__ == "__main__":

    main()

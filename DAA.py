import heapq
import matplotlib.pyplot as plt
import numpy as np

def dijkstra(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    distances = {start: 0}
    parents = {start: None}
    pq = [(0, start)]  # Priority queue (distance, node)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == 0:
                new_distance = current_distance + 1  # All edges have weight = 1
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = current
                    heapq.heappush(pq, (new_distance, neighbor))

    return None  # No path found

# Example maze (0 = open, 1 = obstacle)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Solve the maze
path = dijkstra(maze, start, goal)

# Visualization
if path:
    for x, y in path:
        maze[x][y] = 2
    print("Path found:", path)
else:
    print("No path found.")

# Display the maze
plt.imshow(maze, cmap="hot", interpolation="nearest")
plt.title("Maze with Dijkstra's Path")
plt.show()
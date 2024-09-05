import heapq

def load_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    matrix = []
    for line in lines:
        # Convert each line to a list of integers
        row = list(map(int, line.strip().split(',')))
        matrix.append(row)
    return matrix

def find_minimal_path_sum(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    
    # Priority queue for BFS (min-heap)
    pq = []
    
    # Initialize the priority queue with the top-left cell
    heapq.heappush(pq, (matrix[0][0], 0, 0))  # (cost, row, col)
    
    # Cost matrix to track minimum path cost to each cell
    min_cost = [[float('inf')] * m for _ in range(n)]
    min_cost[0][0] = matrix[0][0]
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        current_cost, x, y = heapq.heappop(pq)
        
        # If we reached the bottom-right corner, return the cost
        if x == n - 1 and y == m - 1:
            return current_cost
        
        # Explore adjacent cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = current_cost + matrix[nx][ny]
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    return float('inf')  # In case no path is found

# Load the matrix and find the minimal path sum
file_path = '83_input.txt'
matrix = load_matrix(file_path)
minimal_path_sum = find_minimal_path_sum(matrix)
print(f"The minimal path sum from the top-left to the bottom-right is: {minimal_path_sum}")

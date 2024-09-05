import heapq

def load_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    matrix = []
    for line in lines:
        row = list(map(int, line.strip().split(',')))
        matrix.append(row)
    return matrix

def find_minimal_path_sum(matrix):
    n = len(matrix)
    
    # Priority queue for BFS (min-heap)
    pq = []
    
    # Initialize the priority queue with all cells in the first column
    for i in range(n):
        heapq.heappush(pq, (matrix[i][0], i, 0))  # (cost, row, col)
    
    # Cost matrix to track minimum path cost to each cell
    min_cost = [[float('inf')] * n for _ in range(n)]
    
    # Fill the initial column costs
    for i in range(n):
        min_cost[i][0] = matrix[i][0]
    
    while pq:
        current_cost, x, y = heapq.heappop(pq)
        
        # If we reached the last column, check the minimum cost
        if y == n - 1:
            return current_cost
        
        # Explore adjacent cells (right, up, down)
        for dx, dy in [(-1, 0), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = current_cost + matrix[nx][ny]
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    return float('inf')  # In case no path is found

# Load the matrix and find the minimal path sum
file_path = 'matrix.txt'
matrix = load_matrix(file_path)
minimal_path_sum = find_minimal_path_sum(matrix)
print(f"The minimal path sum from the left column to the right column is: {minimal_path_sum}")

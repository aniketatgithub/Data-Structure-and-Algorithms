def minMoves(n, startRow, startCol, endRow, endCol):
    """
    Calculates the minimum number of moves needed by a knight to move from a starting position to an ending position on a chess board.

    Args:
        n: The width and height of the square board.
        startRow: The row of the starting location.
        startCol: The column of the starting location.
        endRow: The row of the target location.
        endCol: The column of the target location.

    Returns:
        The minimum number of moves required, or -1 if it is not possible to reach the target location.
    """

    # Check if the starting and ending positions are within the bounds of the chess board.
    if startRow < 0 or startRow >= n or startCol < 0 or startCol >= n or endRow < 0 or endRow >= n or endCol < 0 or endCol >= n:
        return -1

    # Create a queue to store the positions that need to be explored.
    queue = [(startRow, startCol, 0)]

    # Mark the starting position as visited.
    visited = set()
    visited.add((startRow, startCol))

    # While the queue is not empty, continue exploring the positions.
    while queue:
        # Get the current position from the queue.
        row, col, distance = queue.pop(0)

        # If the current position is the ending position, return the distance.
        if row == endRow and col == endCol:
            return distance

        # Try all possible moves from the current position.
        for move in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            new_row = row + move[0]
            new_col = col + move[1]

            # If the new position is within the bounds of the chess board and has not been visited, add it to the queue.
            if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, distance + 1))
                visited.add((new_row, new_col))

    # If the ending position is not reachable, return -1.
    return -1

n = 6
startRow = 5
startCol = 1
endRow = 0
endCol = 5

# Calculate the minimum number of moves required.
min_moves = minMoves(n, startRow, startCol, endRow, endCol)

# Print the minimum number of moves.
print(min_moves)
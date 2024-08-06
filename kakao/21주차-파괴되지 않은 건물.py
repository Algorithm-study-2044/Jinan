def solution(board, skills):
    for skill in skills:
        type, r1, c1, r2, c2, degree = skill
        if type == 1:
            degree *= -1
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += degree
                
    return sum([point > 0 for row in board for point in row])
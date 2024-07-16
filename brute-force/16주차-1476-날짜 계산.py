def find_year(E, S, M):
    year = 1
    e, s, m = 1, 1, 1
    
    while (e != E) or (s != S) or (m != M):
        e += 1
        s += 1
        m += 1
        year += 1
        
        if e > 15:
            e = 1
        if s > 28:
            s = 1
        if m > 19:
            m = 1
    
    return year

# 입력 받기
E, S, M = map(int, input().split())

# 결과 출력
print(find_year(E, S, M))
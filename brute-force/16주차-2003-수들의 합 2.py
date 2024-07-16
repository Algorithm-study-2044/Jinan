def count_subarrays_with_sum(N, M, A):
    start, end = 0, 0
    current_sum = 0
    count = 0

    while end < N:
        # 현재 부분 배열의 합이 M보다 작으면 end 포인터를 증가시키고 합을 업데이트
        if current_sum < M:
            current_sum += A[end]
            end += 1
        # 현재 부분 배열의 합이 M과 같으면 count를 증가시키고 end 포인터를 증가
        elif current_sum == M:
            count += 1
            current_sum += A[end]
            end += 1
        # 현재 부분 배열의 합이 M보다 크면 start 포인터를 증가시키고 합을 업데이트
        else:
            current_sum -= A[start]
            start += 1
        
        # 부분 배열의 합이 M과 같으면 count를 증가
        if current_sum == M:
            count += 1

    return count

# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
print(count_subarrays_with_sum(N, M, A))
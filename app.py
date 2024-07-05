def solution(A, F, M):
    N = len(A)
    total_rolls = N + F
    total_sum_needed = M * total_rolls
    current_sum = sum(A)
    missing_sum = total_sum_needed - current_sum
    
    if missing_sum < F or missing_sum > 6 * F:
        return [0]
    
    result = [1] * F
    remaining_sum = missing_sum - F
    
    for i in range(F):
        if remaining_sum == 0:
            break
        add = min(5, remaining_sum)
        result[i] += add
        remaining_sum -= add
    
    return result

A1, F1, M1 = [3, 2, 4, 3], 2, 4
print(solution(A1, F1, M1))  

A2, F2, M2 = [1, 5, 6], 4, 3
print(solution(A2, F2, M2))  

# A3, F3, M3 = [1, 2, 3, 4], 4, 6
# print(solution(A3, F3, M3)) 

# A4, F4, M4 = [6, 2], 1, 1
# print(solution(A4, F4, M4))
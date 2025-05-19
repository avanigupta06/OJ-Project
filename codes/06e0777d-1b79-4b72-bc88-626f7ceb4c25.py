def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        pop = x % 10
        x //= 10
        
        # Check for overflow before actually appending the digit
        if (result > INT_MAX // 10) or (result == INT_MAX // 10 and pop > INT_MAX % 10):
            return 0
        
        result = result * 10 + pop
    
    return sign * result
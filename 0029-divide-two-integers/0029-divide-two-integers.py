class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # INT_MAX = 2**31 - 1
        # INT_MIN = -2**31

        # if dividend == INT_MIN and divisor == -1:
        #     return INT_MAX

        # negative = (dividend < 0) != (divisor < 0)
        # dividend = abs(dividend)
        # divisor = abs(divisor)

        # quotient = 0
        # while dividend >= divisor:
        #     temp = divisor
        #     multiple = 1
            
        #     while (temp << 1) <= dividend:
        #         temp <<= 1
        #         multiple <<= 1

        #     dividend -= temp
        #     quotient += multiple

        #     if negative:
        #         quotient = -quotient
            
        #     return quotient
       
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
    
    # Handle the overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
    # Determine the result's sign using XOR
        is_negative = (dividend < 0) ^ (divisor < 0)
    
    # Work with positive numbers using standard absolute value
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
    
        quotient = 0
    
    # Exponential subtraction loop using bitwise shifts
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            num_shifts = 0
        
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1
            
            abs_dividend -= temp_divisor
            quotient += (1 << num_shifts)
        
    # Apply the negative sign without using multiplication (*)
        if is_negative:
            return -quotient
        
        return quotient


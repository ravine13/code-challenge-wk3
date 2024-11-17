

#1. Large Power
def large_power(base, exponent):
    result = base ** exponent  
    if result > 5000:
        return True
    else:
        return False

#Divisible By Ten
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Testing large_power
print(large_power(20, 3))  
print(large_power(5, 5))   

# Testing divisible_by_ten
print(divisible_by_ten(50))  
print(divisible_by_ten(43))  

# This code uses efficient method to test and find prime numbers in a given range of numbers. 
def primeNumbersCalculator(num):
    prime = [2]
    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in prime:
            if number % factor == 0:
                break
            if factor > sqrtNum:
                prime.append(number) 
                break  
    return prime
        
# Calling the function
print(f'{primeNumbersCalculator(57)}')

def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2
    return factors

num = int(input("Enter a number: "))
factors = prime_factors(num)
print(f"Prime factors of {num} are: {factors}")
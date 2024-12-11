def generate_primes(limit):
    primes = [2, 3]  
    candidate = 4  
    while len(primes) < limit:
        is_prime = True
        for p in primes:
            if candidate % p == 0:  
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)  
        candidate += 1

    return primes
n = int(input("How many primes do you want? "))
print(generate_primes(n))

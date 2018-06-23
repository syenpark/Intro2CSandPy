def genPrimes():
    primes = [2]
    is_prime = True
    x = primes[0]
    
    while True:
        if is_prime:
            yield primes[-1]
        
        x += 1
        
        for p in primes:
            if not (x % p):
                is_prime = False
                break
            else:
                is_prime = True
                
        if is_prime:
            primes.append(x)

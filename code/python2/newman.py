factorial_memo = {0:1}

def factorial(n):
    try:
        return factorial_memo[n]
    except KeyError:
        return n * factorial(n-1)

def choose(N, k):
    return factorial(N) / factorial(k) / factorial(N-k)

def canonical_ensemble1(Q, p):
    N = len(Q)-1
    sum = 0

    for n, qn in enumerate(Q):
        pn = choose(N, n) * p**n * (1-p)**(N-n)
        print n, pn, qn
        sum += pn * qn
        
    return sum

    

def canonical_ensemble2(Q, p):
    N = len(Q)-1
    choose = 1
    sum = 0
    prod1 = 1
    prod2 = (1-p) ** N

    for n, qn in enumerate(Q):
        pn = choose * prod1 * prod2
        print n, pn, qn
        sum += pn * qn
        
        # update choose for the next iteration
        prod1 *= p
        prod2 /= (1-p)
        choose *= (N-n)
        choose /= (n+1)

    return sum

print canonical_ensemble1([0.0, 0.1, 0.2, 0.3], 0.25)
print canonical_ensemble2([0.0, 0.1, 0.2, 0.3], 0.25)

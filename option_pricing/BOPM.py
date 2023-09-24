import math

def american_call(T, S, K, r, sigma, q, n):
    deltaT = T / n
    up = math.exp(sigma * math.sqrt(deltaT))
    p0 = (up * math.exp(-r * deltaT) - math.exp(-q * deltaT)) / (up * up - 1)
    p1 = math.exp(-r * deltaT) - p0

    for i in range(n + 1):
        S_T = S * math.pow(up, 2 * i - n)
        if S_T - K > 0:
            V_T = S_T - K
        else:
            V_T = 0

    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            S_T = S * math.pow(up, 2 * i - j)
            V_T = p0 * V_T + p1 * V_T
            if S_T - K > 0:
                V_T = max(S_T - K, V_T)
            else:
                V_T = 0
    
    return V_T

def american_put(T, S, K, r, sigma, q, n):
    deltaT = T / n
    up = math.exp(sigma * math.sqrt(deltaT))
    p0 = (up * math.exp(-r * deltaT) - math.exp(-q * deltaT)) / (up * up - 1)
    p1 = math.exp(-r * deltaT) - p0

    for i in range(n + 1):
        S_T = S * math.pow(up, 2 * i - n)
        if K - S_T > 0:
            V_T = K - S_T
        else:
            V_T = 0

    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            S_T = S * math.pow(up, 2 * i - j)
            V_T = p0 * V_T + p1 * V_T
            if K - S_T > 0:
                V_T = max(K - S_T, V_T)
            else:
                V_T = 0
    
    return V_T


import math

def f(t, y):
    return 2 * y

def solucionExacta(t):
    return math.exp(2 * t)

t = 0.0
y_euler = 1.0
h = 0.2

print(f"{'t':<6} | {'Euler':<10} | {'Exacta':<10} | {'Error':<10}")
print("-" * 44)

for _ in range(6):
    exacta = solucionExacta(t)
    error = abs(exacta - y_euler)
    print(f"{t:<6.1f} | {y_euler:<10.4f} | {exacta:<10.4f} | {error:<10.4f}")
    
    y_euler = y_euler + h * f(t, y_euler)
    t = round(t + h, 1)
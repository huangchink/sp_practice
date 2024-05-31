import sympy as sp

# Coordinates for points P and Q
x0, y0, x1, y1 = sp.symbols('x0 y0 x1 y1')
# Distance formula
distance_PQ = sp.sqrt((x0 - x1)**2 + (y0 - y1)**2)

# Expression for (a + b + c)^2
a, b, c = sp.symbols('a b c')
expanded_expression = sp.expand((a + b + c)**2)
# Substitute a = 1, b = 2, c = 3
expanded_substituted = expanded_expression.subs({a: 1, b: 2, c: 3})

# Circumference formula
r = sp.symbols('r')
circumference = 2 * sp.pi * r

print("計算線段 PQ 的長度公式:", distance_PQ)
print("展開 (a + b + c)^2 的公式:", expanded_expression)
print("帶入 a = 1, b = 2, c = 3 計算結果:", expanded_substituted)
print("計算圓周長的公式:", circumference)

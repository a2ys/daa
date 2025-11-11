def karatsuba(num1, num2):
   if num1 < 10 and num2 < 10:
       return num1 * num2

   n = max(len(str(num1)), len(str(num2)))
   mid = n // 2

   a = num1  // (10 ** mid)
   b = num1 % (10 ** mid)
   c = num2 // (10 ** mid)
   d = num2 % (10 ** mid)

   p1 = karatsuba(a, c)
   p2 = karatsuba(b, d)
   p3 = karatsuba(a + b, c + d)

   middle = p3 - p1 - p2

   return p1 * (10 ** (2 * mid)) + middle * (10 ** mid) + p2

print(karatsuba(100, 12))


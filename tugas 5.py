print("============= NOT =============")
a = True
c = not a
print("a adalah", a)
print("------ c = not a ------")
print("c adalah", c)

print("\n============= OR =============")
a = True; b = True
c = a or b
print(a, "OR", b, "menjadi", c)

a = True; b = False
c = a or b
print(a, "OR", b, "menjadi", c)

a = False; b = True
c = a or b
print(a, "OR", b, "menjadi", c)

a = False; b = False
c = a or b
print(a, "OR", b, "menjadi", c)

print("\n============= AND =============")
a = True; b = True
c = a and b
print(a, "AND", b, "menjadi", c)

a = True; b = False
c = a and b
print(a, "AND", b, "menjadi", c)

a = False; b = True
c = a and b
print(a, "AND", b, "menjadi", c)

a = False; b = False
c = a and b
print(a, "AND", b, "menjadi", c)

print("\n============= XOR =============")
a = True; b = True
c = a ^ b
print(a, "^", b, "menjadi", c)

a = True; b = False
c = a ^ b
print(a, "^", b, "menjadi", c)

a = False; b = True
c = a ^ b
print(a, "^", b, "menjadi", c)

a = False; b = False
c = a ^ b
print(a, "^", b, "menjadi", c)

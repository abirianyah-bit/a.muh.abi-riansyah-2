# Operasi Aritmatika dengan Assignment
a = 7
print('Nilai a =', a)

a = 7
a += 1
print('Nilai a += 1 akan menjadi', a)

a = 7
a -= 1
print('Nilai a -= 1 akan menjadi', a)

a = 7
a *= 2
print('Nilai a *= 2 akan menjadi', a)

a = 7
a /= 2
print('Nilai a /= 2 akan menjadi', a)

a = 7
a %= 2
print('Nilai a %= 2 akan menjadi', a)

a = 7
a //= 2
print('Nilai a //= 2 akan menjadi', a)

a = 7
a **= 2
print('Nilai a **= 2 akan menjadi', a)

print('-' * 40)

# Operasi Logika OR
b = True
print('Nilai b =', b)
b |= False
print('Nilai b |= False akan menjadi', b)

b = False
print('Nilai b =', b)
b |= False
print('Nilai b |= False akan menjadi', b)

print('-' * 40)

# Operasi Logika AND
b = True
print('Nilai b =', b)
b &= False
print('Nilai b &= False akan menjadi', b)

b = False
print('Nilai b =', b)
b &= False
print('Nilai b &= False akan menjadi', b)

print('-' * 40)

# Operasi Logika XOR
b = True
print('Nilai b =', b)
b ^= False
print('Nilai b ^= False akan menjadi', b)

b = False
print('Nilai b =', b)
b ^= False
print('Nilai b ^= False akan menjadi', b)

print('-' * 40)

# Operasi Shifting (bitwise shift)
c = 0b0100
print('Nilai c =', format(c, '04b'))

c >>= 1
print('Nilai c >>= 1 akan menjadi', format(c, '04b'))

c = 0b0100
c <<= 1
print('Nilai c <<= 1 akan menjadi', format(c, '04b'))

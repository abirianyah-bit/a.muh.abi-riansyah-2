print("======================= IN")
nama_lengkap = "Bacharuddin Jusuf Habibie"

test = "a"
cek = test in nama_lengkap
print(test + " terdapat di " + nama_lengkap + " adalah " + str(cek))

test = "rud"
cek = test in nama_lengkap
print(test + " terdapat di " + nama_lengkap + " adalah " + str(cek))

test = "bac"
cek = test in nama_lengkap
print(test + " terdapat di " + nama_lengkap + " adalah " + str(cek))

print("======================= NOT IN")
nama_lengkap = "Bacharuddin Jusuf Habibie"

test = "a"
cek = test not in nama_lengkap
print(test + " tidak terdapat di " + nama_lengkap + " adalah " + str(cek))

test = "rud"
cek = test not in nama_lengkap
print(test + " tidak terdapat di " + nama_lengkap + " adalah " + str(cek))

test = "bac"
cek = test not in nama_lengkap
print(test + " tidak terdapat di " + nama_lengkap + " adalah " + str(cek))

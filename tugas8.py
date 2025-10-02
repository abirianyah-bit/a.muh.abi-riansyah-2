# Penggunaan pengecekan pada suatu data
data = [
    "Institut",
    "Teknologi",
    "Bacharuddin",
    "Jusuf",
    "Habibie"
]

print("data =", data)

print("======================= IN")
test1 = "Habibie"
test2 = "Parepare"

cek = test1 in data
print("Apakah " + test1 + " terdapat di dalam data? " + str(cek))

cek = test2 in data
print("Apakah " + test2 + " terdapat di dalam data? " + str(cek))

print("======================= NOT IN")
test1 = "institut"
test2 = "Institut"

cek = test1 not in data
print("Apakah " + test1 + " tidak terdapat di dalam data? " + str(cek))

cek = test2 not in data
print("Apakah " + test2 + " tidak terdapat di dalam data? " + str(cek))

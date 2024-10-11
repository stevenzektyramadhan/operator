perusahaan = "Microsoft"
list_pulau = ['jawa','sumatra', ' Sulawesi']

# ini adalah dictonary, insyaallah akan kita pelajari
# di pertemuan" yg akan datang

mahasiswa = {
    'nama': 'Lendis Fabri',
    'asal' : 'lamongan'
}

print(
    "apakah c ada di var perusahaan ? ",
    'c' in perusahaan
)
print(
    "apakah z tidak ada di var perusahaan ? ",
    'z' in perusahaan
)
print(
    "apakah madura tidak ada di var list_pulau ? ",
    'madura' not in list_pulau
)
print(
    "apakah madura ada di var list_pulau ? ",
    'madura' in list_pulau
)
print(
    "apakah atribut nama  ada di var mahasiswa ? ",
    'nama' in mahasiswa
)

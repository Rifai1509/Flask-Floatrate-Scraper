json1={
  "murid":
  [
    {"nama": "aziz", "no": 1, "kelas": "ipa a"},
    {"nama": "boot", "no": 2, "kelas": "ips a"},
    {"nama": "codet", "no": 3, "kelas": "ipa b"},
    {"nama": "dayat", "no": 4, "kelas": "ips b"},
    {"nama": "entok", "no": 5, "kelas": "ipa c"}
  ],
  "guru" :
  [
    {"nama": "Gatot", "no": 11, "kelas": "ipa a"},
    {"nama": "Jarot", "no": 22, "kelas": "ips a"},
    {"nama": "Duwi", "no": 33, "kelas": "ipa b"},
    {"nama": "Joko", "no": 44, "kelas": "ips b"},
    {"nama": "Heru", "no": 55, "kelas": "ipa c"}
  ]
}
json2={
  "a": {"nama": "aziz", "no": 1, "kelas": "ipa a"},
  "b": {"nama": "boot", "no": 2, "kelas": "ips a"},
  "c": {"nama": "codet", "no": 3, "kelas": "ipa b"},
  "d": {"nama": "dayat", "no": 4, "kelas": "ips b"},
  "e": {"nama": "entok", "no": 5, "kelas": "ipa c"}
}
#cara memamggil json1
# print(json1['murid'][0]['nama']) #manggil aziz
# print(json1['guru'][3]['nama']) #manggil joko

# cara memanggil json2

print(json2.keys())
print(json2["b"])
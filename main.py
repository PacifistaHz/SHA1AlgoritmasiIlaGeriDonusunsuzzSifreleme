import hashlib
f = open("sqls.txt", "r", encoding="utf-8")
metin = f.read()
metin = bytes(metin, "utf-8")

hashNesnesi = hashlib.sha1(metin)
hashDegeri = hashNesnesi.hexdigest()

print(hashDegeri)
modern_sozluk = ["LOL = sesli gülmek","ömer = 123546897"]

soru = input("hangi kelimenin anlamını istiyorsun?")

if soru in modern_sozluk.keys():
    print(modern_sozluk[soru])
else:
    #kelimse eşleşmiyorsa ne yapmalıyız?
    print("kelime bulunamadı")

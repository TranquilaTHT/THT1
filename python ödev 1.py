

print("Dört işlem yapma programına hoşgeldiniz..")
print("*****************************************")
print("Toplama İşlemi İçin + Tuşuna Basınız..")
print("Çıkartma İşlemi İçin - Tuşuna Basınız..")
print("Çarpma İşlemi İçin * Tuşuna Basınız..")
print("Bölme İşlemi İçin / Tuşuna Basınız..")
print("*****************************************")
s=input("Yapmak İstediğiniz İşlemi Seçiniz:")


if s == '+':
    print("Toplama İşlemini Seçtiniz")
    ilksayi=int(input("İlk rakamı giriniz:"))
    ikincisayi=int(input("İkinci Rakamı Giriniz:"))
    sonuc=ilksayi+ikincisayi
    print(ilksayi,"+",ikincisayi,"=",sonuc)
elif s == '-':
    print("Çıkartma İşlemini Seçtiniz")
    ilksayi=int(input("İlk rakamı giriniz:"))
    ikincisayi=int(input("İkinci Rakamı Giriniz:"))
    sonuc=ilksayi-ikincisayi
    print(ilksayi,"-",ikincisayi,"=",sonuc)
elif s == '*':
    print("Çarpma İşlemini Seçtiniz")
    ilksayi=int(input("İlk rakamı giriniz:"))
    ikincisayi=int(input("İkinci Rakamı Giriniz:"))
    sonuc=ilksayi*ikincisayi
    print(ilksayi,"*",ikincisayi,"=",sonuc)
elif s == '/':
    print("Bölme İşlemini Seçtiniz")
    ilksayi=int(input("İlk rakamı giriniz:"))
    ikincisayi=int(input("İkinci Rakamı Giriniz:"))
    sonuc=ilksayi/ikincisayi
    print(ilksayi,"/",ikincisayi,"=",sonuc)

else :
    print("sayı girsene yakışıklı")
















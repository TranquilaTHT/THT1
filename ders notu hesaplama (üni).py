class student():
    

    
    
        

    def show_myself(isim="null", soyisim="null", cinsiyet="null", notun="null",toplam_kredi=60,dersin_kredisi=2.4):

        isim = input("İsminiz: ")
        soyisim = input("Soy isminiz: ")
        cinsiyet = input("Cinsiyetiniz: ")

        print("""

""")
        
        print("İsminiz:",isim)
        print("Soy İsminiz:",soyisim)
        print("Cinsiyetiniz:", cinsiyet)
        print("Toplam Krediniz:",toplam_kredi)
        print("Dersin Kredisi:",dersin_kredisi)

    def show_point(notun=50,toplam_kredi=60,dersin_kredisi=2.4):
        print("""""")
        notun=int(input("Notunuzu Giriniz: "))
        print("""""")

        if(notun>100):
            print("100'den Küçük Bir Değer Giriniz.")

        else:
        
            sonuc=float(notun)*float(dersin_kredisi)
            sonuc=sonuc/float(toplam_kredi)
            
            print(sonuc)
        
        

    show_myself()
    show_point()



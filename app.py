# ==========================================
# Library Management System
# Python Learning Project
# ==========================================

print("=" * 45)
print("     KÜTÜPHANE YÖNETİM SİSTEMİ")
print("=" * 45)
print("Proje başarıyla başlatıldı.")
print("=" * 45)

kitap1 = {
    "kitap_adı": "Clean Code",
    "yazar": "Robert C. Martin",
    "yayın_yılı": 2008,
    "kategori": "Programlama",
    "stok_durumu": True
}

kitap2 = {
    "kitap_adı": "Python Crash Course",
    "yazar": "Eric Matthes",
    "yayın_yılı": 2019,
    "kategori": "Programlama",
    "stok_durumu": True
}

kitap3 = {
    "kitap_adı": "The Pragmatic Programmer",
    "yazar": "Andrew Hunt",
    "yayın_yılı": 1999,
    "kategori": "Programlama",
    "stok_durumu": True
}

kitap4 = {
    "kitap_adı": "Atomic Habits",
    "yazar": "James Clear",
    "yayın_yılı": 2018,
    "kategori": "Kişisel Gelişim",
    "stok_durumu": False
}

kitap5 = {
    "kitap_adı": "Deep Work",
    "yazar": "Cal Newport",
    "yayın_yılı": 2016,
    "kategori": "Kişisel Gelişim",
    "stok_durumu": True
}

kitap6 = {
    "kitap_adı": "The Psychology of Money",
    "yazar": "Morgan Housel",
    "yayın_yılı": 2020,
    "kategori": "Finans",
    "stok_durumu": True
}

kitap7 = {
    "kitap_adı": "Rich Dad Poor Dad",
    "yazar": "Robert T. Kiyosaki",
    "yayın_yılı": 1997,
    "kategori": "Finans",
    "stok_durumu": False
}

kitap8 = {
    "kitap_adı": "Sapiens",
    "yazar": "Yuval Noah Harari",
    "yayın_yılı": 2011,
    "kategori": "Tarih",
    "stok_durumu": True
}

kitap9 = {
    "kitap_adı": "The Hobbit",
    "yazar": "J. R. R. Tolkien",
    "yayın_yılı": 1937,
    "kategori": "Roman",
    "stok_durumu": True
}

kitap10 = {
    "kitap_adı": "1984",
    "yazar": "George Orwell",
    "yayın_yılı": 1949,
    "kategori": "Roman",
    "stok_durumu": False
}

kitaplar = [
    kitap1,
    kitap2,
    kitap3,
    kitap4,
    kitap5,
    kitap6,
    kitap7,
    kitap8,
    kitap9,
    kitap10
]

program_aktif = True

while program_aktif:
    print("\n1 - Kitapları Listele")
    print("2 - Kitap Ara")
    print("3 - Çıkış")

    menu_secimi = input("\nYapmak istediğiniz işlemi seçiniz: ")

    if menu_secimi == "1":
        for kitap in kitaplar:
            print("-" * 35)
            print(f"Kitap Adı: {kitap['kitap_adı']}")
            print(f"Yazar: {kitap['yazar']}")
            print(f"Yayın Yılı: {kitap['yayın_yılı']}")
            print(f"Kategori: {kitap['kategori']}")

            if kitap["stok_durumu"]:
                print("Stok Durumu: Mevcut")
            else:
                print("Stok Durumu: Mevcut değil")

    elif menu_secimi == "2":
        kitap_adi = input("\nAramak istediğiniz kitap adı: ")
        bulundu = False

        for kitap in kitaplar:
            if kitap_adi.lower() == kitap["kitap_adı"].lower():
                print("\nKitap bulundu!")
                print(f"Kitap Adı: {kitap['kitap_adı']}")
                print(f"Yazar: {kitap['yazar']}")
                print(f"Kategori: {kitap['kategori']}")
                print(f"Yayın Yılı: {kitap['yayın_yılı']}")
                bulundu = True
                break  
         
        if not bulundu:
            print("Aradığınız kitap bulunamadı.")

    elif menu_secimi == "3":
        print("Program sonlandırılıyor...")
        program_aktif = False

    else:
        print("Geçersiz seçim yaptınız.")
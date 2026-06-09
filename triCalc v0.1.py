import math

# Döngünün dışında, program ilk açıldığında bir kez selamlıyoruz
print("====================================")
print("   Welcome to the Triangle Calc v0.1 ")
print("====================================\n")

# Sonsuz döngüyü başlatıyoruz
while True:
    
    # Kullanıcı girdileri (Her döngü başında sıfırdan istenir)
    A = float(input("Length of A known side: "))
    B = float(input("Length of another known side: "))
    alpha = float(input("The angle between two known sides (degree): "))
    metric = input("Unit of length? (e.g., cm, m): ")

    # Hesaplamalar
    AlphaRad = math.radians(alpha)
    A2 = A**2
    B2 = B**2
    C2 = A2 + B2 - (2 * A * B * math.cos(AlphaRad))
    lenC = math.sqrt(C2)

    # Sonuçları ekrana basıyoruz
    print("\n------------------------------------")
    print(f"Your triangle: {A}{metric} | {B}{metric} | Angle: {alpha}°")
    print(f"Length of the unknown side is: {lenC:.2f} {metric}")
    print("------------------------------------\n")

    # CRITICAL: Kullanıcıya çıkmak isteyip istemediğini soruyoruz
    secim = input("Durdurmak için 'q' yazın, devam etmek için Enter'a basın: ")
    
    # Eğer kullanıcı küçük veya büyük 'Q' harfine basarsa döngüyü kırıyoruz
    if secim.lower() == 'q':
        print("\nTriangle Calc kapatılıyor. İyi günler!")
        break # Döngüden çıkış bileti
        
    print("\nYeni hesaplama başlatılıyor...\n")
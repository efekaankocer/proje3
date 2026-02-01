# PyQt Port Tarayıcı Uygulaması

Bu proje, PyQt5 kullanılarak geliştirilmiş basit bir port tarayıcı masaüstü uygulamasıdır.
Kullanıcıdan IP adresi ve port aralığı alarak belirtilen portların açık olup olmadığını kontrol eder.

## Özellikler
- Şifreli giriş ekranı
- IP adresi girişi
- Başlangıç ve bitiş portu belirleme
- Buton ile port tarama
- Sonuçların listelenmesi
- Sonuçların txt dosyasına kaydedilmesi

## Kullanılan Teknolojiler
- Python
- PyQt5
- Socket
- Threading

1️⃣ Giriş Ekranı (Login)

<img width="292" height="168" alt="image" src="https://github.com/user-attachments/assets/37c2ff0e-f4e1-4a51-95e2-584c27231988" />

Ekranda görünenler:

Başlık: “Giriş”

Bir adet Şifre alanı

Giriş Yap butonu


Program çalıştırıldığında ilk olarak bir giriş ekranı açılıyor.
Bu ekranda kullanıcıdan bir şifre girmesi isteniyor.
Şifre alanı gizli (password mode) olduğu için yazılan karakterler görünmüyor.

Detay (kodla bağlantı):

Login sınıfı bu ekranı oluşturuyor

Şifre doğruysa (1234) ana uygulama açılıyor

Yanlış girilirse hata mesajı çıkıyor

 
<img width="129" height="122" alt="image" src="https://github.com/user-attachments/assets/f515e1bc-2cdb-4fec-b350-a80cc2bbea02" />


“Şifre yanlış!”

2️⃣ Ana Uygulama – Port Tarayıcı Arayüzü

<img width="412" height="382" alt="image" src="https://github.com/user-attachments/assets/8d67d63c-3990-447c-98fd-f560829f83aa" />


Ekranda görünenler:

IP Adresi alanı (varsayılan: 127.0.0.1)

Başlangıç Portu

Bitiş Portu

Taramayı Başlat butonu

Sonuçların yazdığı büyük metin alanı


Giriş başarılı olduktan sonra port tarayıcı arayüzü açılıyor.
Kullanıcı burada taramak istediği IP adresini ve port aralığını giriyor.

Görsel detay:

Arayüz dark theme kullanıyor

Arka plan koyu, yazılar açık renkte

3️⃣ Taramayı Başlatma

<img width="412" height="376" alt="image" src="https://github.com/user-attachments/assets/60ad71d4-80a5-4e2e-92fe-3080f34f481f" />

Değerler girilmiş halde, tarama başlamadan önce

Örnek:

IP: 127.0.0.1

Başlangıç Port: 20

Bitiş Port: 1024


Gerekli bilgiler girildikten sonra “Taramayı Başlat” butonuna basılıyor.
Bu işlem yeni bir thread başlatarak port taramasını arka planda yapıyor.

Kod bağlantısı:

PortScannerThread sınıfı devreye giriyor

QThread kullanıldığı için arayüz donmuyor

4️⃣ Tarama Sırasında Açık Portların Gösterilmesi

<img width="389" height="178" alt="image" src="https://github.com/user-attachments/assets/83226787-5191-4290-b4e2-7d78deafab10" />


Ekranda görünenler:

Taranan IP: 127.0.0.1

Açık Port: 135


Program belirtilen port aralığını tek tek kontrol ediyor.
Açık olan portlar anlık olarak ekrana yazdırılıyor.
Aynı zamanda bu bilgiler sonuclar.txt dosyasına da kaydediliyor.

Teknik detay:

socket.connect_ex() ile port kontrolü yapılıyor

result.emit() ile GUI güncelleniyor

5️⃣ Sonuç Dosyası (sonuclar.txt)


sonuclar.txt dosyasının içeriği

<img width="171" height="89" alt="image" src="https://github.com/user-attachments/assets/ea3f22ca-b992-4c20-9652-e5b51714a3fb" />


Tarama tamamlandıktan sonra açık portlar hem ekranda gösteriliyor
hem de kalıcı olması için bir metin dosyasına yazılıyor.








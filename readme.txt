Kolaysayfam programının 0.55 sürümü, ürün satışı için html sayfası hazırlamakta kullanılır. index.html, buy.html, Linux Mint veya Ubuntu işletim sistemleri üzerinde gerekli programlar kurulu ise çalıştırılabilir.

Python3 ile çalıştırılmalıdır. Python3'ün Gtk,Gdk, Pango, re, os, gi, datetime, Template, shutil paketleri sisteminizde kurulu olmalıdır. Sisteminizde Glade programı da kurulu olmalıdır. 

Programın geliştirilmesi sonlandırılmıştır.

Programdaki formu doldurarak bir html sayfası oluşturabilirsiniz. Oluşturulacak html sayfası, program tarafından taşınabilir olarak hazırlanacaktır. html sayfasını, w3.css isimli stil dosyasını ve images klasörünü taşıyarak oluşturduğunuz sayfayı her bilgisayarda açabilirsiniz. Dilerseniz sahip olduğunuz web sitenizin herhangi bir dizinine taşıyarak internette de yayınlayabilirsiniz. Sitenizin faviconunu oluşturarak sayfanızın bulunduğu dizine koyarsanız o da görüntülenir.(favicon.gif veya favicon.png olarak) 

GNU Genel Kamu Lisansı Sürüm 3 ile lisanlandırılmıştır.
Lisans şartlarına göz atmak için GenelKamuLisansı(GPLv3).html dosyasını inceleyebilirsiniz.
Programın kodlarını değiştirerek kendi ürün tanıtım-satış sayfalarınızı oluşturabilirsiniz.

Menüden Yardım seçeneğini açtıktan sonra Yardım dosyasını açmak için Firefox programı kullanılmaktadır.


Programı çalıştırmak için sisteminizde kolaysayfam.py, kolaysayfam.glade aynı dizinde olmalıdır. kolaysayfam.py programı çalıştırılabilir yapılmalıdır. Bu şekilde çift tıklayarak terminalde çalıştır seçeneği ile ya da konsol üzerinden ./kolaysayfam.py komutu ile programı başlatabilirsiniz. ksa uzatılı dosyalar, programın bilgi girilmiş dosyalarıdır. (save dosyaları) Programı çalıştırdıktan sonra menüden  Dosya-Aç seçeneği ile bu dosya veya daha sonra kendi hazırlayacağınız herhangi bir dosya seçilerek yüklenebilir. Yaptığınız değişiklikleri menüden Dosya-Kaydet seçeneği ile kayıt altına alabilirsiniz. Web sayfanızı tamamladıktan sonra "Gerekli bölümleri doldurdum, web sayfasını oluştur" butonu ile sayfanızı oluşturabilirsiniz. Koyduğunuz sayfa adı ile aynı dizine bir html dosyası oluşturulacaktır. Sayfa adı kısmı boş kalırsa dosya ismi .html olacağından bu bir gizli dosya olacaktır. Bildiğiniz üzere gnu/linux dağıtımlarında . ile başlayan dosyalar gizli dosyalardır.

AÇILAN SAYFADA YAPILABİLECEK BİLGİ GİRİŞLERİ:
Sayfa Adı: Oluşturulacak web sayfasının adı (Örneğin asa yazarsanız web sayfanız asa.html olarak isimlendirilir)
Sayfa Başlığı: Tarayıcının üst kısmında görünecek olan yazı.(title tagı)
Seo Tanım: Arama motorları için açıklama(descrption meta tagı)
Seo Kelimeler:Arama motorları için anahtar kelimeler (keywords meta tagı)
Yazı Başlığı: Yazınızın üst başlığı, boyutunu da ayarlayabilirsiniz (h1 tagı)
Yazı: Sayfanızın içeriğinde bulunacak yazı. Font seçimi, yazı büyüklüğü ve yazının kalınlaştırılması ve yazının konumu ayarları mevcuttur.
Arkaplan Rengi: Rengi seçtiğinizde etkisini otomatik olarak göreceksiniz. (Template seçimi yaparsanız arka ekranda o görünür)
Yazı Rengi: Yazı karakterlerinin rengini değiştirebilirsiniz, seçimden hemen sonra sonucu görebilirsiniz.
Resim Ekle Butonu: Butona tıklayarak resim seçebilir ve sayfadaki boyutunu yüzde olarak ayarlayabilirsiniz.

Linkler Butonuna Tıklandığında Açılan Bilgi Girişleri:
Ana Sayfa: Menu1 değişkenine tıklandığında açılacak sayfanın linki girilir
Hakkımızda: Menu2 değişkenine tıklandığında açılacak sayfanın linki girilir
Satın Al:  Menu13  değişkenine tıklandığında açılacak sayfanın linki girilir
Menu1: Menu1 değişkenine "Ana Sayfa" isminden farklı bir giriş yapabilirsiniz.
Menu2: Menu2 değişkenine "Hakkımızda" isminden farklı bir giriş yapabilirsiniz.
Menu3: Menu3 değişkenine "Satın Al" isminden farklı bir giriş yapabilirsiniz.

Diğer Butonuna Tıklandığında Açılan Bilgi Girişleri:
Bellekleme Süresi(Saniye): Sayfanın tarayıcı hafızasında kalış süresini belirler.
Resim1 Alt: Resim ekle butonu ile eklediğiniz resim açılmazsa onun yerine buraya  yazılan bilgi görüntülenir.
Resim1 Title: Resim ekle butonu ile eklediğiniz resmin üzerinde mouse beklediğnde beliren yazı.
Template: Arka ekran görüntüsünü renk yerine fotoğraf olarak belirleyebilirsiniz.

GEREKLİ BÖLÜMLERİ DOLDURDUM, WEB SAYFASINI OLUŞTUR: Sayfanız girdiğiniz bilgiler doğrultusunda oluşturulur.
(Bu butonun hemen üzerinde bilgi ekranı bulunmaktadır, yapılan işlemler kırmızı arka ekran üzerine siyah renk yazı ile sunulur)



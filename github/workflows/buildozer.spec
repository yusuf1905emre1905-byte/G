[app]

# (str) Uygulamanın ekranda görünen adı
title = Ziplama Oyunu

# (str) Paket adı (Uptodown'da görünecek olan)
package.name = com.ziplama.com

# (str) Paket alan adı (com.ismin şeklinde)
package.domain = com.zerocore.oyun

# (str) Kaynak kodlarının olduğu dizin (nokta kalsın)
source.dir = .

# (list) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama versiyonu
version = 0.1

# (list) Gereksinimler (Burası hatasız APK için çok kritik)
requirements = python3,kivy

# (str) Ekran yönü (Dik ekran için portrait)
orientation = portrait

# (bool) Tam ekran modu
fullscreen = 1

# (list) Android izinleri (Şimdilik temel izinler yeterli)
android.permissions = INTERNET

# (int) Android API seviyesi (2025 standartı için 33 veya 34 iyidir)
android.api = 33

# (int) Minimum Android sürümü
android.minapi = 21

# (str) Android NDK sürümü (Hata almamak için boş bırak, sistem seçsin)
# android.ndk = 25b

# (bool) Mimari (64-bit zorunluluğu için)
android.archs = arm64-v8a, armeabi-v7a

# (str) Uygulama ikonu (Eğer icon.png yüklersen burayı açarsın)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
# (int) Log seviyesi (Hata ayıklamak için 2 kalsın)
log_level = 2

# (str) Geçici dosyaların saklanacağı yer
warn_on_root = 1

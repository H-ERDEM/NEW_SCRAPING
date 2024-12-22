from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# WebDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # CSV dosyasını aç ve başlık satırını yaz (Kategori sütunu da eklenmiş)
    with open("gundem_haberleri.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Haber İsmi", "Kategori"])  # Başlık satırı

        # 1. sayfadan 5. sayfaya kadar döngü
        for page_num in range(1, 6):
            # Sayfayı aç
            url = f"https://www.milliyet.com.tr/gundem/?page={page_num}"
            driver.get(url)

            # Sayfanın yüklenmesini bekle
            time.sleep(3)

            # Sayfadaki 'strong' etiketlerine sahip tüm yazıları al
            haberler = driver.find_elements(By.XPATH, "//div[contains(@class, 'cat-list-card__content')]/strong")

            # Haber başlıklarını ve kategoriyi CSV dosyasına kaydet
            for haber in haberler:
                writer.writerow([haber.text, "Gündem"])

            print(f"{page_num}. sayfa başlıkları CSV dosyasına kaydedildi.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    # Tarayıcıyı kapat
    driver.quit()

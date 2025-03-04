import webbrowser
from tqdm import tqdm

# URL temel formatı
base_url = "https://example-site/admin/{}/edit"

# ID aralığı (1432'den 1'e kadar)
start_id = 1350
end_id = 1325
# Web tarayıcısında her sayfayı açmak için
for product_id in tqdm(range(start_id, end_id - 1, -1), desc="İşlem Yapılıyor"):
    url = base_url.format(product_id)
    webbrowser.open(url)  # Tarayıcıda URL'yi aç

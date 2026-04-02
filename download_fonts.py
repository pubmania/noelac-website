import urllib.request
import os

fonts = {
    "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap",
    "Inter": "https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap",
    "Outfit": "https://fonts.googleapis.com/css2?family=Outfit:wght@400&display=swap",
    "Lora": "https://fonts.googleapis.com/css2?family=Lora:wght@400&display=swap",
    "OpenSans": "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400&display=swap"
}

os.makedirs(r"C:\Learning\NOELAC\static\fonts", exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in fonts.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            css = response.read().decode('utf-8')
            
        start = css.find('url(') + 4
        end = css.find(')', start)
        font_url = css[start:end].strip()
        
        font_req = urllib.request.Request(font_url, headers=headers)
        with urllib.request.urlopen(font_req) as response:
            font_data = response.read()
            
        ext = ".woff2"
        if ".ttf" in font_url:
            ext = ".ttf"
            
        with open(f"C:\\Learning\\NOELAC\\static\\fonts\\{name.lower()}{ext}", "wb") as f:
            f.write(font_data)
        print(f"Downloaded {name.lower()}{ext}")
    except Exception as e:
        print(f"Failed to fetch {name}: {e}")

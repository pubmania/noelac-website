from PIL import Image

def make_transparent(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    
    new_data = []
    # Identify the background color (usually 0,0,0 if black or top-left pixel)
    bg_color = datas[0] 
    
    for item in datas:
        # Match colors within a small threshold to handle compression artifacts
        if abs(item[0] - bg_color[0]) < 10 and abs(item[1] - bg_color[1]) < 10 and abs(item[2] - bg_color[2]) < 10:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

make_transparent("static/logo.png", "static/logo.png")
make_transparent("static/logo.png", "static/favicon.png")
make_transparent("static/logo.png", "static/favicon-16x16.png")
make_transparent("static/logo.png", "static/favicon-32x32.png")
make_transparent("static/logo.png", "static/apple-touch-icon.png")

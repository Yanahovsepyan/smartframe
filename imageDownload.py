from PIL import Image

png = Image.open(r'weaterIcon.png')
png.load() # required for png.split()

background = Image.new("RGB", png.size, (0, 0, 0))
background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

background.save('foo.jpg', 'JPEG', quality=80)
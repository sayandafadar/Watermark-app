import os

from PIL import Image

LOGO_FILENAME = 'Images/section-3.png'
logoIm = Image.open(LOGO_FILENAME)


im = Image.open('Images/boy.jpg')
rgb_im = im.convert('RGB')
width, height = rgb_im.size

# Resize the logo.
#     print(f'Resizing logo to fit {filename}...')
sLogo = logoIm.resize((int(width / 5), int(height / 5)))
sLogoWidth, sLogoHeight = sLogo.size

rgb_im.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)

# Save changes.
rgb_im.save(os.path.join('withLogo', 'new.jpg'))



from PIL import Image


def logo_style_transform_white(image, logo_anchor, mode=1):
    image = image.convert('RGBA')
    image_width, image_height = image.size
    
    if mode == 1:
        logo_width = logo_anchor
        logo_height = int(image_height * logo_width / image_width)
    elif mode == 2:
        logo_height = logo_anchor
        logo_width = int(image_width * logo_height / image_height)
        
    image = image.resize((logo_width, logo_height))
    
    pixels = image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if pixels[i, j][3] > 0:
                pixels[i, j] = (255, 255, 255, 255)
                
    return image
    
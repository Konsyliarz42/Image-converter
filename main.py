from PIL import Image
import PIL, os

formats = [ 'BMP', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'IM', 'JPEG', 'JPEG 2000', 'MSP',
            'PCX', 'PNG', 'PPM', 'SQI', 'SPIDER', 'TGA', 'TIFF', 'WebP', 'XBM'  ]

#--------------------------------
def open_image(path):
    try:
        print('\nLoading...')
        image = Image.open(path)

    except PIL.UnidentifiedImageError:
        print("File is not image!")

    else:
        name = path[path.rfind(chr(92)) + 1:]   # find '\'
        print(f"({name}) complete")
        return image

#--------------------------------
def convert_to(type_format, image):
    modes = ['F', 'I', 'HSV', 'LAB', 'YCbCr', 'CMYK', 'RGBA', 'RGB', 'P', 'L', '1']
    type_format = type_format.upper()

    for mode in modes:
        try:
            image.convert(mode)
            image.save('test_converter', type_format)
        except:
            pass
        finally:
            image.convert(mode)
            return image

#--------------------------------
def check_type(type_file):
    jpg = ['.jpg', '.jpeg', '.jpe' '.jif', '.jfif', '.jfi']
    jpg2 = ['.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2']
    spider = '.spi'
    tga = ['.tga', '.tpic'] 
    tiff = ['.tif', '.tiff'] 
    webp = '.webp'

    if type_file in jpg:
        return 'JPEG'
    elif type_file in jpg2:
        return 'JPEG 2000'
    elif type_file == spider:
        return 'SPIDER'
    elif type_file in tga:
        return 'TGA'
    elif type_file in tiff:
        return 'TIFF'
    elif type_file == webp:
        return 'WebP'
    else:
        return type_file[1:].upper()

#--------------------------------
def save_image(type_file, image, path, name):
    if type_file[0] != '.':
        type_file = '.' + type_file

    type_file = type_file.lower()
    name += type_file
    path = os.path.join(path, name)
    type_format = check_type(type_file)
    
    try:
        print('\nSaving...')
        image = convert_to(type_format, image)
        image.save(path, type_format)

    except OSError:
        print("Cannot converting")
        os.remove(path)

    else:
        print('Complete')

#================================================================
if __name__ == "d__main__":
    img = None

    print("Type path to image...")

    while img == None:
        path = input('>: ')

        while os.path.isfile(path) == False:
            path = input("\nFile not found!\nPleas type path again\n>: ")

        img = open_image(path)

        if img == None:
            print("Pleas type path again")

img = open_image('img_lights.png')
save_image('tga', img, os.getcwd(), 'x')
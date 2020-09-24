from PIL import Image
import PIL, os

#formats = [ 'BMP', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'IM', 'JPEG', 'JPEG 2000', 'MSP',
#            'PCX', 'PNG', 'PPM', 'SQI', 'SPIDER', 'TGA', 'TIFF', 'WebP', 'XBM'  ]

#--------------------------------
def open_image(path):
    """This function run opening procedure and retruns image file."""

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
def check_type(type_file):
    """Function check a type file and returns name of format file"""

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
def convert_to(type_file, image):
    """Function converts an image to a color mode and returns it converted."""

    modes = ['RGBA', 'RGB', 'F', 'I', 'HSV', 'LAB', 'YCbCr', 'CMYK', 'P', 'L', '1']
    type_format = check_type(type_file)

    for mode in modes:
        try:
            image.convert(mode)
            image.save('test_converter' + type_file, type_format)
        except:
            if os.path.isfile('test_converter' + type_file):
                os.remove('test_converter' + type_file)
        else:
            print("Convert to mode:", mode)
            image.convert(mode)
            return image

#--------------------------------
def save_image(type_file, image, path, name):
    """This function run saving procedure."""

    if type_file[0] != '.':
        type_file = '.' + type_file

    type_file = type_file.lower()
    name += type_file
    path = os.path.join(path, name)
    type_format = check_type(type_file)

    print(type_file, type_format, name, path, sep=' | ')
    
    try:
        print('\nSaving...')
        image = convert_to(type_file, image)
        image.save(path, type_format)

    except OSError:
        print("Cannot converting!")
        os.remove(path)
    
    except AttributeError:
        print("Error in change color mode!")

    else:
        print(f"({name}) complete")

#================================================================
if __name__ == "__main__":
    img = None
    print("Image Converter by Tomasz Kordiak")

    while True:
        print("\nEnter path file (enter empty to abort)")
        while img == None:
            path    = input(">: ")

            if not path:
                print("End program")
                break
            else:
                img = open_image(path)

        if img:
            print("\nEnter data to converting")
            type_file   = input("Type file      >: ")
            name        = input("Name file      >: ")

            print("\nEnter empty to use program directory")
            path    = input("Save folder    >: ")
    
            if not path:
                path = os.getcwd()
            
            save_image(type_file, img, path, name)
            img = None
        else:
            break
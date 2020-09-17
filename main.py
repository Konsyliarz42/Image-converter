from PIL import Image
import PIL, os

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
def convert_to(type_format, image, path, name):
    name += '.' + type_format
    path += chr(92) + name

    print('\nSaving...')

    try:
        image.load()

        if image.getbands() != ('R', 'G', 'B'):
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask = image.split()[3])
            background.save(path, type_format, quality=100)
            
        else:
            image.save(path)

    except OSError:
        print("Cannot converting")
        os.remove(path)

    else:
        print('Complete')

#================================================================
if __name__ == "__main__":
    img = None

    print("Type path to image...")

    while img == None:
        path = input('>: ')

        while os.path.isfile(path) == False:
            path = input("\nFile not found!\nPleas type path again\n>: ")

        img = open_image(path)

        if img == None:
            print("Pleas type path again")

    print("\nSave in...")
    path = input('>: ')

    
    convert_to('bmp', img, path, 'GTX')
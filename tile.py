# original image file should be in the same directory as this script, and already in 4x6 dimensions
#
# outputs tiles in the format "11_original-image.jpg" in same directory, where 11
# indicates the upper left corner of the original image, and 44 indicates the lower
# right corner.

import Image

def make_tiles(filename):
    try:
        img = Image.open(filename)
        width = img.size[0]   #pixels
        height = img.size[1]  #pixels
        new_width = int(width/4)
        new_height = int(height/4)
        for i in range(1, 5):
            for j in range(1, 5):
                img_new = img.crop(((i-1)*new_width, (j-1)*new_height, i*new_width, j*new_height))
                img_new.load()
                new_filename = str(j) + str(i) + "_" + filename
                img_new.save(new_filename, "JPEG")
    except IOError:
        print "Something went wrong! :("


if __name__ == "__main__":
    filename = "IMG_7004.jpg" #change this to be the filename of your image
    make_tiles(filename)

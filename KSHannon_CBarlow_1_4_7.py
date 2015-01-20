import Image
import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw    
import math        
'''def resize_canvas(old_image_path="314.jpg", new_image_path="save.jpg",
                  canvas_width=500, canvas_height=500):
    """Resize the canvas of old_image_path and store the new image in
       new_image_path. Center the image on the new canvas.
    """
    im = Image.open(old_image_path)
    old_width, old_height = im.size

    # Center the image
    x1 = int(math.floor((canvas_width - old_width) / 2))
    y1 = int(math.floor((canvas_height - old_height) / 2))

    mode = im.mode
    if len(mode) == 1:  # L, 1
        new_background = (255)
    if len(mode) == 3:  # RGB
        new_background = (255, 255, 255)
    if len(mode) == 4:  # RGBA, CMYK
        new_background = (255, 255, 255, 255)

    newImage = Image.new(mode, (canvas_width, canvas_height), new_background)
    newImage.paste(im, (x1, y1, x1 + old_width, y1 + old_height))
    newImage.save(new_image_path)''' #just showed up randomly oneday
def add_logo(directory=None):

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'Logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    #image_list, file_list = get_images(directory)

    student_file = os.path.join(directory, 'landscape.jpg')
    student_img = PIL.Image.open(student_file)
    
    width, height = student_img.size

    border_file = os.path.join(directory, 'geometric.jpg')
    border_img = PIL.Image.open(border_file)
    border_big = border_img.resize((width + 40, height + 40))
    
    border_width, border_height = border_big.size

        # Center the image
    x1 = int(math.floor((border_width - width) / 2))
    y1 = int(math.floor((border_height - height) / 2))


    logo_file = os.path.join(directory, 'powercat.png')
    logo_img = PIL.Image.open(logo_file)
    logo_small = logo_img.resize((50, 40)) 

    student_img.paste(logo_small, (0, 0), mask=logo_small)
    border_big.paste(student_img, (x1,y1))

    #student_img_filename = os.path.join(new_directory, filename + '.png')
    border_big.save('this is a thing now.png')
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list 
'''def add_logo_all_images(directory=None):
=======
=======
>>>>>>> parent of 4f755e5... back to old
=======
>>>>>>> parent of 4f755e5... back to old
=======
>>>>>>> parent of 4f755e5... back to old
def add_logo_all_images(directory=None):
    
>>>>>>> parent of 4f755e5... back to old
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'Logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)

    for n in range(len(image_list)):

        filename, filetype = file_list[n].split('.')
<<<<<<< HEAD

        student_img = add_logo(image_list[n])
   
        #student_img.save('HALP5.png')
        new_image_filename = os.path.join(new_directory, filename + '.png')
        student_img.save(new_image_filename)
'''
<<<<<<< HEAD
import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            
import Image
def add_logo(directory=None):
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
        #im.paste('powercat.png',(0,0))
        
        new_image = im.paste('powercat.png',(0,0))
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
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
        
        
          
=======
>>>>>>> origin/master

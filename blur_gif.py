#Import numpy to vectorize each frame for MTCNN and to vectorize the output frame
import numpy as np
#Import imageio to read the input gif
import imageio
#Use PIL's Image and GaussianBlur to filter parts of the images with the faces
from PIL import Image
from PIL.ImageFilter import GaussianBlur
#Import the MTCNN model, designed for capturing parts of faces in an image
from mtcnn import MTCNN
#Use moviepy's ImageSequenceClip to convert a 4d np array to a gif
from moviepy.editor import ImageSequenceClip

#The function face_blur will get inputting a vectorized image and output a vectorized image with blurred faces using MTCNN
def face_blur(img_arr):
    #Convert the numpy array to Image format 
    image = Image.fromarray(img_arr)
    
    #Use the MTCNN model to detect faces from the input numpy array. This Model will detect the boxes, but also the different parts of a face
    boxes = MTCNN().detect_faces(img_arr[:, :, :3])
    #In some images, there are multiple faces so a loop between each box is neccessary
    for face in boxes:
      #The only neccessary part of MTCNN needed is the boxes, so get that from the face along with x1 and y1 coordinates
      x, y, width, height = face['box']
      x1, y1 = x + width, y + height
      
      #Get the part of the image with the face and apply a blur filter to it(a radius as 4 is good for both far away faces and close up faces)
      face = image.crop((x, y, x1, y1))
      blurred_face = face.filter(GaussianBlur(radius=4))
      #Paste the new blurred face onto the original image, using the same coordinates
      image.paste(blurred_face, (x, y, x1, y1))

    #Conver the PIL Image back to a numpy array for ImageSequenceClip to process, and return the new image array
    img_arr = np.array(image)
    return img_arr

#The function blur_gif will be given the path to an input gif, the desired path for the output gif, and the desired fps of the new gif
def blur_gif(input_gif, output_file, fps):
    #Read the input gif path with imageio
    gif = imageio.get_reader(input_gif)
    #Every frame, apply a blur to the frame with the face_blur function, and make sure the last dimension is 3 dimensional for ImageSequenceClip
    new_gif = [face_blur(np.array(frame))[:, :, :3] for frame in gif]
    #Conver the list of numpy arrays to a gif and write the gif in the desired output path and with the desired fps
    clip = ImageSequenceClip(new_gif, fps=fps)
    clip.write_gif(output_file, fps=fps)

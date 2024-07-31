import os 
from PIL import Image 


output_dir = './Pdfs'
source_dir = './Images'

for file in os.listdir(source_dir):
    if file.split('.')[-1].lower() in ('png', 'jpg', 'jpeg'):
        image = Image.open(os.path.join(source_dir, file))
        image_converted = image.convert('RGB')
        image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))

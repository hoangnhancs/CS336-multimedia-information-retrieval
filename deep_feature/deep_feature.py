from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input

from keras.models import Model
from keras.layers import Input
import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt
#from keras_vggface.VGG16 import VGG16

image_input = Input(shape=(224, 224, 3))

vgg_model = VGG16() # pooling: None, avg or max
out = vgg_model.get_layer('fc2').output
#vgg_model_fc7 = Model(image_input, out)
vgg_model_fc2 = Model(vgg_model.input, out)

# Change the image path with yours.
img_paths = []
img = []
# for _ in img_paths:
#   img_load = image.load_img(_)
#   img.append(img_load)
#   arr_img = image.img_to_array(img_load)
#   arr_img = 
# img = image.load_img('/content/ec8adc9b-7304-45ae-b453-bd2ee67d3d1c.jpg', target_size=(224,224))
# img2 = image.load_img('/content/blowing_in_the_wind.jpg', target_size=(224,224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
# x2 = image.img_to_array(img2)
# x2 = np.expand_dims(x2, axis=0)
# x2 = preprocess_input(x2)
# vgg_model_fc2_preds = vgg_model_fc2.predict(x)
#vgg_model_predict = vgg_model.predict(x)
# vgg_model_fc2_preds2 = vgg_model_fc2.predict(x2)
# print(len(vgg_model_fc2_preds[0]))
# print(vgg_model_fc2_preds)
#print(len(vgg_model_predict[0]))
#print(vgg_model.summary())
print(vgg_model_fc2.summary())
#print(np.linalg.norm((vgg_model_fc2_preds[0]- vgg_model_fc2_preds2[0]), axis=0))
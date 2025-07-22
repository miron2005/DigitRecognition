
from PIL import Image
import numpy as np

def predict(img_path='./test_image_1.jpg', model_path='./model_mnist.h5'):

    from tensorflow.keras.models import load_model

    model = load_model(model_path)

    img_width, img_height = 28, 28

    img = Image.open(test_path).convert('L').resize((img_width, img_height))
    img = 255 - np.array(img)
    img[img<50] = 0

    image = img.reshape(-1, 28, 28, 1)
    cls_image = np.argmax(model.predict(image))

    print(cls_image)


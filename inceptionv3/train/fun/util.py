from skimage.transform import resize

import numpy as np 
def helpResize(x_train,x_validation,image_size):
    '''
    HelpResize(x_train = np.array, x_validation = np.array, image_size = int or tuple)

    This is a function to resize the image dimension.
    '''
    X_train = []
    X_validation = []
    
    if type(image_size) is int:
        image = (image_size,image_size)
    else:
        image = tuple(image_size)
    
    for num,img in enumerate(x_train):
        X_train.append(resize(img,image,mode='constant',anti_aliasing=True))
    for num,img in enumerate(x_validation):
        X_validation.append(resize(img,image,mode='constant',anti_aliasing=True))
    
    X_train = np.array(X_train)
    X_validation = np.array(X_validation)
    return X_train,X_validation


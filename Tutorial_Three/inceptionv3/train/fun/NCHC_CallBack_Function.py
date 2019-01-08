#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import roc_auc_score

import tensorflow.python.keras.callbacks
import time

class NCHC_CallBack(tensorflow.keras.callbacks.Callback):
    def __inint__(self):
        pass
    def on_train_begin(self, logs={}):
        self.aucs = []
        self.losses = []
        self.batch_time = []
        self.img_per_sec = []

    def on_train_end(self, logs={}):
        return

    def on_epoch_begin(self, epoch, logs={}):
        return

    def on_epoch_end(self, epoch, logs={}):
        temp_losses = '{:0.3f}'.format(logs.get('loss'))
        self.losses.append(temp_losses)
        y_pred = self.model.predict(self.validation_data[0])
        y_true = self.validation_data[1]
 
        try:
            temp_score = '{:0.3f}'.format(roc_auc_score(y_true,y_pred))
            self.aucs.append(temp_score)
        except ValueError:
            pass
        return

    def on_batch_begin(self, batch, logs={}):
        self.batch_time_start = time.time()
        return

    def on_batch_end(self, batch, logs={}):
        batch_time = time.time() - self.batch_time_start
        batch_size = logs.get('size', 0)
        self.batch_time.append( batch_time )
        self.img_per_sec.append( batch_size / batch_time )
        return



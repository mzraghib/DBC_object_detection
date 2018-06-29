#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test if the tfCreator generates images correctly

"""


#TODO(me): Create unit tests


import tensorflow as tf

for example in tf.python_io.tf_record_iterator("data/foobar.tfrecord"):
    result = tf.train.Example.FromString(example)




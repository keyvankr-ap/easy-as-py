#!/usr/bin/python
import os
path = os.getcwd()
path = path.strip('/')
path_components = path.split('/')
print(path_components)

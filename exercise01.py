#!/usr/bin/python
import os
path = os.getcwd()
path = path.strip(os.sep)
path_components = path.split(os.sep)
if '' in path_components :
    path_components.remove('')
print(path_components)

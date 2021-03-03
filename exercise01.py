#!/usr/bin/python
import os
path = os.getcwd()
path = path.strip(os.sep)
path_components = path.split(os.sep)
print(path_components)

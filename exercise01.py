#!/usr/bin/python

import os
def get_path_components(path):
    #path = os.getcwd()
    #path = path.strip(os.sep)
    path_components = path.split(os.sep)
    while '' in path_components :
        path_components.remove('')
    return path_components


print(get_path_components('/usr/local/bin/'))

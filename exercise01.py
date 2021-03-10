#!/usr/bin/python

import os
def get_path_components(path=None):
    #path = os.getcwd()
    #path = path.strip(os.sep)
    if path is None:
        path = os.getcwd()
    
    path_components = path.split(os.sep)

    
    while '' in path_components :
        path_components.remove('')
    return path_components

def get_path_length(path=None):
    return len(get_path_components(path))



print(get_path_components())
print(get_path_length("/usr/bin"))

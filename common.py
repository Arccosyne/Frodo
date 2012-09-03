#!/usr/bin/python
# Frodo - A web app for monitoring SGE cluster status: https://bitbucket.org/yoavram/frodo
# Copyright (c) 2012 by Yoav Ram.
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.
import os.path
import inspect
import ConfigParser

def working_folder():
    #return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return os.path.dirname(__file__)

def configuration():
    folder = working_folder()
    filepath = folder + os.path.sep + 'frodo.properties'
    cfg = ConfigParser.ConfigParser()
    cfg.read(filepath)
    return cfg

def hosts():
    folder = working_folder()
    filepath = folder + os.path.sep + 'hosts'
    return filepath

if __name__ == '__main__':
    pass

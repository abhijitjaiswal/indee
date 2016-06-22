'''
Created on 22 June, 2016
@author: abhijit
'''
import configparser
import os
import time

def get_config_parser(config_file, options={ }):
    # NOTE: Use SafeConfigParser instead of ConfigParser to support
    # escaping of format strings e.g. % as %%
    config = configparser.SafeConfigParser(options)
    config.read(config_file)
    return config
#!/usr/bin/python
 # -*- coding: utf-8 -*-

"""
    Author  : Shreenidhi Ramachandra
    Date    : 11 September,2017
    Email   : Shreenidhi.tvk@gmail.com
    Usage   : check for the folder existence and create if necessary
"""

import os

class FolderUtility(object):
    """docstring for FolderUtility.
        Handels folder creation
    """
    def __init__(self, arg):
        super(FolderUtility, self).__init__()
        self.arg = arg

    def is_available(self,folder_name):
        if os.path.exist(folder_name):
            return pass

    def create_folder(self,folder_name):
        if self.is_available(folder_name):
            print "Info     : Folder "+folder_name+" already exists!"
        else:
            try:
                pass
            except Exception as e:
                raise

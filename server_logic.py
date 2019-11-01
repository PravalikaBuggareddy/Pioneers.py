"""
This module contains classes named User_services and Admin_services
"""
import os
from pathlib import Path
import datetime
import time
from pylint.lint import Run

class Userservices:
    """This module contains the class User_services """
    def __init__(self, root_directory, curr_directory, username, password):
        """Initializing variables"""
        self.username = username
        self.password = password
        self.root_directory = root_directory
        self.curr_directory = curr_directory
        self.read_file = ''
        self.start_point = 0

    def list_files(self, path_1):
        """
        Files are listed along with their size and last date modified
        """
        files = list(os.listdir(path_1))
        dict1 = {}
        #list1 = ['']
        dict2 = dict()
        for f_1 in files:
            last_mod = os.stat(f_1).st_ctime
            date1 = datetime.datetime.strptime(time.ctime(last_mod), "%a %b %d %H:%M:%S %Y")
            thestats = os.stat(f_1)
            dict2[f_1] = thestats
            dict1[f_1] = date1

        print('Name \t\t\t Size \t\t Date Modified')
        print('-----------------------------------------------------')
        for key in dict1:
            print('{:30s}\t\t\t{:d}\t\t{}'.format(key, dict2[key].st_size, dict1[key][0]))


    def create_folder(self, folder_name, privilage):
            """
            Creating a folder
            """
            path = os.path.join(self.curr_directory,folder_name)
            os.mkdir(path)
            if privilage == 'admin':
                self.create_admin_log(path)
            else:
                self.create_user_log(path, folder_name)    

    def create_user_log(self, directory, folder_name):
            """
            
            """
            file_name = str(f'{directory}\\log.txt')
            file = open(file_name, "w")
            data = folder_name
            user_data = [data, "\n"]
            file.writelines(user_data)
            file.close()
            self.create_admin_log(directory)

    def create_admin_log(self, directory):
        """
        login for admin
        """
        path = self.root_directory #admin directory
        file_name = str(f'{path}\\adminlog.txt')
        open_file = open(file_name, 'r')
        file_lines = open_file.readlines()
        num_lines = sum(1 for line in open('adminlog.txt'))
        i = 0
        numbers = []
        names = []
        for i in range(num_lines):
            file = file_lines[i].strip()
            find = file.find(",")
            numbers.append(find)
            names.append(file[:numbers[i]])
        for i in names:
            self.modify_file(directory, 'log.txt', i)

    def modify_file(self, directory, file_name, input1):
            """
            modifying the file
            """
            file_name = str(f'{directory}\\{file_name}')
            input1 = input1
            file = open(file_name, 'a+')
            user_data = [input1, "\n"]
            file.writelines(user_data)
            file.close()

    def write_file(self, file_name, input_string = None):
        """
        modifying the file
        """
        path = os.path.join(self.curr_directory, file_name)
        if input_string == None:
            file = open(path, 'w')
            file.close()
            reply = 'File cleared'
            return reply

        file = open(path, 'a')
        user_data = [input_string, "\n"]
        file.writelines(user_data)
        file.close()
        reply = 'file edited successfully'
        return reply

    def start_read(self, file_name):
        if file_name == None:
            if self.read_file != '':
                self.read_file = ''
                return 'File Closed'
            return 'Invalid argument'
        else:
            path = os.path.join(self.curr_directory, file_name)
            try:
                if os.path.exists(path):
                    if self.read_file == file_name:
                        self.start_point = self.start_point+100
                        reply = self.view_file(path, self.start_point)
                        return reply
                    else:
                        self.read_file = file_name
                        self.start_point = 0
                        reply = self.view_file(path, self.start_point)
                        return reply
            except Exception as e:
                print('start ',e)
                reply = 'File not found'
                return reply

    def view_file(self, file_name, startpoint):
        """
        view the file
        """
        strt = startpoint+100
        file = open(file_name, "r")
        value = file.read()
        if strt >= len(value):
            self.start_point = 0
        return str(value[startpoint:strt])
    def reverse(self, val): 
        str = "" 
        for i in val: 
            str = i + str
        return str
    def change_directory(self, folder_name):
        inp = '..'
        try:
            if folder_name == inp :
                reval = self.reverse(self.curr_directory)
                no =reval.find('\\')+1
                new_path = reval[no:]
                if self.reverse(new_path) == self.root_directory:
                    return 'access denied'
                else:
                    self.curr_directory = self.reverse(new_path)
                    reply = 'directory changed to '+self.curr_directory
                    return reply
            else:
                user_directory = os.path.join(self.curr_directory,folder_name)
                if os.path.isdir(user_directory):
                    self.curr_directory = user_directory
                    reply = 'directory changed to '+self.curr_directory
                    return reply
                else:
                    return 'file not found'
        except Exception as e:
            reply = f'Exception occured : {e}'
            return reply
        return 'error'
    def print(self):
        return self.curr_directory

class Adminservices(Userservices):
    """
    Admin_services class is created which inherits from user_services
    """
    def __init__(self, root_directory, curr_directory, username, password):
        """Initializing variables"""
        self.username = username
        self.password = password
        self.root_directory = root_directory
        self.curr_directory = curr_directory
        self.read_file = ''
        self.start_point = 0

    def delete_file(self):
        """deleting a file """
        return 0

'''R = Run(["class1.py"], do_exit = False)
print(R.linter.stats["global_note"])'''
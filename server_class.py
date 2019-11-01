from server_logic import Adminservices
from server_logic import Userservices
import os

class Server:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.root_directory = os.getcwd()
        self.current_directory = ''
        self.message = ''
        self.privilege = ''
        #self.client = None

    def getpassword(self,user_name):
        admin_log = 'adminlog.txt'
        admin_file=open(admin_log,'r')
        admin_file_lines=admin_file.readlines()
        admin_line_count = sum(1 for line in open('adminlog.txt'))
        admin_numbers =[]
        admin_names =[]
        admin_pass = []
        for i in range(admin_line_count):
            file = admin_file_lines[i].strip()
            find = file.find(",")
            admin_numbers.append(find)
            admin_names.append(file[:admin_numbers[i]])
            admin_pass.append(file[admin_numbers[i]+1:])
        for j in range(len(admin_names)):
            if user_name == admin_names[j]:
                out = str(f'{admin_names[j]} {admin_pass[j]} admin')
                return out
        user_log = 'userlog.txt'
        user_file=open(user_log,'r')
        user_file_lines=user_file.readlines()
        user_line_count = sum(1 for line in open('userlog.txt'))
        user_numbers =[]
        user_names =[]
        user_pass = []
        for i in range(user_line_count):
            file = user_file_lines[i].strip()
            find = file.find(",")
            user_numbers.append(find)
            user_names.append(file[:user_numbers[i]])
            user_pass.append(file[user_numbers[i]+1:])
        for j in range(0, len(user_names)):
            if user_name == user_names[j]:
                uout = str(f'{user_names[j]} {user_pass[j]} user')
                return uout
        uout = 'failed'
        return uout

    def check(self,given_username,given_password,user,password):
        if given_username == user:
            if given_password == password:
                return 'successful'
        return 'failed'
    
    def initilise(self):
        if self.privilege == 'admin':
            self.client = Adminservices(
                self.root_directory,
                self.current_directory,
                self.username,
                self.password
            )
            print('succes admin')
        elif self.privilege == 'user':
            self.client = Userservices(
                self.root_directory,
                self.current_directory,
                self.username,
                self.password
            )
            print('succes user')
        else:
            print('error')

    def login(self,split_message):
        username=split_message[1]
        password=split_message[2]
        reply=self.getpassword(username)
        split_message_reply = reply.split(' ',2)  #list
        print(split_message_reply)
        given_username=split_message_reply[0]
        if given_username == 'failed':
            return 'failed'

        given_password=split_message_reply[1]
        privilege = split_message_reply[2]
        check_reply=self.check(given_username, given_password, username, password)
        if check_reply == 'successful':
            #cwd = str(f'{self.root_directory}\\{username}')
            cwd = os.path.join(self.root_directory,username)
            self.current_directory = cwd
            self.username = username
            self.password = password
            self.privilege = privilege
            self.initilise()
            return 'successful'
        elif check_reply == 'failed':
            return 'failed'

    def register(self, user_name, password, privilage):
        if privilage == 'admin':
            file_name = str(f'{self.root_directory}\\adminlog.txt')
        elif privilage == 'user':
            file_name = str(f'{self.root_directory}\\userlog.txt')
        file = open(file_name,"a+")
        user_data = str(f'\n{user_name},{password}')
        file.writelines(user_data)
        file.close()
        self.create_folder(user_name,privilage)

    def create_folder(self, user_name, privilage):
            """
            Creating a folder
            """
            path = os.path.join(self.root_directory,user_name)
            os.mkdir(path)
            if privilage == 'admin':
                self.create_admin_log(path)
            else:
                self.create_user_log(path, user_name)    

    def create_user_log(self, directory, user_name):
            """
            
            """
            file_name = str(f'{directory}\\log.txt')
            file = open(file_name, "w")
            data = user_name
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

    def find(self, user_name, privilage):
        if privilage == 'admin':
            log_name = 'adminlog.txt'
        else:
            log_name = 'userlog.txt'
        
        file_name = str(f'{self.root_directory}\\{log_name}')
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
                
        if user_name in names:
            return 'exist'
        return 'ok'

    def start_register(self):
        split_message = self.message.split(' ',3)
        username = split_message[1]
        password = split_message[2]
        privilage = split_message[3]
        reply = self.find(username, privilage)
        if reply == 'exist':
            return reply
        self.register(username, password, privilage)
        split_message = ['login',username,password]
        reply = self.login(split_message)
        return reply
        
    def analize(self,split_message):
        command = split_message[0]

        if self.username == '':
            if command == 'login':
                reply = self.login(split_message)
                print('analise_reply : ',reply)
                return reply
            elif command == 'register':
                reply = self.start_register()
                return reply
            return 'failed'
        else:
            if command == 'list':
                reply = self.client.print()
                return reply

            elif command == 'change_folder':
                try:
                    argument_1 = split_message[1]
                    reply = self.client.change_directory(argument_1)
                except:
                    reply = 'Failed'
                return reply
 
            elif command == 'read_file':
                try:
                    argument_1 = split_message[1]
                    reply = self.client.start_read(argument_1)
                except IndexError:
                    reply = self.client.start_read(None)
                except:
                    reply = 'error occured'
                return reply

            elif command == 'write_file':
                try:
                    argument_1 = split_message[1]
                except IndexError:
                    reply = 'invalid Argument'
                    return reply
                try:
                    argument_2 = split_message[2]
                    reply = self.client.write_file(argument_1,argument_2)
                except IndexError:
                    reply = self.client.write_file(argument_1)
                except:
                    reply = 'error occured'
                return reply
            elif command == 'create_folder':
                try:
                    argument_1 = split_message[1]
                    reply = self.client.create_folder(argument_1,self.privilage)
                except:
                    reply = 'error occured'
                return reply
            else:
                return 'Invalid input'

    def split(self, message):
        self.message = message
        split_message = self.message.split(' ',2)  #list
        print('message split: ',split_message)
        result = self.analize(split_message)
        print('message split reply: ',result)
        return result
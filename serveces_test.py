import unittest
from server_logic import Adminservices
from server_logic import Userservices
import os


class TestSum(unittest.TestCase):

    def test_folder_creation(self):
        client = Userservices(
                    os.getcwd(),
                    os.getcwd(),
                    'pawan',
                    '12345'
                )
        inputvalues = [
            ['asdf','admin'],
            ['asdf','admin']
        ]
        expectedvalues = [
            'folder created',
            'failed to create folder'
        ]
        result = []
        for inputv in inputvalues:
            result.append(client.create_folder(inputv[0],inputv[1]))
        self.assertListEqual(result, expectedvalues)
    
    def test_write_file(self):
        client = Userservices(
                    os.getcwd(),
                    os.getcwd(),
                    'pawan',
                    '12345'
                )
        inputvalues = [
            ['testfile.txt','hello world'],
            ['testfile.txt','second statement'],
            ['testfile.txt',None]
        ]
        expectedvalues = [
            'file edited successfully',
            'file edited successfully',
            'File cleared'
        ]
        result = []
        for inputv in inputvalues:
            result.append(client.write_file(inputv[0],inputv[1]))
        self.assertListEqual(result, expectedvalues)

    def test_change_folder_admin(self):
        userpath = os.path.join(os.getcwd(),'pawan')
        client = Userservices(
                    os.getcwd(),
                    userpath,
                    'pawan',
                    '12345'
                )
        inputvalues = [
            ['group','admin'],
            ['testfolder','admin'],
            ['..','admin'],
            ['..','admin'],
            ['..','admin'],
        ]
        pathlist = [
            os.path.join(userpath,'group'),
            userpath,
            os.path.dirname(userpath)
        ]
        expectedvalues = [
            f'directory changed to {pathlist[0]}',
            'file not found',
            f'directory changed to {pathlist[1]}',
            f'directory changed to {pathlist[2]}',
            'access denied'

        ]
        result = []
        for inputv in inputvalues:
            result.append(client.change_directory(inputv[0],inputv[1]))
        self.assertListEqual(result, expectedvalues)
    
    def test_change_folder_user(self):
        userpath = os.path.join(os.getcwd(),'pawan')
        client = Userservices(
                    os.getcwd(),
                    userpath,
                    'pawan',
                    '12345'
                )
        inputvalues = [
            ['group','user'],
            ['testfolder','user'],
            ['..','user'],
            ['..','user'],
        ]
        pathlist = [
            os.path.join(userpath,'group'),
            userpath
        ]
        expectedvalues = [
            f'directory changed to {pathlist[0]}',
            'file not found',
            f'directory changed to {pathlist[1]}',
            'access denied'
        ]
        result = []
        for inputv in inputvalues:
            result.append(client.change_directory(inputv[0],inputv[1]))
        self.assertListEqual(result, expectedvalues)
    
    def test_read_file(self):
        userpath = os.path.join(os.getcwd(),'pravallika')
        client = Userservices(
                    os.getcwd(),
                    userpath,
                    'pawan',
                    '12345'
                )
        inputvalues = [
            [None],
            ['test.txt'],
            [None],
            ['asdf.txt'],
            ['folder1']
        ]
        expectedvalues = [
            'Invalid argument',
            'hello my name is pravallika\n',
            'File Closed',
            'file doesnot exist',
            'Requested file is a folder'
        ]
        result = []
        for inputv in inputvalues:
            result.append(client.start_read(inputv[0]))
        self.assertListEqual(result, expectedvalues)

    def test_delete_file(self):
        client = Adminservices(
                    os.getcwd(),
                    os.getcwd(),
                    'pawan',
                    '12345'
                )
        inputvalues = [
            ['pawan','12345','admin'],
            ['lasya','23423','user'],
            ['lasya','12345','user']
        ]
        expectedvalues = [
            'You cannot delete your self',
            'Un-Authorized',
            'User Deleted'
        ]
        result = []
        for inputv in inputvalues:
            result.append(client.delete_user(inputv[0],inputv[1],inputv[2]))
        self.assertListEqual(result, expectedvalues)
if __name__ == '__main__':
    unittest.main()

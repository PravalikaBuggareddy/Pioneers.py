"""
This module contains the file management system 
"""
import asyncio

def start():
    print('******* File management System by Pioneers *******')
    while True:
        print('1 : Login ')
        print('2 : Register ')
        ch = input('Enter Choice(1,2): ')
        if ch == '1':
            result = login()
            return result
        elif ch == '2': 
            result = register()
            return result
        else:
            print('Invalid Input ')

def login():
    print('**** Login *****')
    user_name = input('User Name : ')
    password  = input('Password : ')
    result = str(f'login {user_name} {password}')
    return result

def register():
    print('**** Register *****')
    user_name = input('Create User Name : ')
    password  = input('Create Password : ')
    prevelige  = input('Enter prevelage(admin/user) : ')
    if prevelige == 'admin' or prevelige == 'user':
        result = str(f'register {user_name} {password} {prevelige}')
        return result
    else:
        return 'invalid'

def log():
    return 0


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    message = ''

    while True:
        request = start()
        writer.write(request.encode())
        data = await reader.read(10000)
        message = data.decode()
        if message == 'successful':
            print('Login Successful ')
            break
        elif message == 'Created':
            print('New user Created')
            break
        elif message == 'exist':
            print('User Already Exist ')
            print('Try again with new Username')
            continue
        elif message == 'failed':
            print('Login Failed ')
            print('Try Again')
            continue
        elif message == 'invalid':
            print('invalid input ')
        else:
            print('Error has Occured, Please Try Again ')
            continue

    while True:
        message = input('pioneers.py>')
        
        if message == 'quit':
            writer.write(message.encode())
            break
        elif message == '':
            continue

        writer.write(message.encode())
        data = await reader.read(10000)
        print(f'{data.decode()}')
    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client())
from server_class import Server
import asyncio
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)
client_dictonery = {}

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    client_dictonery[addr[1]] = Server()
    print(message)
    while True:
        data = await reader.read(10000)
        message = data.decode().strip()
        if message == 'quit':
            break
        
        print(f"Received {message} from {addr}")
        reply = client_dictonery[addr[1]].split(message)
        print(f"Send: {reply}")
        #hello = 'successful'
        writer.write(reply.encode())
        await writer.drain()
    print("Close the connection")
    writer.close()


async def main():
    ip = '127.0.0.1'
    port = 8888
    server = await asyncio.start_server(
        handle_echo, ip, port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
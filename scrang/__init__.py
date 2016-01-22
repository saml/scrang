import asyncio
import aiohttp.web

class App(object):
    def start(self, loop=None, host='*', port=5000):
        loop = asyncio.get_event_loop() if loop is None else loop
        web_app = aiohttp.web.Application(loop=loop)
        handler = web_app.make_handler()
        future_server = loop.create_server(handler, host, port)
        server = loop.run_until_complete(future_server)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            loop.run_until_complete(handler.finish_connections(1.0))
            server.close()
            loop.run_until_complete(server.wait_closed())
            loop.run_until_complete(web_app.finish())
        loop.close()

        

def create_app():
    app = App()
    return app

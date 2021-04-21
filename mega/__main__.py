import logging
import asyncio
from aiohttp import web
from pyrogram import idle
from mega.telegram import MegaDLBot
from mega.webserver import web_server
from mega.common import Common


async def main():
    await MegaDLBot.start()
    runner = web.AppRunner(await web_server())
    await runner.setup()
    bind_address = "0.0.0.0" if Common().is_env else Common().web_fqdn
    await web.TCPSite(runner, bind_address, Common().web_port).start()
    logging.info(f"Web Server Started at: {bind_address}:{Common().web_port}")
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.error("KeyboardInterruption: Services Terminated!")

import logging 
import asyncio
from concurrent import futures

import grpc.aio as aiogrpc

import config
import storage.db as db


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s",
    handlers=[
        logging.FileHandler("logs/logs.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


async def serve() -> None:
    session = db.Session()
    server = aiogrpc.server(futures.ThreadPoolExecutor(max_workers=10))
    listen_addr = f'{config.SERVER_ADDR}:{config.SERVER_PORT}'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())

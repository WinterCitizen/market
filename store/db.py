from motor.motor_asyncio import AsyncIOMotorClient
import settings


def init_db(loop):
    if settings.MONGO_URI is not None:
        client = AsyncIOMotorClient(
            settings.MONGO_URI, io_loop=loop)
    else:
        client = AsyncIOMotorClient(
            settings.MONGO_HOST, settings.MONGO_PORT, io_loop=loop)
    return client[settings.MONGO_DB_NAME]


def get_collection(db, collection):
    return db[collection]

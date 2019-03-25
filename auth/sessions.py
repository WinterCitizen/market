from store.db import get_collection
from uuid import uuid4
from datetime import datetime, timezone
from auth.exceptions import SessionNotFound


def get_sessions_collection(db):
    return get_collection(db, 'sessions')


class Session:
    def __init__(self, db, id, created_at):
        self.db = db
        self.sessions = get_sessions_collection(db)

        self.id = id
        self.created_at = created_at

    @classmethod
    async def insert(cls, sessions, data):
        return await sessions.insert_one(data)

    @classmethod
    async def find(cls, sessions, data):
        return await sessions.find_one(data)

    @classmethod
    async def create(cls, db):
        data = dict(
            id=str(uuid4()),
            created_at=datetime.now(tz=timezone.utc))

        sessions = get_sessions_collection(db)
        await cls.insert(sessions, data)

        return cls(db, data['id'], data['created_at'])

    @classmethod
    async def obtain(cls, db, id):
        sessions = get_sessions_collection(db)
        result = await cls.find(sessions, dict(id=id))

        if result is None:
            raise SessionNotFound()

        created_at = result['created_at'].replace(tzinfo=timezone.utc)

        return cls(db, result['id'], created_at)

    def get_cookie_value(self):
        return self.id

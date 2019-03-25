from aiohttp.web import middleware

from auth.exceptions import SessionNotFound
from auth.sessions import Session


@middleware
class SessionMiddleware:
    SESSION_COOKIE = 'session'

    def get_session_id(self, request):
        return request.cookies.get(self.SESSION_COOKIE)

    def session_cookie_redirect(self, response, session):
        response.set_cookie(self.SESSION_COOKIE, session.session_id)

        return response

    async def create_session(self, db):
        return await Session.create(db), True

    async def obtain_session(self, db, session_id):
        try:
            return await Session.obtain(db, session_id), False
        except SessionNotFound:
            return await Session.create(db), True

    async def get_session(self, request):
        db = request.app['db']
        session_id = self.get_session_id(request)

        if session_id is None:
            return await self.create_session(db)
        else:
            return await self.obtain_session(db, session_id)

    def set_session_cookie(self, response, session):
        response.set_cookie('session', session.get_cookie_value())

    async def __call__(self, request, handler):
        session, created = await self.get_session(request)
        request.session = session

        response = await handler(request)

        if created:
            self.set_session_cookie(response, session)

        return response

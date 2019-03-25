#!/usr/bin/env python
from asyncio import get_event_loop

import aiohttp_jinja2
import jinja2
from aiohttp import web

from auth.middlewares import SessionMiddleware
from doors.views import routes as doors_routes
from contacts.views import routes as contacts_routes
from admin.views import routes as admin_routes
from store.db import init_db
import settings
import os


def add_routes(app):
    app.add_routes(doors_routes)
    app.add_routes(contacts_routes)
    app.add_routes(admin_routes)

    if settings.DEBUG:
        app.add_routes([web.static('/static', settings.STATIC_ROOT)])
        app.add_routes([web.static('/media', settings.MEDIA_ROOT)])


def load_templates(app):
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            settings.TEMPLATE_DIRS))


def init_app(loop):
    app = web.Application(
        middlewares=[SessionMiddleware()],
        client_max_size=1024 * 1024 * 100)
    app['db'] = init_db(loop)
    add_routes(app)

    load_templates(app)

    return app


def main(port):
    loop = get_event_loop()

    app = init_app(loop)
    web.run_app(app, port=port)


if __name__ == '__main__':
    main(int(os.environ.get('PORT', 8001)))

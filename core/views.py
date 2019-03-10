from aiohttp import web
import aiohttp_jinja2
from store.db import get_collection


class TemplateView(web.View):
    template = None
    collection = None

    def get_db(self):
        return self.request.app['db']

    def get_collection(self):
        db = self.get_db()
        return get_collection(db, self.collection)

    async def get_context(self):
        return {}

    def template_response(self, context):
        return aiohttp_jinja2.render_template(
            self.template, self.request, context)

    async def get(self):
        context = await self.get_context()
        return self.template_response(context)

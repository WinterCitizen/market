from core.views import TemplateView
from aiohttp.web import RouteTableDef

routes = RouteTableDef()


@routes.view('/contacts/')
class ContactsView(TemplateView):
    template = 'contacts/index.jinja2'

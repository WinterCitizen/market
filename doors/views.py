from aiohttp.web import Response, RouteTableDef, HTTPNotFound
import aiohttp_jinja2
from core.views import TemplateView
from bson import ObjectId

routes = RouteTableDef()


@routes.view('/doors/')
class DoorListView(TemplateView):
    template = 'doors/list.jinja2'
    collection = 'doors'

    async def get_context(self):
        doors = await self.get_doors()
        return {
            'doors': await self.get_doors(),
        }

    async def get_doors(self):
        doors = self.get_collection()

        cursor = doors.find()

        return [door async for door in cursor]

    


@routes.view('/doors/{id:\w+}/')
class DoorDetailView(TemplateView):
    template = 'doors/detail.jinja2'
    collection = 'doors'

    async def get_door(self):
        _id = self.request.match_info['id']
        doors = self.get_collection()

        door = await doors.find_one({'_id': ObjectId(_id)})
        if door is None:
            raise HTTPNotFound()

        return door

    async def get_context(self):
        doors = self.get_collection()

        return {
            'door': await self.get_door(),
        }



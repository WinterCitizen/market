import asyncio
import os
from concurrent.futures.thread import ThreadPoolExecutor
from uuid import uuid4

import aiohttp_jinja2
from aiohttp.web import HTTPFound, HTTPNotFound, Response, RouteTableDef
from bson import ObjectId
from funcy import pluck_attr

from core.views import TemplateView
from doors.doors import Door
from settings import MEDIA_ROOT

routes = RouteTableDef()


class AddDoorView(TemplateView):
    collection = 'doors'
    category = None

    async def get_context(self):
        return dict(
            category=Door.get_categories(self.category),
        )

    def get_file_extension(self, file_):
        file_name = file_.filename
        *_, extension = file_name.split('.')

        return extension

    def save_file(self, image_file, path):
        with open(path, 'wb') as f:
            f.write(image_file.read())

    async def save_image(self, image):
        extension = self.get_file_extension(image)
        file_name = f'{str(uuid4())}.{extension}'
        path = os.path.join(MEDIA_ROOT, file_name)
        url = f'/media/{file_name}'
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            ThreadPoolExecutor(),
            self.save_file,
            image.file,
            path)

        return url

    async def save_images(self, images):
        return await asyncio.gather(*map(self.save_image, images))

    async def save_door(self, data):
        image_urls = await self.save_images(data.getall('images'))
        doors = self.get_collection()

        insert_data = {**data, 'images': image_urls}

        await doors.insert_one(insert_data)

    async def post(self):
        data = await self.request.post()
        await self.save_door(data)
        raise HTTPFound(self.request.path)


@routes.view('/add-interroom/')
class AddInterroomDoorView(AddDoorView):
    template = 'admin/add-door.jinja2'
    category = Door.INTERROOM


@routes.view('/add-entrance/')
class AddEntranceDoorView(AddDoorView):
    template = 'admin/add-door.jinja2'
    category = Door.ENTRANCE

from pymongo import MongoClient
from PIL import Image
from doors import models
from django.db import transaction
from django.core.files import File
from decimal import Decimal
from itertools import count


def get_or_create(model, **kwargs):
    obj, _ = model.objects.get_or_create(**kwargs)
    return obj


counter = count()


@transaction.atomic
def main():
    db = MongoClient('localhost')['market']
    doors = db['doors']

    door_names = set()

    for door in doors.find():
        if door['name'] in door_names:
            continue
        door_names.add(door['name'])
        door_obj = get_or_create(
            models.Door,
            subcategory=get_or_create(
                models.Subcategory,
                title=door['subcategory'],
                category=get_or_create(models.Category, title=door['category'])),
            manufacturer=get_or_create(models.Manufacturer, title=door['manufacturer']),
            frame_material=get_or_create(models.FrameMaterial, title=door['frame_material']),
            cover_material=get_or_create(models.CoverMaterial, title=door['cover_material']),
            thickness=door['thickness'],
            price=Decimal(door['price']+'.0'),
            title=door['name'],
        )
        heights = door['measurements'].split('х')[0].split(',')
        for height in heights:
            height_obj = get_or_create(models.Height, value=height)
            door_obj.heights.add(height_obj)

        delimiter = '/' if '/' in door['measurements'].split('х')[1] else ','
        widths = door['measurements'].split('х')[1].split(delimiter)
        for width in widths:
            width_obj = get_or_create(models.Width, value=width)
            door_obj.widths.add(width_obj)

        packings = door['packing'].split(',')
        for packing in packings:
            packing_obj = get_or_create(models.PackingMaterial, title=packing)
            door_obj.packings.add(packing_obj)

        file_name = door['images'][0][1:]
        im = Image.open(file_name)
        colors = im.getcolors(2**24)
        color_tuple = max(colors, key=lambda c: c[0])[1]
        color = '#'

        for item in color_tuple:
            color += hex(item)[2:]

        color_obj = get_or_create(models.Color, value=color, defaults=dict(title=str(next(counter))))
        get_or_create(
            models.Picture,
            image=File(open(file_name, 'rb')),
            color=color_obj,
            door=door_obj)

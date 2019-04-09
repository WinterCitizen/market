from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

        unique_together = ('title', 'category')

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'

    def __str__(self):
        return self.title


class FrameMaterial(models.Model):
    title = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'каркас полотна'
        verbose_name_plural = 'каркасы полотна'

    def __str__(self):
        return self.title


class CoverMaterial(models.Model):
    title = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'отделка'
        verbose_name_plural = 'отделки'

    def __str__(self):
        return self.title


class Height(models.Model):
    value = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = 'высота'
        verbose_name_plural = 'высоты'

    def __str__(self):
        return str(self.value)


class Width(models.Model):
    value = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = 'ширина'
        verbose_name_plural = 'ширины'

    def __str__(self):
        return str(self.value)


class PackingMaterial(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'упаковка'
        verbose_name_plural = 'упаковки'

    def __str__(self):
        return self.title


class Door(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    subcategory = models.ForeignKey(
        Subcategory, verbose_name='подкатегория', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name='производитель', on_delete=models.PROTECT)
    frame_material = models.ForeignKey(
        FrameMaterial, verbose_name='каркас полотна', on_delete=models.PROTECT)
    cover_material = models.ForeignKey(
        CoverMaterial, verbose_name='отделка', on_delete=models.PROTECT)
    heights = models.ManyToManyField(Height, verbose_name='высоты', blank=True)
    widths = models.ManyToManyField(Width, verbose_name='ширины', blank=True)
    thickness = models.PositiveIntegerField(
        verbose_name='толщина полотна (мм)')
    packings = models.ManyToManyField(
        PackingMaterial, verbose_name='материалы упаковки', blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='цена')

    class Meta:
        verbose_name = 'дверь'
        verbose_name_plural = 'двери'

        unique_together = (
            'title',
            'manufacturer',
            'frame_material',
            'cover_material',
            'thickness',
        )

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=32, unique=True)
    value = models.CharField(max_length=7, unique=True)

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    door = models.ForeignKey(Door, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

        unique_together = (
            ('image', 'color'),
            ('image', 'color', 'door'),
        )

    def __str__(self):
        door = str(self.door)
        color = str(self.color)

        return f'{door} - {color}'

from django import forms
from django.forms.widgets import TextInput
from doors import models
from django.utils.functional import lazy
from functools import partial


class ColorModelForm(forms.ModelForm):
    class Meta:
        model = models.Door
        fields = '__all__'

        widgets = {
            'value': TextInput(attrs=dict(type='color')),
        }


class DoorFilterForm(forms.Form):
    title__icontains = forms.CharField(required=False, label='Название')
    manufacturer__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Производитель',
        choices=lazy(
            partial(
                models.Manufacturer.objects.values_list, 'id', 'title'),
            tuple,
        ),
        required=False)
    subcategory__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Категория',
        choices=lazy(
            partial(
                models.Subcategory.objects.values_list, 'id', 'title'),
            tuple,
        ),
        required=False)
    frame_material__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Каркас полотна',
        choices=lazy(
            partial(
                models.FrameMaterial.objects.values_list, 'id', 'title'),
            tuple,
        ),
        required=False)
    cover_material__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Отделка',
        choices=lazy(
            partial(
                models.CoverMaterial.objects.values_list, 'id', 'title'),
            tuple,
        ),
        required=False)
    heights__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Высота',
        choices=lazy(
            partial(
                models.Height.objects.values_list, 'id', 'value'),
            tuple,
        ),
        required=False)
    widths__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Ширина',
        choices=lazy(
            partial(
                models.Width.objects.values_list, 'id', 'value'),
            tuple,
        ),
        required=False)
    packings__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Ширина',
        choices=lazy(
            partial(
                models.PackingMaterial.objects.values_list, 'id', 'title'),
            tuple,
        ),
        required=False)
    price__gte = forms.IntegerField(
        min_value=0, label='Цена от', required=False)
    price__lte = forms.IntegerField(
        min_value=0, label='Цена до', required=False)
    thickness = forms.IntegerField(
        min_value=0, label='Толщина полотна (мм)', required=False)

from django import forms
from django.forms.widgets import TextInput
from doors import models


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
        choices=models.Manufacturer.objects.values_list('id', 'title'),
        required=False)
    subcategory__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Категория',
        choices=models.Subcategory.objects.values_list('id', 'title'),
        required=False)
    frame_material__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Каркас полотна',
        choices=models.FrameMaterial.objects.values_list('id', 'title'),
        required=False)
    cover_material__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Отделка',
        choices=models.CoverMaterial.objects.values_list('id', 'title'),
        required=False)
    heights__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Высота',
        choices=models.Height.objects.values_list('id', 'value'),
        required=False)
    widths__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Ширина',
        choices=models.Width.objects.values_list('id', 'value'),
        required=False)
    packings__in = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Ширина',
        choices=models.PackingMaterial.objects.values_list('id', 'title'),
        required=False)
    price__gte = forms.IntegerField(
        min_value=0, label='Цена от', required=False)
    price__lte = forms.IntegerField(
        min_value=0, label='Цена до', required=False)
    thickness = forms.IntegerField(
        min_value=0, label='Толщина полотна (мм)', required=False)

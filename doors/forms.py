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


class DoorFilterForm(forms.ModelForm):
    class Meta:
        model = models.Door
        exclude = ('price', )

    title = forms.CharField(required=False, label='Название')
    manufacturer = forms.ModelMultipleChoiceField(
        queryset=models.Manufacturer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Производитель',
        required=False)
    subcategory = forms.ModelMultipleChoiceField(
        queryset=models.Subcategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Категория',
        required=False)
    frame_material = forms.ModelMultipleChoiceField(
        queryset=models.FrameMaterial.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Каркас полотна',
        required=False)
    cover_material = forms.ModelMultipleChoiceField(
        queryset=models.CoverMaterial.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Отделка',
        required=False)
    price_from = forms.IntegerField(
        min_value=0, label='Цена от', required=False)
    price_to = forms.IntegerField(
        min_value=0, label='Цена до', required=False)
    thickness = forms.IntegerField(
        min_value=0, label='Толщина полотна (мм)', required=False)

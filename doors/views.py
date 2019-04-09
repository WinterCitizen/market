from django.conf import settings
from django.views.generic import ListView, DetailView
from django.http import HttpResponseBadRequest

from doors.models import Door, Picture
from doors.forms import DoorFilterForm


class DoorsListView(ListView):
    template_name = 'doors/list.djt'
    queryset = Door.objects.all().order_by('pk')
    paginate_by = settings.DOORS_PER_PAGE
    cleaned_data = None

    def get_form(self):
        if self.request.method == 'POST':
            return DoorFilterForm(self.request.POST)
        else:
            return DoorFilterForm()

    def clean_data(self, cleaned_data):
        for key, value in cleaned_data.items():
            if not value:
                continue

            if isinstance(value, list):
                value = list(map(int, value))

            yield key, value

    def perform_filter(self, queryset):
        return queryset.filter(**self.cleaned_data).distinct()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.cleaned_data is not None:
            return self.perform_filter(queryset)

        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = self.get_form()
        return context

    def post(self, request, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return HttpResponseBadRequest()
        else:
            self.cleaned_data = dict(self.clean_data(form.cleaned_data))

        return super().get(request, **kwargs)


class DoorDetailView(DetailView):
    template_name = 'doors/detail.djt'
    queryset = Door.objects.all().order_by('pk')

    def get_heights(self):
        obj = self.get_object()

        return '/'.join(map(str, obj.heights.all()))

    def get_widths(self):
        obj = self.get_object()

        return '/'.join(map(str, obj.widths.all()))

    def get_packings(self):
        obj = self.get_object()

        return ', '.join(map(str, obj.packings.all()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_picture'] = Picture.objects.get(pk=self.picture_pk)
        context['measurements'] = f'{self.get_heights()}x{self.get_widths()}'
        context['packings'] = self.get_packings()
        return context

    def get(self, request, picture_pk, **kwargs):
        self.picture_pk = picture_pk
        return super().get(request, **kwargs)

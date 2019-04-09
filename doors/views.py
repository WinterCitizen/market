from django.conf import settings
from django.views.generic import ListView, DetailView

from doors.models import Door, Picture
from doors.forms import DoorFilterForm


class DoorsListView(ListView):
    template_name = 'doors/list.djt'
    queryset = Door.objects.all().order_by('pk')
    paginate_by = settings.DOORS_PER_PAGE

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = DoorFilterForm()
        return context

    def post(self, *args, **kwargs):
        import ipdb; ipdb.set_trace()


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

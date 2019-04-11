from django.views.decorators.http import require_POST
from django.http.response import HttpResponseRedirect


@require_POST
def add_to_card(request, door, picture):
    if request.session.get('card') is None:
        request.session['card'] = []

    request.session['card'].append((door, picture, 1))
    request.session.save()

    return HttpResponseRedirect(request.GET['redirect_to'])

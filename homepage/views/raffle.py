from django.conf import settings
from django_mako_plus import view_function, jscontext
from homepage import models as hmod
from django.db.models import Sum
from random import shuffle

@view_function
def process_request(request):
    h = hmod.Person.objects.filter(raffle='A').order_by('?').first()
    if h is not None:
        name = h.first_name + ' ' + h.last_name
        h.raffle = 'I'
        h.save()
        button = '<a id="button" class="btn btn-primary" href="">Go Again</a>'
    else:
        name = "That's all folks!"
        button = '<a id="button" class="btn btn-primary" href="/homepage/rafflestart">Refresh the raffle?</a>'

    context = {
        # sent to index.html and index.js:
        jscontext('name'): name,
        jscontext('button'): button,
    }
    return request.dmp.render('raffle.html', context)

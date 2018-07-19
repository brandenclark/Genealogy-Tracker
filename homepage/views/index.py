from django.conf import settings
from django_mako_plus import view_function, jscontext
from homepage import models as hmod
from django.db.models import Sum

@view_function
def process_request(request):
    names = hmod.Person.objects.all().aggregate(Sum('names'))['names__sum']
    ordinances = hmod.Person.objects.all().aggregate(Sum('ordinances'))['ordinances__sum']
    if names is None:
        names = 0
    if ordinances is None:
        ordinances = 0
    context = {
        # sent to index.html and index.js:
        jscontext('names'): names,
        jscontext('ordinances'): ordinances,
    }
    return request.dmp.render('index.html', context)

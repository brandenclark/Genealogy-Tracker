from django.conf import settings
from django_mako_plus import view_function, jscontext
from homepage import models as hmod
from django.db.models import Sum
from random import shuffle

@view_function
def process_request(request):
    for p in hmod.Person.objects.all():
        p.raffle = 'A'
        p.save()

    return request.dmp.render('rafflestart.html')

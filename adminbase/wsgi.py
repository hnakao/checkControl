import schedule
import time
import threading
# para el trabajo con las fechas
from datetime import datetime, date, timedelta

from dashboard.models import Bank, PayCheck, Mensajes

"""
WSGI config for adminbase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adminbase.settings")

"""aqui porner lo que se ejecutara una sola ver"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# esta funcion se ejecutara cada un dia para verificar
# la fecha de los cheques
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def job1():
        print("I'm job...")
        chekes = PayCheck.objects.filter(pagado = 0)
        chekes_at_date = PayCheck.objects.filter(at_date__gte = date.today(),pagado = 0)
        chekes_post_date = PayCheck.objects.filter(post_date__gte = date.today(),pagado = 0)

        Mensajes.objects.all().delete()

        for check_at_date in chekes_at_date:
            estado = check_at_date.at_date - date.today()
            print(estado)
            if estado == timedelta(days = 5):
                check_at_date.estado = 5
                check_at_date.save()
                mensaje = Mensajes(user = check_at_date.user, fecha = date.today(), prioridad = 2, mensaje="Tiene un cheque con 5 dias para su fecha de pago.", leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 2):
                check_at_date.estado = 2
                check_at_date.save()
                mensaje = Mensajes(user=check_at_date.user, fecha=date.today(), prioridad=2,
                                   mensaje="Cheque número: %s, con 2 dias para su fecha de pago."%(check_at_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 1):
                check_at_date.estado = 1
                check_at_date.save()
                mensaje = Mensajes(user=check_at_date.user, fecha=date.today(), prioridad=3,
                                   mensaje="Cheque número: %s, con 1 dia para su fecha de pago."%(check_at_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 0):
                check_at_date.estado = 0
                check_at_date.save()
                mensaje = Mensajes(user=check_at_date.user, fecha=date.today(), prioridad=4,
                                   mensaje="Cheque número: %s, para pagar hoy."%(check_at_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")

        for check_post_date in chekes_post_date:
            print (check_post_date.post_date)
            estado = check_post_date.post_date - date.today()
            print(estado)

            if estado == timedelta(days = 5):
                check_post_date.estado = 5
                check_post_date.save()
                mensaje = Mensajes(user = check_post_date.user, fecha = date.today(), prioridad = 2, mensaje="Cheque número: %s, tiene 5 dias para su fecha de post date"%(check_post_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 2):
                check_post_date.estado = 2
                check_post_date.save()
                mensaje = Mensajes(user=check_post_date.user, fecha=date.today(), prioridad=2,
                                   mensaje="Cheque número: %s, tiene 2 dias para su fecha de post date" % (
                                       check_post_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 1):
                check_post_date.estado = 1
                check_post_date.save()
                mensaje = Mensajes(user=check_post_date.user, fecha=date.today(), prioridad=3,
                                   mensaje="Cheque número: %s, tiene 1 dia para su fecha de post date" % (
                                       check_post_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")
            elif estado == timedelta(days = 0):
                check_post_date.estado = 0
                check_post_date.save()
                mensaje = Mensajes(user=check_post_date.user, fecha=date.today(), prioridad=4,
                                   mensaje="Cheque número: %s, para pagar hoy." % (
                                       check_post_date.check_number), leido="no")
                mensaje.save()
                print ("+++++++++++++++++++++++++++++++++++++++++++++++")

            check_post_date.save()


def job():
    schedule.every(0.5).minutes.do(job1)
    while True:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target = job)
t.start()



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

application = get_wsgi_application()



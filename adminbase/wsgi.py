import schedule
import time
import threading
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

def job():
	schedule.every(0.2).minutes.do(job1)
	while True:
		schedule.run_pending()
		time.sleep(1)

t = threading.Thread(target = job)
t.start()



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

application = get_wsgi_application()



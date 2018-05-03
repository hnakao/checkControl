from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import RegistroUserForm, PayCheckForm

from dashboard.models import Bank, PayCheck

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# index
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def index_view(request):
    banks = Bank.objects.all()
    context = {
        'banks': banks,
    }
    return render(request, 'components/index.html', context)



class BlankView(TemplateView):
    template_name = "components/blank.html"

    def get_context_data(self, **kwargs):
        context = super(BlankView, self).get_context_data(**kwargs)
        context.update({'title': "Blank Page"})
        return context


class ButtonsView(TemplateView):
    template_name = "components/buttons.html"

    def get_context_data(self, **kwargs):
        context = super(ButtonsView, self).get_context_data(**kwargs)
        context.update({'title': "Buttons"})
        return context


class FlotView(TemplateView):
    template_name = "components/flot.html"

    def get_context_data(self, **kwargs):
        context = super(FlotView, self).get_context_data(**kwargs)
        context.update({'title': "Flot Charts"})
        return context


class FormsView(TemplateView):
    template_name = "components/forms.html"

    def get_context_data(self, **kwargs):
        context = super(FormsView, self).get_context_data(**kwargs)
        context.update({'title': "Forms"})
        return context


class GridView(TemplateView):
    template_name = "components/grid.html"

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context.update({'title': "Grid"})
        return context


class IconsView(TemplateView):
    template_name = "components/icons.html"

    def get_context_data(self, **kwargs):
        context = super(IconsView, self).get_context_data(**kwargs)
        context.update({'title': "Icons"})
        return context
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# login view
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def login_view(request):
    message = ''
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('dashboard:index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff and user.is_active:
                login(request, user)
                return redirect(reverse('dashboard:index'))

            # verificar que halla verificado su cuenta desde el link de activacion enviado en el email
            """if UserProfile.objects.get(user=user.id).verificado_email != 1:
                print("no ha verificado el email")
                message = 'Para acceder al sitio debe de verificar su email. <a href="#" onclick="reenviar_email_activacion(%s)">Reenviar email</a>.' % (
                    user.id)
                form = Forgot_Password_Form()
                context = {
                    'form': form,
                    'message': message,
                }
                return render(request, 'accounts/login.html', {'message': message})"""
            if user.is_active:
                login(request, user)
                return redirect(reverse('dashboard:index'))
            else:
                message = 'Su cuenta no esta activa.'
                return render(request, 'components/login.html', {'message': message})
        else:
            # Redireccionar informando que la cuenta esta inactiva
            pass
            message = 'Nombre de usuario o contraseña incorrecto.'

    #form = Forgot_Password_Form()
    context = {
        #'form': form,
        'message': message,
    }

    return render(request, 'components/login.html', context)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# logout_view
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def logout_view(request):
    logout(request)
    #message.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('dashboard:login'))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Registrar Usuario
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def registro_usuario_view(request):
	if request.method == 'POST':
	# Si el method es post, obtenemos los datos del formulario
		form = RegistroUserForm(request.POST, request.FILES)
			# Comprobamos si el formulario es valido
		if form.is_valid():
			# En caso de ser valido, obtenemos los datos del formulario.
			# form.cleaned_data obtiene los datos limpios y los pone en un
			# diccionario con pares clave/valor, donde clave es el nombre del campo
			# del formulario y el valor es el valor si existe.
			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			password = cleaned_data.get('password')
			email = cleaned_data.get('email')
			photo = cleaned_data.get('photo')
			nombre = cleaned_data.get('nombre')
			apellidos = cleaned_data.get('apellidos')
			# E instanciamos un objeto User, con el username y password
			user_model = User.objects.create_user(username=username, password=password)
			# Añadimos el email
			user_model.nombre = nombre
			user_model.apellidos = apellidos
			user_model.email = email
			# Y guardamos el objeto, esto guardara los datos en la db.
			user_model.save()



			# Se llama al proceso que envía el mail
			# Email.enviar_correo_registro_usuario(usuario = user_profile, host = request.get_host())

			message = 'Para acceder al sitio debe de verificar su email.'
			return render(request, 'components/login.html', {'message': message})
	else:
	# Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
		form = RegistroUserForm()
	# Creamos el contexto
	context = {'form': form}
	# Y mostramos los datos
	return render(request, 'components/singup_user.html', context)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  chekes
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def chekes_view(request):
    if request.method == 'GET':
        # obtener todos los chekes del usuario logueado
        chekes = PayCheck.objects.filter(user = request.user.id)
        form = PayCheckForm()
        context = {
            'chekes' : chekes,
            'form' : form,
        }
        return render(request, 'components/chekes.html', context)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class MorrisView(TemplateView):
    template_name = "components/morris.html"

    def get_context_data(self, **kwargs):
        context = super(MorrisView, self).get_context_data(**kwargs)
        context.update({'title': "Morris Charts"})
        return context


class NotificationsView(TemplateView):
    template_name = "components/notifications.html"

    def get_context_data(self, **kwargs):
        context = super(NotificationsView, self).get_context_data(**kwargs)
        context.update({'title': "Notifications"})
        return context


class PanelsView(TemplateView):
    template_name = "components/panels-wells.html"

    def get_context_data(self, **kwargs):
        context = super(PanelsView, self).get_context_data(**kwargs)
        context.update({'title': "Panels and Wells"})
        return context


class TablesView(TemplateView):
    template_name = "components/tables.html"

    def get_context_data(self, **kwargs):
        context = super(TablesView, self).get_context_data(**kwargs)
        context.update({'title': "Tables"})
        return context


class TypographyView(TemplateView):
    template_name = "components/typography.html"

    def get_context_data(self, **kwargs):
        context = super(TypographyView, self).get_context_data(**kwargs)
        context.update({'title': "Typography"})
        return context

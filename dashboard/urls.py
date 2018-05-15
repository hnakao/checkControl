from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.registro_usuario_view, name="register"),
    url(r'^index/$', views.index_view, name="index"),
    url(r'^chekes/$', views.chekes_view, name="chekes"),
    url(r'^chekes2/(\d{1,1000})$', views.chekes2_view, name="chekes2"),
    url(r'^cheque_modal/$', views.cheque_modal_view, name="cheque_modal"),
    url(r'^filtrar/$', views.filtrar_view, name="filtrar"),
    url(r'^mostrar_mensajes/$', views.mostrar_mensajes, name="mostrar_mensajes"),
url(r'^eliminar_mensaje/(\d{1,1000})$', views.eliminar_mensaje, name="eliminar_mensaje"),

    url(r'^blank/$', views.BlankView.as_view(), name="blank"),
    url(r'^buttons/$', views.ButtonsView.as_view(), name="buttons"),
    url(r'^flot/$', views.FlotView.as_view(), name="flot"),
    url(r'^forms/$', views.FormsView.as_view(), name="forms"),
    url(r'^grid/$', views.GridView.as_view(), name="grid"),
    url(r'^icons/$', views.IconsView.as_view(), name="icons"),
    url(r'^morris/$', views.MorrisView.as_view(), name="morris"),
    url(r'^notifications/$', views.NotificationsView.as_view(), name="notifications"),
    url(r'^panels/$', views.PanelsView.as_view(), name="panels"),
    url(r'^tables/$', views.TablesView.as_view(), name="tables"),
    url(r'^typography/$', views.TypographyView.as_view(), name="typography"),
]

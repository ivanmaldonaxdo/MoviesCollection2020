from django.conf.urls import include, url 
from . import views
from .views import ApiMoviesCollections
from rest_framework import routers

router = routers.DefaultRouter()
router.register('peliserie', ApiMoviesCollections)

urlpatterns = [ 
    url(r'^$', views.indexInicio,name='home'),
    url(r'^Register/$', views.register, name="register"),
    url(r'^Login/$', views.login, name="login"),
    url(r'^BiblioPelis/$', views.indexPelis, name="indexPelis"),
    url(r'^BiblioSeries/$', views.indexSeries, name="indexSeries"), 
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detailPeliserie, name='detailPS'),
    url(r'^Mantenedor/$', views.mantenedor, name="mantenedor"), 
    url(r'^PeliSerie/new/$', views.CrearPeliserie, name='new_peliserie'),
    url(r'^PeliSerie/(?P<pk>[0-9]+)/edit/$', views.EditarPeliserie, name='edit_peliserie'),
    url(r'^PeliSerie/(?P<pk>[0-9]+)/delete/$', views.EliminarPeliserie, name='delete_peliserie'),
    url(r'^Carousel/new/$', views.CrearCarousel, name='new_carousel'),
    url(r'^Carousel/(?P<pk>[0-9]+)/edit/$', views.EditarCarousel, name='edit_carousel'),
    url(r'^Carousel/(?P<pk>[0-9]+)/delete/$', views.EliminarCarousel, name='delete_carousel'),
    url(r'^Consultas/$', views.indexConsultas, name='consultas'),
    url(r'^Consultas/(?P<pk>[0-9]+)/delete/$', views.EliminarConsulta, name='delete_consulta'),
    url(r'^api/', include(router.urls)),
    url(r'^', include('pwa.urls'))
]
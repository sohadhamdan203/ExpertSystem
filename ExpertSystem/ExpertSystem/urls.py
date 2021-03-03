from django.conf.urls import include, url
import app.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^home$', app.views.index, name='home'),
]


from django.conf.urls import url
from log.views import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
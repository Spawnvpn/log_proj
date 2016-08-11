from django.conf.urls import url
from log_app import views

app_name = 'logg'

urlpatterns = [
    url(r"^index/$", view=views.index, name="index"),
    # url(r"^test/$", view=views.test, name="test"),
]


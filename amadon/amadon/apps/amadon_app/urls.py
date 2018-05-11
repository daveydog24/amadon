from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/add_item$', views.add_item),
    url(r'^amadon/results$', views.results),
    url(r'^amadon/buy$', views.buy),
    url(r'^amadon/process$', views.process),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^amadon/clear_cart$', views.clear)
]
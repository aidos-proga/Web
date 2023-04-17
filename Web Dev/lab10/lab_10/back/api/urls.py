from rest_framework import routers
from . import views

r = routers.SimpleRouter()

r.register(r'company', views.CompanyModelViewSet)
r.register(r'vacancy', views.VacanciesModelViewSet)

urlpatterns = r.urls

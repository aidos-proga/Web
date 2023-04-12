from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.ReadCompany),
    path('companies/<int:id>/', views.RetrieveCompany),
    path('companies/<int:id>/vacancies/', views.ByCompany),
    path('vacancies/', views.ReadVacancy),
    path('vacancies/<int:id>/', views.RetrieveVacancy),
    path('vacancies/top_ten/', views.TopTenVacancy),
]
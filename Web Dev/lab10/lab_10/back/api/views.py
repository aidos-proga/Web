from django.http import JsonResponse

from . import models, serializer
from rest_framework import viewsets


class CompanyModelViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializer.CompanySerializer


class VacanciesModelViewSet(viewsets.ModelViewSet):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializer.VacancySerializer


def ByCompany(request, **kwargs):
    vacancies = models.Vacancy.objects.filter(company_id=int(kwargs['id']))
    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'salary': i.salary,
    } for i in vacancies]

    return JsonResponse(data=data, safe=False)

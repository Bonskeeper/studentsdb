# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Views for Students


def visit_student(request):
    journals = (
        {
            'id': 1,
            'name': u'Подоба Вiталiй',
        },
        {
            'id': 2,
            'name': u'Корост Андрiй',
        },
        {
            'id': 3,
            'name': u'Притула Тарас',
        }
    )
    return render(request, 'students/visit_students.html', {'journals': journals})

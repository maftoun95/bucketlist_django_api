from __future__ import print_function, unicode_literals

from django.http import HttpResponse
from django.views import View

from django.core import serializers
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Task


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Api(View):

    def get(self, request):
        data = serializers.serialize("json", Task.objects.all())
        return HttpResponse(data)

    def post(self, request, *args, **kwargs):
        newtask = Task()
        newtask.objective = request.body
        newtask.save()
        return HttpResponse("WEEEEOOOOO")

    def patch(self, request, task_id):
        task_to_update = Task.objects.get(pk=task_id)
        task_to_update.objective = request.body
        task_to_update.save()
        data = serializers.serialize("json",
                                     Task.objects.all())
        return HttpResponse(data)

    def delete(self, request, task_id):
        task_to_delete = Task.objects.get(pk=task_id)
        deleted_task = task_to_delete.delete()
        return HttpResponse(Task.objects.all())

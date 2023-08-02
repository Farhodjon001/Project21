from django.shortcuts import render
from .models import Workers
from django.http import JsonResponse
# Create your views here.

def get_all(request):
    if request.method=="GET":
        all_date= Workers.objects.all()
        result=[]
        for worker in all_date:
             result.append({"id":worker.id,"worker_name":worker.first_name})
        return JsonResponse({"date":result})

def get_by_id(request,worker_id):
    if request.method=="GET":
        try:
            date=Workers.objects.get(id=worker_id)
        except Human.DoesNotExists:
            return JsonResponse({"msg": "NOT FOUND"})
        return JsonResponse({"id":date.id,"worker_name":date.first_name})
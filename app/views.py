from django.shortcuts import render, redirect
from django.http import HttpResponse    
from .models import gradregistrationModel


def home(request):
    return render(request, "home.html")

def records(request):
    data = request.GET
    message = data.get('message', '')
    records= gradregistrationModel.objects.all()
    return render(request, "records.html", {"records": records, "message": message })

def profile(request):
    try:
        data = request.GET
        id = data['id']
        record= gradregistrationModel.objects.get(infoID=id)
        return render(request, "profile.html", {"profile": record })

    except:
        message = "record no longer exist for the selected id"
        return redirect('/records/?message=' + message)


def update(request):
    data = request.GET
    id = data['id']
    message = data.get('message', '')
    record= gradregistrationModel.objects.get(infoID=id)
    return render(request, 'update.html', {"profile": record, "message": message })

def delete(request):

    try:
        data = request.GET
        id = data['id']
        message = "Record has been deleted successfully"
        record= gradregistrationModel.objects.get(infoID=id)
        record.delete()
        return redirect('/records/?message=' + message)

    except:
        message = "Record can not be deleted presently, please try again"
        return redirect('/records/?message=' + message)







# Create your views here.
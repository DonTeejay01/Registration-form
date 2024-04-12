from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import gradregistrationModel




def registrationform(request):
    try:
        if request.method == "POST":
            form = request.POST
            saveData = gradregistrationModel.objects.create(
            firstname = form['firstname'],
            lastname = form['lastname'],
            email = form['email'],
            phone = form['phone'],
            department = form['department'],
            matricNum = form['matricNum'],
            parentLastname = form['parentLastname'],
            parentFirstname = form['parentFirstname'],
            parentEmail = form['parentEmail'],
            parentPhone = form['parentPhone']
            )
            message = "Thanks for contacting us"
            return render(request, "home.html", {"message": message })
            
        else:
            message = "INVALID request"
            return render(request, "home.html", {"message": message })
    except Exception as error:
        message = "something went wrong, please try again. Error: ".str(error)
        return render(request, "home.html", {"message": message })


def updateform(request):
    try:
        id = 0
        if request.method == "POST":
            form = request.POST
            id = form['id']
            record = gradregistrationModel.objects.get(infoID=id)
            record.firstname = form['firstname']
            record.lastname = form['lastname']
            record.email = form['email']
            record.phone = form['phone']
            record.department = form['department']
            record.matricNum = form['matricNum']
            record.parentLastname = form['parentLastname']
            record.parentFirstname = form['parentFirstname']
            record.parentEmail = form['parentEmail']
            record.parentPhone = form['parentPhone']
            record.save()
            message = "profile updated successfully"
            return redirect('/update/?id=' + str(id) + '&message=' + message)

            
        else:
            message = "INVALID request"
            return redirect('/records/?message=' + message)
    except Exception as error:
        message = "something went wrong, please try again. Error: ".str(error)
        return redirect('/records/?message=' + message)


from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Consultation, Message
from users.models import User


# Create your views here.
def index(request):
    consultants = User.objects.filter(is_consultant=True)

    context = {
        'consultants': consultants
    }
    return render(request, "consultation/index.html", context)

def consultations(request):
    print(request.user)
    print(request.user.id)
    try:
        user = User.objects.get(pk=request.user.id)
        #print(request.user)
        #consultant = request.user
        print(user)
    except User.DoesNotExist:
        context = {
            'message': "No consultations found"
        }
        print(Consultation.objects.all())
        return render(request, "consultation/consultations.html", context)

    """ try:
        patient = Patient.objects.get(pk=request.user.id)
        #patient = request.user
        print(patient)
    except Patient.DoesNotExist:
        context = {
        'message': "No consultations found"
        }
        print(Consultation.objects.all())
        return render(request, "consultation/consultations.html", context) """

    if user.is_patient == True:
        active_consultations = Consultation.objects.filter(patient=user).filter(is_active=True).order_by('-start_date')
        closed_consultations = Consultation.objects.filter(patient=user).filter(is_active=False).order_by('-start_date')
        print(active_consultations)
        print(closed_consultations)
        for i in active_consultations:
            print(i.patient)
            print(i.consultant)
            print(i.start_date)
        context = {
            #'qualification': consultant.qualification,
            'active_consultations': active_consultations,
            'closed_consultations': closed_consultations
        }
        print(context['active_consultations'])
        print(context['closed_consultations'])
        print(Consultation.objects.all())
        print(user)
        #print(consultant)
        return render(request, "consultation/consultations.html", context)
    else:
        active_consultations = Consultation.objects.filter(consultant=user).filter(is_active=True).order_by('-start_date')
        closed_consultations = Consultation.objects.filter(consultant=user).filter(is_active=False).order_by('-start_date')
        print(active_consultations)
        print(closed_consultations)
        context = {
            #'qualification': consultant.qualification,
            'active_consultations': active_consultations,
            'closed_consultations': closed_consultations
        }
        print(context['active_consultations'])
        print(context['closed_consultations'])
        print(Consultation.objects.all())
        print(user)
        #print(patient)
        return render(request, "consultation/consultations.html", context)

    context = {
        #'qualification': consultant.qualification,
        'active_consultations': active_consultations,
        'closed_consultations': closed_consultations
    }
    print(context['active_consultations'])
    print(context['closed_consultations'])
    print(Consultation.objects.all())
    return render(request, "consultation/consultations.html", context)


@login_required
def consultation(request, room_name):
    if request.method == "GET":
        try:
            if request.user.username == room_name:
                consultant = User.objects.get(pk=request.user.id)
            else:
                consultant = User.objects.get(username=room_name)
                patient = User.objects.get(pk=request.user.id)
            consultation = Consultation.objects.get(name=room_name, consultant=consultant)
            patient = consultation.patient
            consultation = Consultation.objects.get(name=room_name, consultant=consultant, patient=patient)
        except Consultation.DoesNotExist:
            cons = User.objects.get(username=room_name)
            patient = User.objects.get(pk=request.user.id)
            consultation = Consultation(name=room_name, consultant=cons, patient=patient)
            consultation.save()

        messages = []

        if consultation:
            messages = Message.objects.filter(consultation=consultation)

        return render(request, 'consultation/consultation.html', {
            'consultant_name': room_name,
            'messages': messages,
            'consultation': consultation
        })
    else:
        consultation = Consultation.objects.get(name=room_name)
        consultation.is_active = False
        consultation.end_date = date.today()
        #consultation.name = room_name + "-closed"
        consultation.save()
        return render(request, 'consultation/consultation.html', {
            'consultant_name': room_name,
            #'messages': messages,
            'consultation': consultation
        })

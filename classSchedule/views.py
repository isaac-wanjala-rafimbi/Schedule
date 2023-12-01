from django.forms import modelform_factory
from django.shortcuts import render, redirect
from classSchedule.models import PersonData
from classSchedule.models import Schedule

from django.contrib import messages


# Create your views here.
def home(request):
    all_items = Schedule.objects.all()
    return render(request, 'website/index.html', {'all_items': all_items})


def result(request):
    form = Schedule.objects.all()
    return render(request, 'website/resullt.html', {'form': form})


MeetingForm =modelform_factory(Schedule,exclude=[])

def homepage(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("result")
        else:  # Handle the case of an invalid form
            return render(request, 'website/new.html', {"form": form})
    else:  # GET request or any other method, return a blank form
        form = MeetingForm()
        return render(request, 'website/new.html', {"form": form})

def zoomDetails(request):
    meetings = PersonData.objects.all()
    return render(request, 'website/index.html', {'meetings': meetings})

def alright(request):
    all_items=Schedule.objects.all()
    return render(request, 'website/form2.html', {'all_items':all_items})




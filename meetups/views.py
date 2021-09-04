from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
           registration_form = RegistrationForm(request.POST)
           if registration_form.is_valid():
               user_email = registration_form.cleaned_data['email']
               participant, _ = Participant.objects.get_or_create(email=user_email)
               selected_meetup.participants.add(participant)
               return redirect('confirm-registration', meetup_slug = meetup_slug)

               
               
        return render(request, 'meetups/meetup-details.html', {
            'meetup_slug': meetup_slug, 
            'meetup_location': selected_meetup.location, 
            'meetup_description': selected_meetup.description, 
            'meetup_title': selected_meetup.title, 
            'meetup_found': True, 
            'meetup_image': selected_meetup.image.url, 
            'form': registration_form
            })

    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
            })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organiser_email': meetup.organiser_email
    })
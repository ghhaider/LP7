from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import generic
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from lp7.forms import ContactForm, eventBookingForm, packageSpaceForm
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from django.conf import settings
from django.forms import ValidationError
import urllib
import json
from django.core.paginator import Paginator
from django.core.files.uploadedfile import SimpleUploadedFile
from lp7.models import TopBar, Logo, about, \
    BGimages, LP7features, Locations, Events, LP7MembersLogo, LP7Testimonials, Promotions, \
    PricingRawalpindi, PricingIslamabad, PackagePriceFeatures, ContactedUser, eventBooking, \
    packageSpace, galleryRWP, galleryISD



# Home Page View
def index(request):
    # Display all the Dynamic values form models
    aboutLP7 = about.objects.all()
    PMBG = BGimages.objects.all()
    lp7Features = LP7features.objects.all()
    location = Locations.objects.all()
    memberLogo = LP7MembersLogo.objects.all()
    testi = LP7Testimonials.objects.all()
    Prwp = PricingRawalpindi.objects.all()
    Pisd = PricingIslamabad.objects.all()
    Pfeature = PackagePriceFeatures.objects.all()


    #if promotion:
        #promo = Promotions.objects.filter(status='Active')
        #context={'promo': promo}
        #return render(request, 'index.html', context)
    #else:
        #messages.success(request, 'There is no promotional offer running at this time in LaunchPad7.')

    #evn = Events.objects.filter(status='Active').last()
    #if evn:
        #events = Events.objects.filter(status='Active').last()
        #context={'events': events}
        #return render(request, 'index.html', context)
    #else:
        #messages.success(request, 'There is no event being held at this time in LaunchPad7.')

    c = context = ({
    'about': aboutLP7,
    'BG': PMBG,
    'featuresLP7': lp7Features,
    'loc': location,
    'memLogo': memberLogo,
    'testi': testi,
    'Prwp': Prwp,
    'Pisd': Pisd,
    'Pfeature': Pfeature,
    })

    # Render the HTML template index.html
    return render(request, 'index.html', c )


# Location Page View
def locations(request):
     # Display all the Dynamic values form models
     location = Locations.objects.all()


     c = context = ({
      'loc': location,
     })

     # Render the HTML template locations.html
     return render(request, 'locations.html', c,)


# Contact Us Page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                sender_message = form.cleaned_data['message']
                sender_phone = form.cleaned_data['phone']

                message = "{0} has sent you a new message:\n\n{1}".format(sender_phone, form.cleaned_data['message'])
                send_mail('New Contact Information', message, sender_email, ['shakeela.sadaqat@launchpad7.com'])
                form.save()
                messages.success(request, 'Thank you very much for contacting us, one of our \
                correspondent will get back to you soon.')
                # Email setting for contact form
                return redirect('contact')
            else:
                messages.error(request, 'Please complete the Captcha Challenge before pressing the send button.')
                return redirect('contact')

    else:
        form = ContactForm()

    c = context = ({
    'form': form,
    })
    # Render the HTML template contact.html
    return render(request, 'contact.html', c)




# View for Packages Page
def packages(request):
    # Display all the Dynamic values form models
    Prwp = PricingRawalpindi.objects.all()
    Pisd = PricingIslamabad.objects.all()
    addOn = PackagePriceFeatures.objects.all()

    c = context = ({
    'Prwp': Prwp,
    'Pisd': Pisd,
    'addOn': addOn,
    })

    # Render the HTML template packages.html
    return render(request, 'packages.html', c )


# View for Event Booking Page
def BookEvent(request):
    if request.method == 'POST':
        form = eventBookingForm(request.POST, request.FILES)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                sender_message = form.cleaned_data['eventDetail']
                sender_phone = form.cleaned_data['phone']


                message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['eventDetail'])
                send_mail('New Event Booking Information', message, sender_email, ['shakeela.sadaqat@launchpad7.com'])
                form.save()
                messages.success(request, 'Thank you very much for contacting us, one of our \
                correspondent will get back to you soon.')
                # Email setting for contact form
                return redirect('contact')
            else:
                messages.error(request, 'Please complete the Captcha Challenge before pressing the send button.')
                return redirect('BookEvent')

    else:
        form = eventBookingForm()

    c = context = ({
    'form': form,
    })
    # Render the HTML template contact.html
    return render(request, 'BookEvent.html', c)


# View for PackageSpace
def PackageSpace(request):

    if request.method == 'POST':
        form = packageSpaceForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            if result['success']:
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                sender_phone = form.cleaned_data['phone']
                sender_selected_package = form.cleaned_data['selectedPackage']
                sender_selected_location = form.cleaned_data['selectedLocation']
                u = form.save()

                message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['phone'], form.cleaned_data['selectedLocation'])
                send_mail('New Contact Information', message, sender_email, ['shakeela.sadaqat@launchpad7.com'])
                messages.success(request, 'Thank you very much for contacting us, one of our \
                correspondent will get back to you soon.')
                # Email setting for contact form
                return redirect('PackageSpace')
            else:
                messages.error(request, 'Please complete the Captcha Challenge before pressing the send button.')
                return redirect('PackageSpace')
    else:
        form = packageSpaceForm()

    c = context = ({
    'form': form,
    })

    # Render the HTML template PackageSpace.html
    return render(request, 'PackageSpace.html', c)




# View for Gallery Page
def gallery(request):
    # Display all the Dynamic values form models
    gallRWP = galleryRWP.objects.filter().order_by('-id')[:8]
    gallISD = galleryISD.objects.filter().order_by('-id')[:8]

    c = context = ({
    'gallRWP': gallRWP,
    'gallISD': gallISD,
    })


    # Render the HTML template packages.html
    return render(request, 'gallery.html', c)



# Display the detail and generic views
class EventListView(generic.ListView):
    model = Events
    #paginate_by = 2

class EventDetailView(generic.DetailView):
    model = Events

class PromotionListView(generic.ListView):
    model = Promotions
    #paginate_by = 2

class PromotionDetailView(generic.DetailView):
    model = Promotions

class LocationDetailView(generic.DetailView):
    model = Locations

class pricingrawalpindiDetailView(generic.DetailView):
    model = PricingRawalpindi

class pricingislamabadDetailView(generic.DetailView):
    model = PricingIslamabad

class aboutListView(generic.ListView):
    model = about

class GalleryISDListView(generic.ListView):
    model = galleryISD


class GalleryRWPListView(generic.ListView):
    model = galleryRWP


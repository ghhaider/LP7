from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.validators import validate_email

from LP7Website import settings
from lp7.models import ContactedUser, eventBooking, packageSpace, customUser


# Contact Form
class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Name',

    }), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Phone Number',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Message',
    }))

    class Meta:
        model = ContactedUser
        fields = ['name', 'email', 'phone', 'message']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit() and name.isalpha():
            raise forms.ValidationError("Name can't be in digits.")
        length = 4
        if len(name) < length:
            raise forms.ValidationError("Name should be more than 3 characters.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        min_length = 10
        if len(phone) < min_length:
            raise forms.ValidationError("Your Phone number should have at least 10 characters.")
        return phone

    def clean_message(self):
        message = self.cleaned_data['message']
        min_length = 15
        if len(message) < min_length:
            raise forms.ValidationError("Your message should have at least 15 characters.")
        return message


# Event Booking Form
class eventBookingForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput ',
        'placeholder': 'Your Name',
        'required': 'True'
    }), max_length=50)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control formInput ',
        'placeholder': 'Your Email',
        'required': 'True'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Phone Number',
        'required': 'True'
    }))
    organization = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Organization',
        'required': 'True'
    }))
    eventName = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Event Name',
        'required': 'True'
    }))
    eventDate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={
        'class': 'form-control formInput',
        'id': 'datePicker'
    }))
    eventTime = forms.TimeField(input_formats=settings.TIME_INPUT_FORMATS, widget=forms.TimeInput(attrs={
        'class': 'form-control formInput',
        'id': 'timePicker'
    }))
    eventDetail = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Event Detail',
        'required': 'True'
    }))
    eventGuest = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Expected No. of Guests',
        'required': 'True'
    }))
    CHOICES = [('Islamabad', 'Islamabad'),
               ('Rawalpindi', 'Rawalpindi')]
    eventLocation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'form-check form-check-inline ',
    }))

    # def __init__(self, *args, **kwargs):
    #     super(addCoWorkerForm, self).__init__(*args, **kwargs)
    #     self.fields['coworkerPicture'].required = False
    #     self.fields['companyName'].required = False
    #     self.fields['joiningDate'].required = False
    #     self.fields['dob'].required = False

    class Meta:
        model = eventBooking
        fields = ['name', 'email', 'phone', 'organization', 'eventName',
                  'eventTime', 'eventDate', 'eventGuest', 'eventDetail', 'eventLocation']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit() and name.isalpha():
            raise forms.ValidationError("Name can't be in digits.")
        length = 4
        if len(name) < length:
            raise forms.ValidationError("Name should be more than 3 characters.")
        return name

    def clean_eventName(self):
        eventName = self.cleaned_data['eventName']
        if eventName.isdigit() and eventName.isalpha():
            raise forms.ValidationError("Event name can't be in digits.")
        length = 4
        if len(eventName) < length:
            raise forms.ValidationError("Event name should be more than 3 characters.")
        return eventName

    def clean_organization(self):
        organization = self.cleaned_data['organization']
        if organization.isdigit() and organization.isalpha():
            raise forms.ValidationError("Organization name can't be in digits.")
        length = 4
        if len(organization) < length:
            raise forms.ValidationError("Organization name should be more than 3 characters.")
        return organization

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        min_length = 10
        if len(phone) < min_length:
            raise forms.ValidationError("Your phone number should have at least 10 characters.")
        return phone

    def clean_eventDetail(self):
        eventDetail = self.cleaned_data['eventDetail']
        min_length = 15
        if len(eventDetail) < min_length:
            raise forms.ValidationError("Your event detail should be more than 15 characters.")
        return eventDetail

    def clean_eventLocation(self):
        eventLocation = self.cleaned_data['eventLocation']
        if eventLocation is None:
            raise forms.ValidationError("Please select one location.")
        return eventLocation


# Package Space Form
class packageSpaceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput ',
        'placeholder': 'Your Name',
        'required': 'True'

    }), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control formInput ',
        'placeholder': 'Your Email',
        'required': 'True'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control formInput',
        'placeholder': 'Phone Number',
        'required': 'True'
    }))

    CHOICES = [('', ''),
               ('Virtual', 'Virtual'),
               ('Private Office', 'Private Office'),
               ('Dedicated Desk', 'Dedicated Desk'),
               ('Event Access', 'Event Access'),
               ('Private Office', 'Private Office')]
    selectedPackage = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': 'form-control formInput',
        'required': 'True',
    }))

    CHOICES = [('', ''),
               ('Islamabad', 'Islamabad'),
               ('Rawalpindi', 'Rawalpindi')]
    selectedLocation = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': 'form-control formInput',
        'required': 'True'
    }))

    class Meta:
        model = packageSpace
        fields = ['name', 'email', 'phone', 'selectedPackage', 'selectedLocation']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit() and name.isalpha():
            raise forms.ValidationError("Name can't be in digits.")
        length = 4
        if len(name) < length:
            raise forms.ValidationError("Name should be more than 3 characters.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        min_length = 10
        if len(phone) < min_length:
            raise forms.ValidationError("Your phone number should have at least 10 characters.")
        return phone


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = customUser
        fields = '__all__'


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = customUser
        fields = '__all__'

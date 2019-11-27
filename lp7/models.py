from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime
import uuid

from django.db import models
from django.urls import reverse


# Model for TopBar.
class TopBar(models.Model):
    TopBarNum = models.CharField('Top Bar Number', max_length=30, help_text='Enter phone number to display on TopBar.')

    def __str__(self):
        """String for representing the Model object."""
        return self.TopBarNum

    class Meta:
        verbose_name_plural = "Top Bar"


class Logo(models.Model):
    logoImage = models.ImageField(upload_to='../media/images/', help_text='Please upload the website logo here.')
    altTitle = models.CharField(max_length=30, help_text="Enter Alt text for image.", default='Alt text')

    class Meta:
        verbose_name_plural = "Logo Section"


# Model for About
class about(models.Model):
    aboutHeading = models.TextField('Heading Text', max_length=50, help_text='Please enter your heading here.')
    aboutParagraph1 = models.TextField('Paragraph 1', max_length=2000, help_text='Please enter your paragraph.')
    aboutParagraph2 = models.TextField('Paragraph 2', max_length=2000, help_text='Please enter your paragraph.')
    aboutImage = models.ImageField(default='About Image', upload_to='../media/images/about',
                                   help_text='Please upload the image for About section')

    def get_absolute_url(self):
        """Returns the url to access a detail record for about section."""
        return reverse('about-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "About Section"


# Model for Background Images
class BGimages(models.Model):
    perfectBG = models.ImageField('Perfect Match Background', upload_to='../media/images/backgrounds',
                                  help_text='Please upload the background image for Perfect Match Section')
    memberBG = models.ImageField('Member Logos Background', upload_to='../media/images/backgrounds',
                                 help_text='Please upload the background image for Members Logo Section')
    locationPageBG = models.ImageField('Locations Page Background', upload_to='../media/images/backgrounds',
                                       help_text='Please upload the background image for Locations page',
                                       default='Locations Page BG')
    locationDetailBG = models.ImageField('Location Detail Page Background',
                                         upload_to='../media/images/backgrounds',
                                         help_text='Please upload the background image for Location Detail page',
                                         default='Location Detail Page BG')
    contactPageBG = models.ImageField('Contact Page Background', upload_to='../media/images/backgrounds',
                                      help_text='Please upload the background image for Contact page',
                                      default='Contact Page BG')

    eventPageListBG = models.ImageField('Event List Page Background', upload_to='../media/images/backgrounds',
                                        help_text='Please upload the background image for Event List page',
                                        default='Event List Page BG')
    eventDetailPageBG = models.ImageField('Event Detail Page Background', upload_to='../media/images/backgrounds',
                                          help_text='Please upload the background image for Event Detail page',
                                          default='Event Detail Page BG')
    promotionListPageBG = models.ImageField('Promotion List Page Background', upload_to='../media/images/backgrounds',
                                            help_text='Please upload the background image for Promotion List page',
                                            default='Promotion List Page BG')
    promotionDetailPageBG = models.ImageField('Promotion Detail Page Background',
                                              upload_to='../media/images/backgrounds',
                                              help_text='Please upload the background image for Promotion Detail page',
                                              default='Promotion Detail Page BG')
    packageDetailPageBG = models.ImageField('Package Detail Page Background',
                                            upload_to='../media/images/backgrounds',
                                            help_text='Please upload the background image for Package Detail page',
                                            default='Package Detail Page BG')
    homeHeadPageBG = models.ImageField('Home Head Section Background',
                                       upload_to='../media/images/backgrounds',
                                       help_text='Please upload the background image for Home Head Section page',
                                       default='Home Head Section BG')
    aboutPageBG = models.ImageField('About Page Background',
                                    upload_to='../media/images/backgrounds',
                                    help_text='Please upload the background image for Home About page',
                                    default='About Page BG')

    galleryPageBG = models.ImageField('Gallery Page Background',
                                      upload_to='../media/images/backgrounds',
                                      help_text='Please upload the background image for gallery page',
                                      default='gallery Page BG')

    eventFormBG = models.ImageField('Event Form Background',
                                    upload_to='../media/images/backgrounds',
                                    help_text='Please upload the background image for event Form',
                                    default='event form')

    packageFormBG = models.ImageField('package Form Background',
                                      upload_to='../media/images/backgrounds',
                                      help_text='Please upload the background image for package Form',
                                      default='Package form')

    class Meta:
        verbose_name_plural = "Background Images Section"


# Model for LP7 Features
class LP7features(models.Model):
    featureText = models.TextField('Featured Text', max_length=200, help_text='Please enter your featured text.')

    class Meta:
        verbose_name_plural = "Features Section"


# Model for LP7 Locations
class Locations(models.Model):
    LocationImage = models.ImageField('Location Image', upload_to='../media/images/locations',
                                      help_text='Please upload location image.')
    LocationName = models.CharField('Location Name', default='', max_length=50,
                                    help_text='Please enter the location name.')
    LocationAddress = models.TextField('Location Address', max_length=500, blank=True,
                                       help_text='Enter the detailed address.')
    LocationPhone = models.CharField('PTCL Number', max_length=30, blank=True,
                                     help_text='Enter the PTCL number for location.')
    LocationMobile = models.CharField('Mobile Number', max_length=30, blank=True,
                                      help_text='Enter Mobile/Whatsapp number for location.')
    LocationEmailID = models.CharField('Email Address', max_length=50, blank=True,
                                       help_text='Enter the Email address for location.')
    LocationWeb = models.CharField('Web Address ', max_length=50, blank=True,
                                   help_text='Enter the web address for location.')
    slug = models.SlugField(unique=True, default='')

    def get_absolute_url(self):
        """Returns the url to access a detail record for particular location."""
        return reverse('locations-detail', kwargs={'slug': self.slug})

    def __str__(self):
        """String for representing the Model object."""
        return self.LocationName

    class Meta:
        verbose_name_plural = "Locations Section"


# Model for LP7 Events
class Events(models.Model):
    eventTitle = models.CharField('Event Title', max_length=500, blank=True, help_text='Please enter your event title '
                                                                                       'here.', )
    eventImage = models.ImageField('Event Image', upload_to='../media/images/events/', help_text='Please upload the '
                                                                                                 'event image')
    eventText = models.TextField('Event Detail', max_length=2000, blank=True, help_text='Please enter the detail of '
                                                                                        'event.')
    eventLocation = models.CharField('Event Location', blank=True, max_length=100, help_text='Please enter the '
                                                                                             'location of event.')
    eventDate = models.DateField('Event Date', blank=True, help_text='Please select the date of your event.', null=True)
    eventTime = models.TimeField('Event Time', blank=True, help_text='Please select the starting time of your event.',
                                 null=True)
    slug = models.SlugField(unique=True, default='')
    Status_Choices = (
        ('', ''),
        ('Active', 'Active'),
        ('Expire', 'Expire'),
    )
    status = models.CharField('Event Status', max_length=10, choices=Status_Choices, help_text='Select the status '
                                                                                               'of event.',
                              default='')

    def get_absolute_url(self):
        """Returns the url to access a detail record for particular event."""
        return reverse('events-detail', kwargs={'slug': self.slug})

    def __str__(self):
        """String for representing the Model object."""
        return self.eventTitle

    class Meta:
        verbose_name_plural = "Events Section"


# Model for Event Page Header
class EventsHeader(models.Model):
    eventDetailText = models.TextField('Event Detail Page Text', blank=True,
                                       help_text='Please enter some paragraph for event detail page.',
                                       )
    eventDetailImage = models.ImageField(upload_to='../media/images/events',
                                         help_text='Please upload the image file for event detail page.',
                                         default='Event detail image', blank=True)

    class Meta:
        verbose_name_plural = "Events Page Heading"


# Model for LP7 Members
class LP7MembersLogo(models.Model):
    logoImage = models.ImageField('Member Logo', upload_to='../media/images/members/',
                                  help_text='Please upload the new member logo.', )

    class Meta:
        verbose_name_plural = "Members Section"


# Model for Testimonials
class LP7Testimonials(models.Model):
    testiImage = models.ImageField('Testimonial Image', upload_to='../media/images/testimonials',
                                   help_text='Please upload the image of testimonial.')
    testiText = models.TextField('Testimonial Review', max_length=1500, help_text='Please enter the text of text of '
                                                                                  'review.')
    testiName = models.CharField('Testimonial Name', max_length=100, help_text='Please enter the name of testimonial.')
    testiTitle = models.CharField('Testimonial Title', max_length=50, help_text='Please enter the title of '
                                                                                'testimonial.')
    testiCompany = models.CharField('Testimonial Company', max_length=50, help_text='Please enter the name of '
                                                                                    'testimonial company.', blank=True)

    class Meta:
        verbose_name_plural = "Testimonial Section"


# Model for LP7 Promotions
class Promotions(models.Model):
    promotionTitle = models.CharField('Promotion Title', max_length=500, blank=True,
                                      help_text='Please enter your promotion title '
                                                'here.')
    promotionImage = models.ImageField('Promotion Image', upload_to='../media/images/promotions/',
                                       help_text='Please upload the '
                                                 'promotion image')
    promotionText = models.TextField('Promotion Detail', default='Promotion detail', max_length=500,
                                     help_text='Please enter the detail of '
                                               'promotion.')
    promotionLocation = models.CharField('Promotion Location', blank=True, max_length=100, help_text='Please enter the '
                                                                                                     'location of '
                                                                                                     'promotion.')
    promotionStartDate = models.DateField('promotion Starting Date', blank=True, help_text='Please select the starting '
                                                                                           'date of promotion.')
    promotionEndDate = models.DateField('promotion Ending Date', blank=True,
                                        help_text='Please select the starting date of promotion.')
    Status_Choices = (
        ('', ''),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField('Promotion Status', max_length=10, choices=Status_Choices, help_text='Select the status '
                                                                                                   'of promotion.',
                              default='')
    slug = models.SlugField(unique=True, default='')

    def get_absolute_url(self):
        """Returns the url to access a detail record for particular event."""
        return reverse('promotions-detail', kwargs={'slug': self.slug})

    def __str__(self):
        """String for representing the Model object."""
        return self.promotionTitle

    class Meta:
        verbose_name_plural = "Promotions Section"


# Model for Package Features
class PackagePriceFeatures(models.Model):
    featureName = models.CharField('Package Feature', max_length=200, help_text='Please enter the features of package')

    def __str__(self):
        """String for representing the Model object."""
        return self.featureName

    class Meta:
        verbose_name_plural = "Package Features Section"


# Model for Pricing Rawalpindi
class PricingRawalpindi(models.Model):
    PackageNameRWP = models.CharField('Package Name', max_length=50, help_text='Please enter the package name.')
    PackageImageRWP = models.ImageField('Package Image', upload_to='../media/images/pricing/',
                                        help_text='Please upload the image for package.')
    PackageFeature = models.ManyToManyField('PackagePriceFeatures',
                                            help_text='Please select the features for your particular package.')
    PackagePrice = models.IntegerField('Price', help_text='Please enter the price for this particular package.')
    discountedPriceRWP = models.IntegerField('Discounted Price', help_text='Please enter the discounted price for '
                                                                           'this particular package.',
                                             blank=True, null=True)
    discountedPercentRWP = models.CharField('Discounted Percent', help_text='Please enter the Discounted '
                                                                            'Percentage of this particular '
                                                                            'package.(e.g: 20%)', max_length=10,
                                            blank=True, null=True)
    discountedDateRWP = models.DateField('Discount Validity', help_text='Please select the validity of discount for '
                                                                        'this particular package.',
                                         blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.PackageNameRWP

    def get_absolute_url(self):
        """Returns the url to access a detail record for particular price list."""
        return reverse('packagerwp-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Pricing Rawalpindi Section"


# Model for Pricing Islamabad2
class PricingIslamabad(models.Model):
    PackageNameISD = models.CharField('Package Name', max_length=50, help_text='Please enter the package name.')
    PackageImageISD = models.ImageField('Package Image', upload_to='../media/images/pricing/',
                                        help_text='Please upload the image for package.')
    PackageFeature = models.ManyToManyField('PackagePriceFeatures',
                                            help_text='Please select the features for your particular package.')
    PackagePrice = models.IntegerField('Price', help_text='Please enter the price for this particular package.')
    discountedPriceISD = models.IntegerField('Discounted Price', help_text='Please enter the discounted price for '
                                                                           'this particular package.',
                                             blank=True, null=True)
    discountedPercentISD = models.CharField('Discounted Percent', help_text='Please enter the Discounted '
                                                                            'Percentage of this particular '
                                                                            'package.(e.g: 20%)', max_length=10,
                                            blank=True, null=True)
    discountedDateISD = models.DateField('Discount Validity', help_text='Please select the validity of discount for '
                                                                        'this particular package.',
                                         blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.PackageNameISD

    def get_absolute_url(self):
        """Returns the url to access a detail record for particular price list."""
        return reverse('packageisd-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Pricing Islamabad Section"


# Model for Contact Us
class ContactedUser(models.Model):
    name = models.CharField('Name', max_length=50, help_text="Sender's Name.")
    email = models.EmailField('Email', help_text="Sender's Email")
    phone = models.CharField('Phone Number', help_text="Sender's Phone Number", default='', max_length=100)
    message = models.TextField('Message', help_text="Sender's Message")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us Form"


# Model for Gallery Rawalpindi
class galleryRWP(models.Model):
    galleryRWPimage = models.ImageField('Gallery Image', upload_to='../media/images/gallery/RWP/',
                                        help_text='Please upload the image for Gallery Rawalpindi.')
    galleryRWPimageName = models.CharField('Image Name', max_length=30, help_text="please enter the name of image.")
    galleryRWPevent = models.CharField('Image Event', max_length=80,
                                       help_text='Please enter the name of event where the image captured.')

    def __str__(self):
        return self.galleryRWPimageName

    class Meta:
        verbose_name_plural = "Gallery Rawalpindi"


# Model for Gallery Islamabad
class galleryISD(models.Model):
    galleryISDimage = models.ImageField('Gallery Image', upload_to='../media/images/gallery/ISD/',
                                        help_text='Please upload the image for Gallery Islamabad.')
    galleryISDimageName = models.CharField('Image Name', max_length=30, help_text="please enter the name of image.")
    galleryISDevent = models.CharField('Image Event', max_length=80,
                                       help_text='Please enter the name of event where the image captured.')

    def __str__(self):
        return self.galleryISDimageName

    class Meta:
        verbose_name_plural = "Gallery Islamabad"


# Model for Contact Us
class eventBooking(models.Model):
    name = models.CharField('Name', max_length=50, help_text="Sender's Name.")
    email = models.EmailField('Email', help_text="Sender's Email")
    phone = models.CharField('Phone Number', max_length=100, help_text="Sender's Phone Number", default='')
    organization = models.CharField('Organization', max_length=50, help_text="Sender's Organization Name.")
    eventName = models.CharField('Event Name', max_length=150, help_text='Name of event.')
    eventDate = models.DateField('Event Date', help_text='Event Date.', null=True, blank=True, )
    eventTime = models.TimeField('Event Time', help_text='Event Time.', default=datetime.time())
    eventDetail = models.TextField('Event Detail',
                                   help_text='Event Detail.',
                                   )
    eventGuest = models.IntegerField('Expected No. of guest in event')
    eventLocation = models.CharField('Event Location', max_length=50, default='Location')

    def __str__(self):
        return self.eventName

    class Meta:
        verbose_name_plural = "Event Booking Form"


# Model for book package space
class packageSpace(models.Model):
    name = models.CharField("Sender's Name", max_length=50, help_text="Sender's Name.")
    email = models.EmailField("Sender's Email", help_text="Sender's Email.")
    phone = models.CharField("Sender's Phone Number", help_text="Sender's Phone Number.", default='', max_length=100)
    selectedPackage = models.CharField("Selected Package", help_text="Preferred Package.", max_length=80)
    selectedLocation = models.CharField('Selected Location', help_text='Preferred location.', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Package Space Form'


# Custom User Model
class customUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'Users'

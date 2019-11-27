from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from lp7.forms import MyUserChangeForm, MyUserCreationForm
from lp7.models import top_bar, Logo, about, \
    Locations, BGimages, LP7features, Events, LP7MembersLogo, LP7Testimonials, Promotions, \
    PricingRawalpindi, PricingIslamabad, PackagePriceFeatures, ContactedUser, \
    galleryISD, galleryRWP, eventBooking, packageSpace, EventsHeader
from lp7.models import customUser


# Register the Admin classes for Footer Addresses
@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('LP7 Location', {
            'fields': ('LocationName', 'LocationAddress', ('LocationPhone', 'LocationMobile'),
                       'LocationEmailID', 'LocationWeb', 'LocationImage', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('LocationName',)}


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_filter = ('eventTitle', 'eventDate', 'eventLocation')
    list_display = ('eventTitle', 'eventDate', 'eventTime', 'eventLocation', 'status')
    fieldsets = (
        ('LP7 Events', {
            'fields': ('eventTitle', 'eventImage', 'eventText', 'eventLocation',
                       ('eventDate', 'eventTime'), 'status', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('eventTitle',)}


@admin.register(LP7Testimonials)
class LP7TestimonialsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('LP7 Testimonials', {
            'fields': ('testiName', ('testiTitle', 'testiCompany'), 'testiImage', 'testiText',)
        }),
    )


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_filter = ('promotionLocation', 'promotionStartDate', 'promotionEndDate',)
    list_display = ('promotionTitle', 'promotionStartDate', 'promotionEndDate', 'promotionLocation', 'status')
    fieldsets = (
        ('LP7 Promotions', {
            'fields': ('promotionTitle', 'promotionLocation', 'promotionText', 'promotionImage',
                       ('promotionStartDate', 'promotionEndDate'), 'status', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('promotionTitle',)}


@admin.register(PricingRawalpindi)
class PricingRawalpindiAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Rawalpindi Packages', {
            'fields': (('PackageNameRWP', 'PackageImageRWP'), 'PackagePrice',
                       'PackageFeature', ('discountedPriceRWP', 'discountedPercentRWP'), 'discountedDateRWP')
        }),
    )


@admin.register(PricingIslamabad)
class PricingIslamabadAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Islamabad Packages', {
            'fields': (('PackageNameISD', 'PackageImageISD'), 'PackagePrice',
                       'PackageFeature', ('discountedPriceISD', 'discountedPercentISD'), 'discountedDateISD')
        }),
    )


@admin.register(BGimages)
class BGimagesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('LP7 Background Images', {
            'fields': ('perfectBG', 'memberBG', 'locationPageBG', 'contactPageBG',
                       'eventPageListBG', 'eventDetailPageBG', 'promotionListPageBG',
                       'promotionDetailPageBG', 'packageDetailPageBG', 'homeHeadPageBG',
                       'aboutPageBG', 'locationDetailBG', 'galleryPageBG', 'eventFormBG',
                       'packageFormBG')
        }),
    )


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('LP7 Logo', {
            'fields': ('logoImage', 'altTitle')
        }),
    )


@admin.register(ContactedUser)
class ContactedUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    readonly_fields = ['name', 'email', 'phone', 'message', ]
    fieldsets = (
        ("Sender's Data", {
            'fields': ('name', 'email', 'phone', 'message')
        }),
    )

    def has_add_permission(self, request):
        return False


@admin.register(galleryISD)
class galleryISDAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Gallery Islamabad", {
            'fields': ('galleryISDimage', 'galleryISDimageName', 'galleryISDevent')
        }),
    )


@admin.register(galleryRWP)
class galleryRWPAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Gallery Rawalpindi", {
            'fields': ('galleryRWPimage', 'galleryRWPimageName', 'galleryRWPevent')
        }),
    )


@admin.register(eventBooking)
class eventBookingAdmin(admin.ModelAdmin):
    # readonly_fields = ['name', 'email', 'phone', 'organization', 'eventName', 'eventDetail', 'eventGuest',
    #                    'eventDate', 'eventTime', 'eventLocation']
    fieldsets = (
        ("Sender's Information", {
            'fields': (('name', 'email'), 'phone', 'organization')
        }),
        ("Event Information", {
            'fields': ('eventName', 'eventDetail', 'eventGuest', 'eventLocation', ('eventDate', 'eventTime'))
        }),
    )

    # def has_add_permission(self, request):
    #     return False


@admin.register(packageSpace)
class packageSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'selectedPackage', 'selectedLocation')
    readonly_fields = ['name', 'email', 'phone', 'selectedPackage', 'selectedLocation']
    fieldsets = (
        ("Sender's Information", {
            'fields': (('name', 'email'), 'selectedPackage', 'selectedLocation')
        }),

    )

    def has_add_permission(self, request):
        return False


# Register Custom User model
class customUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = customUser
    # list_display = ['username', 'mobile_number', 'birth_date']
    #fieldsets = UserAdmin.fieldsets + (
        # (None, {'fields': ('profession', 'birth_date')}),
    #)  # this will allow to change these fields in admin module


admin.site.register(customUser, customUserAdmin)

# Register your models here.
admin.site.register(top_bar)
# admin.site.register(Logo)
admin.site.register(about)
admin.site.register(EventsHeader)
# admin.site.register(BGimages)
admin.site.register(LP7features)
# admin.site.register(Locations)
admin.site.register(LP7MembersLogo)
admin.site.register(PackagePriceFeatures)
# admin.site.register(Contact)
admin.site.site_header = 'LaunchPad7 Administration'
admin.site.index_title = 'Welcome to LaunchPad7 Administration'
admin.site.site_title = 'LaunchPad7'
admin.site.unregister(Group)
# admin.site.register(LP7events)
# admin.site.register(AddressIslamabad)
# admin.site.register(AddressRawalpindi)

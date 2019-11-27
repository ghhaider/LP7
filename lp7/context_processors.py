from lp7.models import TopBar, Logo, Locations, BGimages, PricingIslamabad, PricingRawalpindi, EventsHeader


def common_content(request):
    # Display all the Dynamic values form models
    num = TopBar.objects.last()
    alt = Logo.objects.all()
    location = Locations.objects.all()
    PMBG = BGimages.objects.all()
    Prwp = PricingRawalpindi.objects.all()
    Pisd = PricingIslamabad.objects.all()
    eventHeading = EventsHeader.objects.last()

    context = {
        'topBarNumber': num,
        'loc': location,
        'altText': alt,
        'BG': PMBG,
        'Prwp': Prwp,
        'Pisd': Pisd,
        'eventHeading': eventHeading
    }

    return {'sameContent': context}

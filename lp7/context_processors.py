from lp7.models import TopBar, Logo, Locations, BGimages, PricingIslamabad, PricingRawalpindi, EventsHeader, Events, \
    Promotions


def common_content(request):
    # Display all the Dynamic values form models
    num = TopBar.objects.last()
    alt = Logo.objects.all()
    location = Locations.objects.all()
    PMBG = BGimages.objects.all()
    Prwp = PricingRawalpindi.objects.all()
    Pisd = PricingIslamabad.objects.all()
    eventHeading = EventsHeader.objects.last()
    promotion = Promotions.objects.filter(status='Active').last()
    events = Events.objects.filter(status='Active').last()

    context = {
        'num': num,
        'loc': location,
        'altText': alt,
        'BG': PMBG,
        'Prwp': Prwp,
        'Pisd': Pisd,
        'eventHeading': eventHeading,
        'events': events,
        'promotion': promotion
    }

    return {'sameContent': context}

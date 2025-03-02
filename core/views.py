from django.shortcuts import render
from django.http import HttpResponseServerError, Http404
from . import models


def home(request):
    services = models.Service.objects.all()
    contacts = models.ContactInformation.objects.all()
    feedbacks = models.Feedback.objects.all()
    stats = models.Statistics.objects.all()
    main_services = models.MainService.objects.all()
  

    return render(request, 'index.html', {
        'services': services,
        'contacts': contacts,
        'feedbacks': feedbacks,
        'stats': stats,
        'main_services': main_services
    })


def about(request):
    services = models.Service.objects.all()
    contacts = models.ContactInformation.objects.all()
    feedbacks = models.Feedback.objects.all()
    stats = models.Statistics.objects.all()
    main_services = models.MainService.objects.all()
    return render(request, 'about.html', {'services': services, 'contacts': contacts,
                                          'feedbacks': feedbacks,
                                          'stats': stats,
                                          'main_services': main_services})

def services(request):
    services = models.Service.objects.all()
    contacts = models.ContactInformation.objects.all()
    feedbacks = models.Feedback.objects.all()
    stats = models.Statistics.objects.all()
    main_services = models.MainService.objects.all()

    return render(
        request,
        'services.html',
        {
            'services': services,
            'contacts': contacts,
            'feedbacks': feedbacks,
            'stats': stats,
            'main_services': main_services,
        }
    )

    
def contact(request):
    services = models.Service.objects.all()
    contacts = models.ContactInformation.objects.all()
    feedbacks = models.Feedback.objects.all()
    stats = models.Statistics.objects.all()
    main_services = models.MainService.objects.all()

    return render(
        request,
        'contact.html',
        {
            'services': services,
            'contacts': contacts,
            'feedbacks': feedbacks,
            'stats': stats,
            'main_services': main_services,
        }
    )


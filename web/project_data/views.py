from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Kickstarter


def kickstarter_list_view(request):
    kickstarters = get_list_or_404(Kickstarter)
    context = {
        'kickstarters': kickstarters
    }

    return render(request, 'kickstarters/kickstarter_list.html', context)


def kickstarter_detail_view(request, pk=None):
    kickstarter = get_object_or_404(Kickstarter)
    context = {
        'kickstarter': kickstarter
    }

    return render(request, 'kickstarters/kickstarter_detail.html', context)



from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Kickstarter


def campaigns_list_view(request):
    campaigns = get_list_or_404(Kickstarter)
    context = {
        'campaigns': campaigns
    }

    return render(request, 'campaigns/campaigns_list.html', context)


def campaign_detail_view(request, pk=None):
    campaign = get_object_or_404(Kickstarter)
    context = {
        'campaign': campaign
    }

    return render(request, 'campaigns/campaign_detail.html', context)

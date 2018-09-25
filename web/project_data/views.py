from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import Kickstarter



def kickstarter_list_view(request):
    kickstarters = get_list_or_404(Kickstarter)
    paginator = Paginator(kickstarters, 20)
    page = request.GET.get('page')
    kickstarters = paginator.get_page(page)

    context = {
        'campaigns': campaigns
    }

    return render(request, 'campaigns/campaigns_list.html', context)



def kickstarter_detail_view(request, pk=None):
    kickstarter = get_object_or_404(Kickstarter, id=pk)
    context = {
        'campaign': campaign
    }

    return render(request, 'campaigns/campaign_detail.html', context)

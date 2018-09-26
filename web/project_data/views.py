from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Kickstarter

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def kickstarter_list_view(request):
    kickstarters = get_list_or_404(Kickstarter.objects.order_by('-usd_pledged'))
    paginator = Paginator(kickstarters, 20)
    page = request.GET.get('page')
    kickstarters = paginator.get_page(page)
    context = {
        'kickstarters': kickstarters
    }

    return render(request, 'kickstarters/kickstarter_list.html', context)


def kickstarter_detail_view(request, pk=None):
    kickstarter = get_object_or_404(Kickstarter, id=pk)
    context = {
        'kickstarter': kickstarter
    }

    return render(request, 'kickstarters/kickstarter_detail.html', context)

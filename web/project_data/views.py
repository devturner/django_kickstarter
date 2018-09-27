from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Kickstarter

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def kickstarter_list_view(request):
    """List view for kickstarters that implements custom pagination for efficiency.
    """
    num_per_page = 20

    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    else:
        page = 1

    length = Kickstarter.objects.count()
    num_pages = length // num_per_page

    if page > num_pages:
        page = num_pages
    next_page = page + 1
    prev_page = page - 1

    kwargs = {
        'id__gte': (page*num_per_page)-num_per_page+1,
        'id__lte': page*num_per_page
        }

    kickstarters = get_list_or_404(Kickstarter.objects.order_by('-usd_pledged'), **kwargs)

    # paginator = Paginator(kickstarters, num_per_page)
    # print('paginator is', paginator)

    # kickstarters = paginator.get_page(page)

    context = {
        'kickstarters': kickstarters,
        'num_pages': str(num_pages),
        'curr_page': str(page),
        'next_page': str(next_page),
        'prev_page': str(prev_page)
    }

    return render(request, 'kickstarters/kickstarter_list.html', context)


def kickstarter_detail_view(request, pk=None):
    """Kickstarter detail view
    """
    kickstarter = get_object_or_404(Kickstarter, id=pk)
    context = {
        'kickstarter': kickstarter
    }

    return render(request, 'kickstarters/kickstarter_detail.html', context)

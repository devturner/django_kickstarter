from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def calculate_percentage(kickstarter):
    """Custom filter to calculate percent of goal met
    """
    if kickstarter.usd_goal_real > 0:
        percent = int((kickstarter.usd_pledged / kickstarter.usd_goal_real) * 100)
    else:
        percent = 0

    return '{:,}%'.format(percent)


@register.filter
def pledged_per_backer(kickstarter):
    """Custom filter to calculate amount pledged per backer
    """
    if kickstarter.backers > 0:
        ppb = int(kickstarter.usd_pledged / kickstarter.backers)
    else:
        ppb = 0

    return '${:,}'.format(ppb)

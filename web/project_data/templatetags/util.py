from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def calculate_percentage(kickstarter):
    percent = int((kickstarter.usd_pledged / kickstarter.usd_goal_real) * 100)

    return '{:,}%'.format(percent)


@register.filter
def pledged_per_backer(kickstarter):
    ppb = int(kickstarter.usd_pledged / kickstarter.backers)

    return '${:,}'.format(ppb)

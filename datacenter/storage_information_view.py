from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit


def storage_information_view(request):

    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = list()

    for active_visit in active_visits:
        non_closed_visits.append(
            {
                "who_entered": active_visit.passcard,
                "entered_at": localtime(active_visit.entered_at),
                "duration": active_visit.format_duration(active_visit.get_duration()),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

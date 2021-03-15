from django.shortcuts import render
from django.utils import timezone
from datacenter.models import Visit


def get_duration(entered_at, left_at=None):
    """
    Getting duration of the visit.
    :param entered_at: time when the one entered warehouse
    :param left_at: time when the one left warehouse
    :return: duration in seconds
    """

    return (timezone.now() - entered_at).total_seconds() if not left_at else (left_at - entered_at).total_seconds()


def format_duration(seconds):
    """
    Formatting duration for print, given a total number of seconds.
    :param seconds: number of seconds
    :return: timedelta in formatted form
    """

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def storage_information_view(request):

    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = list()

    for active_visit in active_visits:
        localized_time_entered = timezone.localtime(active_visit.entered_at)
        non_closed_visits.append(
            {
                "who_entered": active_visit.passcard,
                "entered_at": localized_time_entered,
                "duration": format_duration(get_duration(localized_time_entered)),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

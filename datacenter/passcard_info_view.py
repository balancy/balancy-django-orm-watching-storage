from django.shortcuts import render
from django.utils import timezone

from datacenter.models import Passcard, Visit
from datacenter.storage_information_view import get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    this_passcard_all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_all_visits_formatted = list()

    for visit_by_passcard in this_passcard_all_visits:
        localized_time_entered_at = timezone.localtime(visit_by_passcard.entered_at)
        duration = get_duration(localized_time_entered_at) if not visit_by_passcard.leaved_at else \
            get_duration(localized_time_entered_at, timezone.localtime(visit_by_passcard.leaved_at))

        this_passcard_all_visits_formatted.append(
            {
                "entered_at": localized_time_entered_at,
                "duration": format_duration(duration),
                "is_strange": (duration // 3600) > 0,
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_all_visits_formatted,
    }
    return render(request, 'passcard_info.html', context)

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits_formatted = list()
    for this_passcard_visit in this_passcard_visits:
        duration = this_passcard_visit.get_duration()

        this_passcard_visits_formatted.append(
            {
                "entered_at": localtime(this_passcard_visit.entered_at),
                "duration": this_passcard_visit.format_duration(duration),
                "is_strange": this_passcard_visit.is_strange(duration),
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits_formatted,
    }
    return render(request, 'passcard_info.html', context)

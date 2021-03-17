from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        """Getting duration of the visit.

        :return: duration in seconds
        """

        return (now() - localtime(self.entered_at)).total_seconds() if not self.leaved_at \
            else (self.leaved_at - self.entered_at).total_seconds()

    @staticmethod
    def format_duration(total_seconds):
        """
        Formatting duration for print, given a total number of seconds.
        :param total_seconds: number of seconds
        :return: timedelta in formatted form
        """

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    @staticmethod
    def is_strange(total_seconds):
        """Checks if the visit was more than one hour.

        :param total_seconds: number of seconds
        :return: is visit strange or not
        """

        return (total_seconds // 3600) > 0

    def __str__(self):
        return "{user} entered at {entered} {left}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            left="left at " + str(self.leaved_at) if self.leaved_at else "not left"
        )

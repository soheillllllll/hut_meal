from django.contrib import admin

from hut_meal_reservation.models import Table, Reservation, Time

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'table', 'time', 'active',]

    class Meta:
        Model = Reservation


admin.site.register(Table)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Time)

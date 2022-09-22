from django.contrib import admin
from  .models import BookTicket, Location, Route, Assignment, Bus
# Register your models here.
admin.site.register(BookTicket)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(Assignment)
admin.site.register(Bus)
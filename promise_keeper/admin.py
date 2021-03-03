from django.contrib import admin
from .models import Contact, Politician, Party, State, Promise

# Register your models here.
admin.site.register(Contact)
admin.site.register(Politician)
admin.site.register(Party)
admin.site.register(State)
admin.site.register(Promise)

#Header Admin Site
admin.site.site_header = "Promise Keeper"
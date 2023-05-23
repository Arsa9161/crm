from django.contrib import admin
from .models import User
from .models import Lead
from .models import Contact
from .models import Activity

# Register your models here.


class UserAdmin(admin.ModelAdmin):
  list_display = ("name", "phone", "company",)


class LeadAdmin(admin.ModelAdmin):
  list_display = ("lead_name", "phone", "address",)


class ActivityAdmin(admin.ModelAdmin):
  list_display = ("activity_name", "company", "status",)


class ContactAdmin(admin.ModelAdmin):
  list_display = ("contacted_name", "date", "note", "type")


admin.site.register(User, UserAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Activity, ActivityAdmin)

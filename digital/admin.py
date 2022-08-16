from django.contrib import admin
from .models import Pricing,PaypalClient,emailCampaign,customPrice,emailFile
# Register your models here.

class EmailCampaignAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','email','subscribe','sent_message',)
    list_filter = ()

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



class PricingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return request.user.username == "texplode"

    def has_delete_permission(self, request, obj=None):
        return request.user.username == "texplode"

    def has_change_permission(self, request, obj=None):
        return request.user.username == "texplode"






admin.site.register(emailCampaign,EmailCampaignAdmin)
admin.site.register(Pricing,PricingAdmin)
admin.site.register(PaypalClient,PricingAdmin)
admin.site.register(customPrice,PricingAdmin)
admin.site.register(emailFile)
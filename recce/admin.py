from django.contrib import admin
from recce.models import RecceVehicle, VehiclePhoto, InstallOption, InstallPhoto, InstallFixedView, BatteryConfig, InstallOptionMaxSetup

@admin.register(RecceVehicle)
class RecceVehicleAdmin(admin.ModelAdmin):
    list_display = ("brand","model","variant","year_from","year_to")
    search_fields = ("brand","model","variant")

admin.site.register(VehiclePhoto)
admin.site.register(InstallOption)
admin.site.register(InstallPhoto)
admin.site.register(InstallFixedView)
admin.site.register(BatteryConfig)
admin.site.register(InstallOptionMaxSetup)

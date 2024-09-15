from django.contrib import admin
from .models import Clinician, Department, Hospital, Patient, Procedure


admin.site.register(Clinician)
admin.site.register(Department)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Procedure)

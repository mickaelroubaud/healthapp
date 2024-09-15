from rest_framework import serializers
from .models import Patient, Clinician, Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ["id", "name"]


class ClinicianSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer()
    uuid = serializers.UUIDField()

    class Meta:
        model = Clinician
        fields = ["name", "uuid", "department"]


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    clinicians = ClinicianSerializer(many=True)

    class Meta:
        model = Patient
        fields = ["url", "firstname", "lastname", "email", "clinicians"]

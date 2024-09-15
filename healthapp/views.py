from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.exceptions import ValidationError
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(ReadOnlyModelViewSet):
    """
    Allow to view and search for Patients
    """

    EMAIL_QUERY_PARAM = "email"
    CLINICIAN_QUERY_PARAM = "clinician"
    DEPARTMENT_QUERY_PARAM = "department"

    SEARCH_QUERY_PARAMS = [
        EMAIL_QUERY_PARAM,
        CLINICIAN_QUERY_PARAM,
        DEPARTMENT_QUERY_PARAM,
    ]

    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("id")

    def get_queryset(self):
        email = self.request.query_params.get(self.EMAIL_QUERY_PARAM)
        clinician_uuid = self.request.query_params.get(self.CLINICIAN_QUERY_PARAM)
        department_id = self.request.query_params.get(self.DEPARTMENT_QUERY_PARAM)

        if email is not None:
            self.queryset = self.queryset.filter(email__contains=email)

        if clinician_uuid is not None:
            self.queryset = self.queryset.filter(clinicians__uuid=clinician_uuid)

        if department_id is not None:
            self.queryset = self.queryset.filter(
                clinicians__department__id=department_id
            )

        return self.queryset

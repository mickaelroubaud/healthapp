from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import PatientViewSet


class TestSearch(TestCase):
    """
    Tests the patients endpoint with search query

    """

    fixtures = [
        "healthapp/fixtures/tests.json",
    ]

    def test_search_by_email_with_exact_match(self):
        """
        Tests that Patients are searchable by email and exact match return only one patient
        """
        factory = APIRequestFactory()
        view = PatientViewSet.as_view({"get": "list"})
        request = factory.get(
            "/patients/?email=josephroth@example.org",
            content_type="application/json",
        )

        response = view(request)
        assert response.status_code == 200
        results = response.data["results"]
        assert len(results) == 1
        assert results.pop()["email"] == "josephroth@example.org"

    def test_search_by_email_with_partial_match(self):
        """
        Tests that Patients are searchable by email
        and partial match return patients with the query in their email
        """
        factory = APIRequestFactory()
        view = PatientViewSet.as_view({"get": "list"})
        request = factory.get(
            "/patients/?email=joseph",
            content_type="application/json",
        )

        response = view(request)
        assert response.status_code == 200
        results = response.data["results"]
        for patient in results:
            assert "joseph" in patient["email"]

    def test_search_by_clinician_uuid(self):
        """
        Tests that Patients are searchable by clinician
        """
        factory = APIRequestFactory()
        view = PatientViewSet.as_view({"get": "list"})
        request = factory.get(
            "/patients/?clinician=06b7c912-41ad-4b81-8fc5-ad283e0fc7ce",
            content_type="application/json",
        )

        response = view(request)
        assert response.status_code == 200
        results = response.data["results"]

        for patient in results:
            patient_clinicians = patient["clinicians"]
            for clinician in patient_clinicians:
                assert clinician["uuid"] == "06b7c912-41ad-4b81-8fc5-ad283e0fc7ce"

    def test_search_by_department(self):
        """
        Tests that Patients are searchable by department
        """
        factory = APIRequestFactory()
        view = PatientViewSet.as_view({"get": "list"})
        request = factory.get(
            "/patients/?department=2",
            content_type="application/json",
        )

        response = view(request)
        assert response.status_code == 200
        results = response.data["results"]
        for patient in results:
            patient_clinicians = patient["clinicians"]
            for clinician in patient_clinicians:
                assert clinician["department"]["id"] == 2


from django.db import models


class Hospital(models.Model):
    """
    Represents an hospital
    """

    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    """
    A department inside an hospital

    """

    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class Procedure(models.Model):
    """
    A procedure like a liver transplant

    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Clinician(models.Model):
    """
    Clinicians
    Each clinician is associated with a particular department
    and a procedure

    """

    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    uuid = models.UUIDField(unique=True)
    procedure = models.ForeignKey(
        Procedure, on_delete=models.PROTECT, blank=True, null=True
    )

    class Meta:
        indexes = [models.Index(fields=["uuid"])]

    def __str__(self):
        to_string = f"{self.name} - {self.uuid}"
        if self.procedure is not None:
            to_string += f" ({self.procedure.name})"
        return to_string


class Patient(models.Model):
    """
    A patient of an hospital
    Each patient is associated with on or more clinicians
    """

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.TextField()
    clinicians = models.ManyToManyField(Clinician)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

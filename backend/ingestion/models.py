from django.db import models


class UploadRecord(models.Model):

    source=models.CharField(
        max_length=50
    )

    category=models.CharField(
        max_length=50
    )

    value=models.FloatField()

    unit=models.CharField(
        max_length=50
    )

    approved=models.BooleanField(
        default=False
    )


    def __str__(self):

        return self.category
from django.contrib import admin

from .models import UploadRecord


@admin.register(UploadRecord)

class UploadAdmin(
admin.ModelAdmin
):

    list_display=[

        'source',

        'category',

        'value',

        'unit',

        'approved'

    ]
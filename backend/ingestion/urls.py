from django.urls import path

from .views import (
GetData,
Approve
)


urlpatterns=[

path(
'records/',
GetData.as_view()
),

path(
'approve/<int:id>/',
Approve.as_view()
)

]
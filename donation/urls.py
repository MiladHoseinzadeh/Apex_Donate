from django.urls import path

from donation.views import index

app_name = "donation"

urlpatterns = [
	path("", index, name="index"),
]

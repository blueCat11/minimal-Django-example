from django.contrib import admin
from django.urls import path, include, re_path

from testapp.views import * #Index, StartSurvey, Interests, Questionnaire, Demographics, InterestValues
from minimal_Django import settings
from . import views
from django.conf import settings  # New Import
from django.conf.urls.static import static  # New Import

urlpatterns = [
    re_path(r'^$', Index.as_view(), name="index"),

]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from .views import ChangeOilView, InflateTiresView, DiagnosticView


urlpatterns = [
    path('change_oil/', ChangeOilView.as_view(), name='change_oil'),
    path('inflate_tires/', InflateTiresView.as_view(), name='tires'),
    path('diagnostic/', DiagnosticView.as_view(), name='diagnostic'),
]

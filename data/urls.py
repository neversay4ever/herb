from .views import (
    SampleListView,
    SpeicesListView,
    SampleDetailView,
    SpeciesDetailView,
    AnalysisListView,
    StatListView,
    AnalysisDetailView,
    statview,
)
from django.urls import path

app_name = "data"


urlpatterns = [
    path("species/<int:id>/", SpeciesDetailView.as_view(template_name='data/species_detail.html'), name="species_detail"),
    path("sample/<int:id>/", SampleDetailView.as_view(template_name='data/sample_detail.html'), name="sample_detail"),
    path("analysis/<int:id>/", AnalysisDetailView.as_view(template_name='data/assembly_detail.html'), name="analysis_detail"),
    path("species/", SpeicesListView.as_view(), name="species"),
    path("samples/", SampleListView.as_view(), name="samples"),
    path("analysis/", AnalysisListView.as_view(), name='analysis'),
    path("stat/", statview, name='stat'),
]

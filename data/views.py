import json

from django.http.response import HttpResponse
import pandas as pd
from django.shortcuts import render, get_object_or_404
from .models import Assembly, Cpc, Species, Sample
# Create your views here.
from django.views import generic
from django.views.generic.detail import DetailView
from django.db.models import Count


class SpeicesListView(generic.ListView):
    model = Species


class SampleListView(generic.ListView):
    model = Sample


class AnalysisListView(generic.ListView):
    model = Assembly
    paginate_by = 15
    paginate_orphans = 3


def statview(request):
    context = {}
    context['sample_data'] = Sample.objects.all()
    count_gis = list(Sample.objects.values(
        'lattitude', 'longitude').annotate(count=Count('id')))
    df_count_gis = pd.DataFrame(count_gis).fillna('unkown')
    cols = ['count']

    context['sample_geo_json'] = df_count_gis
    return render(request, 'data/cpc_list.html', context)


class StatListView(generic.ListView):
    model = Cpc
    paginate_by = 15
    template_name = 'sample_home__.html'
    context_object_name = 'samples'
    paginate_by = 100
    queryset = Sample.objects.all()

    def get_queryset(self):
        qs = Sample.objects.all()

        q = self.request.GET.get('q', '')
        if q:
            qs = Sample.objects.filter(
                Q(sample_id__icontains=q) | Q(sample_box_id__icontains=q) | Q(
                    headchest_id__icontains=q) | Q(headchest_usage__icontains=q) | Q(abdomen_id__icontains=q) | Q(abdomen_usage__icontains=q) | Q(gut_id__icontains=q) | Q(gut_usage__icontains=q) | Q(leg_id__icontains=q) | Q(sample_phylum__icontains=q) | Q(sample_class__icontains=q) | Q(sample_order__icontains=q) | Q(sample_genus__icontains=q) | Q(sample_species__icontains=q) | Q(sample_subspecies__icontains=q) | Q(sample_breed__icontains=q) | Q(identifier_name__icontains=q) | Q(identifier_email__icontains=q) | Q(exact_site__icontains=q) | Q(country__icontains=q) | Q(state_province__icontains=q) | Q(city__icontains=q) | Q(county__icontains=q) | Q(latitude__icontains=q) | Q(longitude__icontains=q) | Q(elevation__icontains=q) | Q(collector_name__icontains=q) | Q(bee_type__icontains=q)
            )
        self.sample_filter = SampleFilter(
            self.request.GET, queryset=qs)
        return self.sample_filter.qs.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.

        count_gis = list(self.sample_filter.qs.exclude(latitude__isnull=True).values(
            'latitude', 'longitude', 'sample_species').annotate(count=Count('id')))
        df_count_gis = pd.DataFrame(count_gis).fillna('unkown')
        cols = ['count', 'sample_species']

        geo_json = df_to_geojson(df_count_gis, cols)
        context['sample_geo_json'] = geo_json

        sample_query = self.sample_filter.qs

        context['sample_count'] = sample_query.count()
        context['sample_strain_count'] = sample_query.filter(
            gut_usage='已分菌').count()
        context['sample_meta_count'] = sample_query.filter(
            gut_usage='meta').count()
        context['sample_no_latitude_count'] = sample_query.filter(
            latitude=None).count()

        context['sample_filter'] = self.sample_filter

        return context


class SpeciesDetailView(DetailView):
    model = Species

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Species, id=id_)


class SampleDetailView(DetailView):
    model = Sample

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Sample, id=id_)


class AnalysisDetailView(DetailView):
    model = Assembly

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Assembly, id=id_)


# Create your views here.

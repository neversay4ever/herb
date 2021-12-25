from django.contrib import admin
from data.models import Species, Sample, Assembly, Cpc, Cog, Kegg, Kog, Nr, Pfam, Swissprot, Go, Ssr
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class SpeciesAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Species._meta.get_fields() if field.name != 'gongneng']


class SampleAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Sample._meta.get_fields()]


class AssemblyAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Assembly._meta.get_fields()]


class CpcAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Cpc._meta.get_fields()]


class CogAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Cog._meta.get_fields()]


class KeggAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Kegg._meta.get_fields()]


class KogAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Kog._meta.get_fields()]


class NrAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Nr._meta.get_fields()]


class PfamAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Pfam._meta.get_fields()]


class SwissprotAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Swissprot._meta.get_fields()]


class GoAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Go._meta.get_fields()]


class SsrAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Ssr._meta.get_fields()]


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Assembly, AssemblyAdmin)
admin.site.register(Cpc, CpcAdmin)
admin.site.register(Cog, CogAdmin)
admin.site.register(Kegg, KeggAdmin)
admin.site.register(Kog, KogAdmin)
admin.site.register(Nr, NrAdmin)
admin.site.register(Pfam, PfamAdmin)
admin.site.register(Swissprot, SwissprotAdmin)
admin.site.register(Go, GoAdmin)
admin.site.register(Ssr, SsrAdmin)

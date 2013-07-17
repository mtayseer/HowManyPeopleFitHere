from django.contrib import admin
from olwidget.admin import GeoModelAdmin
from olwidget.widgets import InfoMap

from .models import Area

class AreaAdmin(GeoModelAdmin):
    list_display = ('name', 'area_sq_km', 'people_in_area', 'map')
    options = {
        'layers': ['osm.mapnik'],
        'default_lat': 30.021915,
        'default_lon': 31.231899,
        'default_zoom': 12
    }

    def map(self, model):
        model_map = InfoMap([
                [model.area, model.name]
            ], options={
                'map_div_style': {'width': '540px', 'height': '300px'},
            })
        AreaAdmin.Media = model_map.media
        return unicode(model_map)
    map.allow_tags = True

    @property
    def media(self):
        return InfoMap([]).media


admin.site.register(Area, AreaAdmin)
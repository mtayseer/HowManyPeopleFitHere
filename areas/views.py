from django.shortcuts import render, get_object_or_404
from django import forms
from olwidget.fields import MapField, EditableLayerField
from .models import Area

class MapEditor(forms.Form):
    area = MapField([
            EditableLayerField({'geometry': 'polygon', 'name': 'area'})
        ], options={
                'map_div_style': {'width': '800px', 'height': '300px'},
        })


def home(request, area_id=1):
    areas = Area.objects.filter(active=True)
    selected_area = areas.get(id=area_id)
    map = MapEditor(initial={'area': selected_area.area})
    return render(request, 'home.html', {'map': map, 'areas': areas})

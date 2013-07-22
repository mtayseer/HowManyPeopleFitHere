from django.shortcuts import render
from django import forms
from olwidget.fields import MapField, EditableLayerField
from .models import Area

class MapEditor(forms.Form):
    area = MapField([
            EditableLayerField({'geometry': 'polygon', 'name': 'area'})
        ], options={
                'map_div_style': {'width': '800px', 'height': '300px'},
        })

def home(request):
    map = MapEditor(initial={'area': Area.objects.all()[0].area})
    return render(request, 'home.html', {'map': map})
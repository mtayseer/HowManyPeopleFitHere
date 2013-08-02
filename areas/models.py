from django.contrib.gis.db import models

class AreaManager(models.Manager):
    def get_query_set(self):
        return super(AreaManager, self).get_query_set().extra(select={'_area_sq_km': 'st_area(area)'})

class Area(models.Model):
    name = models.CharField(max_length=500)
    area = models.MultiPolygonField(geography=True, srid=4326)
    active = models.BooleanField(default=True)

    def area_sq_km(self):
        return self._area_sq_km / 10 ** 6
    area_sq_km.short_description = 'Area (km2)'

    def people_in_area(self):
        return '{:,.0f}'.format(self.area_sq_km() * 10 ** 6 / 0.25)

    objects = AreaManager()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name
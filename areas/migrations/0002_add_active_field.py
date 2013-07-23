# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Area.active'
        db.add_column('areas_area', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Area.active'
        db.delete_column('areas_area', 'active')


    models = {
        'areas.area': {
            'Meta': {'ordering': "['id']", 'object_name': 'Area'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'geography': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['areas']
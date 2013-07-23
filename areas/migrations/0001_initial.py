# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table('areas_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('area', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(geography=True)),
        ))
        db.send_create_signal('areas', ['Area'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table('areas_area')


    models = {
        'areas.area': {
            'Meta': {'object_name': 'Area'},
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'geography': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['areas']
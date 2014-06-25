# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Newsletter'
        db.create_table(u'newsletter_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('released_date', self.gf('django.db.models.fields.DateField')()),
            ('added_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('newsletter', ['Newsletter'])


    def backwards(self, orm):
        # Deleting model 'Newsletter'
        db.delete_table(u'newsletter_newsletter')


    models = {
        'newsletter.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'added_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'released_date': ('django.db.models.fields.DateField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['newsletter']
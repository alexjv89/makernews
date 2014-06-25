# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Newsletter.number'
        db.add_column(u'newsletter_newsletter', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default='1'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Newsletter.number'
        db.delete_column(u'newsletter_newsletter', 'number')


    models = {
        'newsletter.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'added_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'released_date': ('django.db.models.fields.DateField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['newsletter']
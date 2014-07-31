# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'menu_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'menu', ['Menu'])

        # Adding model 'MenuItem'
        db.create_table(u'menu_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('link', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Menu'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.MenuItem'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='hash', max_length=64)),
        ))
        db.send_create_signal(u'menu', ['MenuItem'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'menu_menu')

        # Deleting model 'MenuItem'
        db.delete_table(u'menu_menuitem')


    models = {
        u'menu.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Menu']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'hash'", 'max_length': '64'})
        }
    }

    complete_apps = ['menu']
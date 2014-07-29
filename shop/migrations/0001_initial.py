# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tax'
        db.create_table(u'shop_tax', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'shop', ['Tax'])

        # Adding model 'Currency'
        db.create_table(u'shop_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('factor', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'shop', ['Currency'])

        # Adding model 'Category'
        db.create_table(u'shop_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['Category'])

        # Adding model 'ItemImage'
        db.create_table(u'shop_itemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'shop', ['ItemImage'])

        # Adding model 'Item'
        db.create_table(u'shop_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('descripion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Tax'], null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Currency'])),
        ))
        db.send_create_signal(u'shop', ['Item'])

        # Adding M2M table for field categories on 'Item'
        m2m_table_name = db.shorten_name(u'shop_item_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'shop.item'], null=False)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'category_id'])

        # Adding M2M table for field images on 'Item'
        m2m_table_name = db.shorten_name(u'shop_item_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'shop.item'], null=False)),
            ('itemimage', models.ForeignKey(orm[u'shop.itemimage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'itemimage_id'])


    def backwards(self, orm):
        # Deleting model 'Tax'
        db.delete_table(u'shop_tax')

        # Deleting model 'Currency'
        db.delete_table(u'shop_currency')

        # Deleting model 'Category'
        db.delete_table(u'shop_category')

        # Deleting model 'ItemImage'
        db.delete_table(u'shop_itemimage')

        # Deleting model 'Item'
        db.delete_table(u'shop_item')

        # Removing M2M table for field categories on 'Item'
        db.delete_table(db.shorten_name(u'shop_item_categories'))

        # Removing M2M table for field images on 'Item'
        db.delete_table(db.shorten_name(u'shop_item_images'))


    models = {
        u'shop.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'shop.currency': {
            'Meta': {'object_name': 'Currency'},
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'shop.item': {
            'Meta': {'object_name': 'Item'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shop.Category']", 'symmetrical': 'False'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Currency']"}),
            'descripion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shop.ItemImage']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'tax': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Tax']", 'null': 'True', 'blank': 'True'})
        },
        u'shop.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'shop.tax': {
            'Meta': {'object_name': 'Tax'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['shop']
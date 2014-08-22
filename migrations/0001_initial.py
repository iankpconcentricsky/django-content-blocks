# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JoinTable'
        db.create_table(u'content_blocks_jointable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content_set', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_block_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content_block_set', to=orm['contenttypes.ContentType'])),
            ('content_block_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'content_blocks', ['JoinTable'])

        # Adding model 'ThreeColumn'
        db.create_table(u'content_blocks_threecolumn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_block_title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('image1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('body1', self.gf('ckeditor.fields.HTMLField')()),
            ('image2', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('body2', self.gf('ckeditor.fields.HTMLField')()),
            ('image3', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title3', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('body3', self.gf('ckeditor.fields.HTMLField')()),
        ))
        db.send_create_signal(u'content_blocks', ['ThreeColumn'])

        # Adding model 'TwoColumn'
        db.create_table(u'content_blocks_twocolumn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_block_title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('body1', self.gf('ckeditor.fields.HTMLField')()),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('body2', self.gf('ckeditor.fields.HTMLField')()),
        ))
        db.send_create_signal(u'content_blocks', ['TwoColumn'])

        # Adding model 'OneColumn'
        db.create_table(u'content_blocks_onecolumn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_block_title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('image_position', self.gf('django.db.models.fields.CharField')(default='bottom', max_length=10)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('body', self.gf('ckeditor.fields.HTMLField')()),
        ))
        db.send_create_signal(u'content_blocks', ['OneColumn'])

        # Adding model 'Quote'
        db.create_table(u'content_blocks_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_block_title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'content_blocks', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'JoinTable'
        db.delete_table(u'content_blocks_jointable')

        # Deleting model 'ThreeColumn'
        db.delete_table(u'content_blocks_threecolumn')

        # Deleting model 'TwoColumn'
        db.delete_table(u'content_blocks_twocolumn')

        # Deleting model 'OneColumn'
        db.delete_table(u'content_blocks_onecolumn')

        # Deleting model 'Quote'
        db.delete_table(u'content_blocks_quote')


    models = {
        u'content_blocks.jointable': {
            'Meta': {'ordering': "['position']", 'object_name': 'JoinTable'},
            'content_block_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'content_block_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_block_set'", 'to': u"orm['contenttypes.ContentType']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_set'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'content_blocks.onecolumn': {
            'Meta': {'object_name': 'OneColumn'},
            'body': ('ckeditor.fields.HTMLField', [], {}),
            'content_block_title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_position': ('django.db.models.fields.CharField', [], {'default': "'bottom'", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'content_blocks.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'content_block_title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'content_blocks.threecolumn': {
            'Meta': {'object_name': 'ThreeColumn'},
            'body1': ('ckeditor.fields.HTMLField', [], {}),
            'body2': ('ckeditor.fields.HTMLField', [], {}),
            'body3': ('ckeditor.fields.HTMLField', [], {}),
            'content_block_title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title3': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'content_blocks.twocolumn': {
            'Meta': {'object_name': 'TwoColumn'},
            'body1': ('ckeditor.fields.HTMLField', [], {}),
            'body2': ('ckeditor.fields.HTMLField', [], {}),
            'content_block_title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['content_blocks']
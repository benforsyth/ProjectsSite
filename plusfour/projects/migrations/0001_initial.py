# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Owner'
        db.create_table(u'projects_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.TextField')()),
            ('last', self.gf('django.db.models.fields.TextField')()),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('public_source_repository', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'projects', ['Owner'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('icon_path', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('ranking', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'Technology'
        db.create_table(u'projects_technology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('framework', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Technology'])

        # Adding M2M table for field project on 'Technology'
        m2m_table_name = db.shorten_name(u'projects_technology_project')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('technology', models.ForeignKey(orm[u'projects.technology'], null=False)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['technology_id', 'project_id'])


    def backwards(self, orm):
        # Deleting model 'Owner'
        db.delete_table(u'projects_owner')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'Technology'
        db.delete_table(u'projects_technology')

        # Removing M2M table for field project on 'Technology'
        db.delete_table(db.shorten_name(u'projects_technology_project'))


    models = {
        u'projects.owner': {
            'Meta': {'object_name': 'Owner'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'first': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.TextField', [], {}),
            'public_source_repository': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_path': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ranking': ('django.db.models.fields.IntegerField', [], {})
        },
        u'projects.technology': {
            'Meta': {'object_name': 'Technology'},
            'framework': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Project']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['projects']
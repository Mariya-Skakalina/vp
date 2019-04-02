from django_elasticsearch_dsl import DocType, Index, fields
from .models import *

public = Index('publics')
public.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@public.doc_type
class PublicDocument(DocType):
    context = fields.TextField(attr="ctx")
    section = fields.NestedField(properties={
        'name': fields.StringField(),
    })
    author = fields.NestedField(properties={
        'nickname': fields.StringField(),
    })
    topic_public = fields.NestedField(properties={
        'title': fields.StringField(),
        'id': fields.IntegerField()
    })
    class Meta:
        model = Public
        related_models = [Section,Topic]
        fields = [
            'title',
            'id',
            'publication'
        ]

        queryset_pagination = 20
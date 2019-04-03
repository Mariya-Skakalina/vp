from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer

from .models import *

public = Index('publics')
public.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@public.doc_type
class PublicDocument(DocType):
    context = fields.TextField(attr="ctx")
    section = fields.ObjectField(properties={
        'name': fields.StringField(analyzer=html_strip),
    })
    # section = fields.ObjectField(properties={
    #     'to_dict': fields.ObjectField()
    # })
    author = fields.ObjectField(properties={
        'nickname': fields.StringField(analyzer=html_strip),
    })
    topic_public = fields.ObjectField(properties={
        'title': fields.StringField(analyzer=html_strip),
        'id': fields.IntegerField()
    },attr='topic_public')

    class Meta:
        model = Public
        related_models = [Section,Topic]
        fields = [
            'title',
            'id',
            'publication'
        ]

        queryset_pagination = 20


    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        print(related_instance)
        if isinstance(related_instance, Topic):
            return related_instance.public_set.all()
        elif isinstance(related_instance, Section):
            return related_instance.public_set.all()
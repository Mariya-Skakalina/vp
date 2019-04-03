from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer
from .models import User


user = Index('users')
user.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@user.doc_type
class UserDocument(DocType):
    class Meta:
        model = User

        fields = [
            'nickname',
            'id'
        ]
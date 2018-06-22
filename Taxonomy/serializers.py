from .models import Taxonomy, Keyword
from rest_framework import serializers 


        
class KeywordsSerializer(serializers.ModelSerializer):
    taxonomy = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Keyword
        fields = '__all__'

class TaxonomySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Taxonomy
        fields = ["name","keywords","id"]
        read_only_fields = ["keywords","id"]
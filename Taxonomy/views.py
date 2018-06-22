from rest_framework import generics
from .models import Keyword,Taxonomy
from .serializers import KeywordsSerializer, TaxonomySerializer

class ListKeywords(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordsSerializer
    
class DetailKeyword(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordsSerializer

class ListTaxonomy(generics.ListAPIView):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer
    
class DetailTaxonomy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer

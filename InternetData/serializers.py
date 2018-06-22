from .models import DataJob
from rest_framework.serializers import ModelSerializer

class DataJobSerializer(ModelSerializer):
    model = DataJob
    fields = ('keywords','coderunner','type')
from django.forms import ModelForm
from yunwei.models import soft
class softform(ModelForm):
    class Meta:
        model = soft
        # fields = '__all__'
        fields=('name','install_server')
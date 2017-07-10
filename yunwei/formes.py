from django.forms import ModelForm
from yunwei.models import runsql as runsqlmodel
class runsql(ModelForm):
    # lastuptime=forms.DateTimeField()
    # runner=forms.CharField(max_length=20)
    # runserver=forms.CharField(max_length=20)
    # runfile=forms.CharField(max_length=20)
    class Meta:
        model = runsqlmodel
        # fields = '__all__'
        fields=('runserver','runfile')
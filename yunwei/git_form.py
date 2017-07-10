from django.forms import  ModelForm
from yunwei.models import git
class git_form(ModelForm):
    class Meta:
        model=git
        # fields='__all__'
        fields=('gitserver','gitbranch','gitname','notice','possqlphp','mssqlphp')
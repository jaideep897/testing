from django import forms
from .models import technology_list
class NewACCForm(forms.ModelForm):
    class Meta:
        model = technology_list
        fields =['Technology_Name']

    def clean_Technology_Name(self):
        Technology_Name=self.cleaned_data.get('Technology_Name')

        if(Technology_Name==""):
            raise forms.ValidationError('this field cannot be left blank')
            
        for instance in technology_list.objects.all():
            if instance.Technology_Name==Technology_Name:
               raise forms.ValidationError('there is a technology with the name'+Technology_Name)
            return Technology_Name
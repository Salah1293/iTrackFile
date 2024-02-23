from django.forms import ModelForm
from .models import *
from django import forms

#classModel of criminal
class CriminalForm(ModelForm):
    class Meta:
        model = PvdmDocs11
        fields = ['docindex1', 'docindex2', 'docindex6', 'docindex7']
        labels = {
            'docindex1': 'Case Number',
            'docindex2': 'Order Date',
            'docindex6': 'Defendant Last Name',
            'docindex7': 'Defendant First Name'
        }

        widgets = {
            'docindex2': forms.DateInput(attrs={'type': 'date'})
        }

    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))

    def __init__(self, *args, **kwargs):
        super(CriminalForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})


#classModel of civil
class CivilForm(ModelForm):
    class Meta:
        model = PvdmDocs12
        fields = ['docindex1', 'docindex2', 'docindex11', 'docindex12', 'docindex6', 'docindex7']
        
        widgets = {
                'docindex2': forms.DateInput(attrs={'type': 'date'})
            }
        
    last_name = forms.CharField(label='Last Name', required=False)
    first_name = forms.CharField(label='First Name', required=False)
    case_number = forms.CharField(label='Case Number', required=False)
        
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))

    def __init__(self, *args, **kwargs):
        super(CivilForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})



#classModel of criminal cases
class CriminalCasesForm(ModelForm):
    class Meta:
        model = PvdmDocs17
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4']
        labels = {
            'docindex1': 'Date',
            'docindex2': 'Case Number',
            'docindex3': 'Last/corporation',
            'docindex4': 'First'
        }

        widgets = {
            'docindex1': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(CriminalCasesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})


#classModel of criminal junevile
class CriminalJuvenileForm(ModelForm):
    class Meta:
        model = PvdmDocs13
        fields = ['docindex1', 'docindex2', 'docindex6', 'docindex7']
        labels = {
            'docindex1': 'Case Number',
            'docindex2': 'Order Date',
            'docindex6': 'Defendant Last Name',
            'docindex7': 'Defendant First Name'
        }

        widgets = {
            'docindex2' : forms.DateInput(attrs={'type':'date'})
        }

    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type' : 'date'}))

    def __init__(self, *args,**kwargs):
        super(CriminalJuvenileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})


#classForm of historic index
class HistoricIndexCardsForm(ModelForm):
    class Meta:
        model = PvdmDocs114
        fields = ['docindex1', 'docindex2']
        labels = {
            'docindex1' : 'Last Name',
            'docindex2' : 'First Name',
        }


    def __init__(self, *args, **kwargs):
        super(HistoricIndexCardsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of historic order book
class HistoricOrderBooksForm(ModelForm):
    class Meta:
        model = PvdmDocs113
        fields = ['docindex2']
        labels = {
            'docindex2' : 'Year'
        }


    def __init__(self, *args, **kwargs):
        super(HistoricOrderBooksForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})
 
            
#classForm of hr
class HrForm(ModelForm):
    class Meta:
        model = PvdmDocs15
        fields = ['docindex1', 'docindex2', 'docindex3']
        labels = {
            'docindex1' : 'Last Name',
            'docindex2' : 'First Name',
            'docindex3' : 'EIN'
        }


    def __init__(self, *args, **kwargs):
        super(HrForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of bond books
class BondBooksForm(ModelForm):
    class Meta:
        model = PvdmDocs116
        fields = ['docindex1', 'docindex2']
        labels = {
            'docindex1' : 'Book',
            'docindex2' : 'Page',
        }


    def __init__(self, *args, **kwargs):
        super(BondBooksForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of Charters
class ChartersForm(ModelForm):
    class Meta:
        model = PvdmDocs19
        fields = ['docindex1', 'docindex2', 'docindex3']
        labels = {
            'docindex1' : 'Charter Name',
            'docindex2' : 'Book',
            'docindex3' : 'Page'
        }


    def __init__(self, *args, **kwargs):
        super(ChartersForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of Concealed Weapons
class ConcealedWeaponsForm(ModelForm):
    class Meta:
        model = PvdmDocs112
        fields = ['docindex1', 'docindex7', 'docindex8', 'docindex9']
        labels = {
            'docindex1' : 'Case Number',
            'docindex7' : 'Subject Company',
            'docindex8' : 'Subject Last Name',
            'docindex9' : 'Subject First Name'
        }


    def __init__(self, *args, **kwargs):
        super(ConcealedWeaponsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of indictments
class IndictmentsForm(ModelForm):
    class Meta:
        model = PvdmDocs110
        fields = ['docindex1', 'docindex3', 'docindex5']
        labels = {
            'docindex1' : 'Case Number',
            'docindex3' : 'Defendant First Name',
            'docindex5' : 'Defendant Last Name'
        }


    def __init__(self, *args, **kwargs):
        super(IndictmentsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of law & chancery
class LawChanceryForm(ModelForm):
    class Meta:
        model = PvdmDocs16
        fields = ['docindex1', 'docindex2']
        labels = {
            'docindex1' : 'Date',
            'docindex2' : 'LAW/CHANCERY#',
        }


    def __init__(self, *args, **kwargs):
        super(LawChanceryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})
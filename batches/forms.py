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
        fields = ['docindex1', 'docindex2', 'docindex11', 'docindex12',
                   'docindex6', 'docindex7','docindex17','docindex16']
        
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

    BOOK_TYPE_CHOICES = [
    ('bond_book_1', 'Bond Book 1'),
    ('court_order_superior', 'Court Order Superior'),
    ('court_quarterly_sessions', 'Court Quarterly Sessions'),
    ('estray_book', 'Estray Book'),
    ('land_causes_1', 'Land Causes 1'),
    ('land_causes_2', 'Land Causes 2'),
    ('land_records_long_standing', 'Land Records Long Standing'),
    ('minute_book', 'Minute Book'),
    ('ordinary_bond_book', 'Ordinary Bond Book'),
    ('quite_rents', 'Quite Rents'),
    ('reg_free_negroes_val_2', 'Reg Free Negroes Val 2'),
    ('reg_free_negroes_val_3', 'Reg Free Negroes Val 3'),
    ('roads', 'Roads'),
    ('surveys', 'Surveys'),
]
    
    docindex1 = forms.ChoiceField(choices=BOOK_TYPE_CHOICES, required=True)


    class Meta:
        model = PvdmDocs113
        fields = ['docindex1', 'docindex2']
        labels = {
            'docindex1' : 'Book Type',
            'docindex2' : 'Year',
        }


    def __init__(self, *args, **kwargs):
        super(HistoricOrderBooksForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})
        self.fields['docindex1'].label = 'Book Type'


            
#classForm of hr
class HrForm(ModelForm):
    class Meta:
        model = PvdmDocs115
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


#classForm of destruction orders
class DestructionOrdersForm(ModelForm):
    class Meta:
        model = PvdmDocs115
        fields = ['docindex1', 'docindex2']
        labels = {
            'docindex1' : 'Order Type',
            'docindex2' : 'Order Date',
        }


    def __init__(self, *args, **kwargs):
        super(DestructionOrdersForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of adoption
class AdoptionForm(ModelForm):
    class Meta:
        model = PvdmDocs14
        fields = ['docindex1', 'docindex6','docindex7', 'docindex16','docindex17']
        labels = {
            'docindex1' : 'Case Number',
            'docindex6' : 'Plaintiff Last Name',
            'docindex7' : 'Plaintiff First Name',
            'docindex16' : 'Subject Last Name',
            'docindex17' : 'Subject First Name',
        }


    def __init__(self, *args, **kwargs):
        super(AdoptionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})


#classForm of clerk orders
class ClerkOrdersForm(ModelForm):
    class Meta:
        model = PvdmDocs18
        fields = ['docindex1', 'docindex8','docindex9', 'docindex10','docindex13',
                  'docindex14', 'docindex15','docindex18', 'docindex19','docindex20']
        labels = {
            'docindex1' : 'Case Number',
            'docindex8' : 'Plaintiff Company',
            'docindex9' : 'Plaintiff Last Name',
            'docindex10' : 'Plaintiff First Name',
            'docindex13' : 'Defendant Company',
            'docindex14' : 'Defendant Last Name',
            'docindex15' : 'Defendant First Name',
            'docindex18' : 'Subject Company',
            'docindex19' : 'Subject Last Name',
            'docindex20' : 'Subject First Name',
        }


    def __init__(self, *args, **kwargs):
        super(ClerkOrdersForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'autocomplete' : 'off'})



############################# update cards ###################################

#abstract class for update process
class BaseUpdateForm(ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(BaseUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})





#update card bond books
class UpdateBondBooks(BaseUpdateForm):
    class Meta:
        model = PvdmDocs116
        fields = ['docindex1', 'docindex2']

        labels = {
            'docindex1' : 'book',
            'docindex2' : 'page'
        }




#update card chaeters
class UpdateCharters(BaseUpdateForm):
    class Meta:
        model = PvdmDocs19
        fields = ['docindex1', 'docindex2', 'docindex3']

        labels = {
            'docindex1' : 'Charter Name',
            'docindex2' : 'book',
            'docindex3' : 'page'
        }



#update card adoption
class UpdateAdoption(BaseUpdateForm):
    class Meta:
        model = PvdmDocs14
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11', 'docindex12', 'docindex13', 'docindex14', 'docindex15',
                  'docindex16', 'docindex17', 'docindex18', 'docindex19', 'docindex20',
                  'docindex21', 'docindex22']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Judge Name',
            'docindex4' : 'Sealed',
            'docindex5' : 'Plaintiff Company',
            'docindex6' : 'Plaintiff Last Name',
            'docindex7' : 'Plaintiff First Name',
            'docindex8' : 'Plaintiff Middle Name',
            'docindex9' : 'Plaintiff Suffix',
            'docindex10' : 'Defendant Company',
            'docindex11' : 'Defendant Last Name',
            'docindex12' : 'Defendant First Name',
            'docindex13' : 'Defendant Middle Name',
            'docindex14' : 'Defendant Suffix',
            'docindex15' : 'Subject Company',
            'docindex16' : 'Subject Last Name',
            'docindex17' : 'Subject First Name',
            'docindex18' : 'Subject Middle Name',
            'docindex19' : 'Subject Suffix',
            'docindex20' : 'Date Scanned',
            'docindex21' : 'Judge Initials',
            'docindex22' : 'Scan Date'
        }



#update card civil
class UpdateCivil(BaseUpdateForm):
    class Meta:
        model = PvdmDocs12
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11', 'docindex12', 'docindex13', 'docindex14', 'docindex15',
                  'docindex16', 'docindex17', 'docindex18', 'docindex19', 'docindex20',
                  'docindex21', 'docindex22']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Judge Name',
            'docindex4' : 'Sealed',
            'docindex5' : 'Plaintiff Company',
            'docindex6' : 'Plaintiff Last Name',
            'docindex7' : 'Plaintiff First Name',
            'docindex8' : 'Plaintiff Middle Name',
            'docindex9' : 'Plaintiff Suffix',
            'docindex10' : 'Defendant Company',
            'docindex11' : 'Defendant Last Name',
            'docindex12' : 'Defendant First Name',
            'docindex13' : 'Defendant Middle Name',
            'docindex14' : 'Defendant Suffix',
            'docindex15' : 'Subject Company',
            'docindex16' : 'Subject Last Name',
            'docindex17' : 'Subject First Name',
            'docindex18' : 'Subject Middle Name',
            'docindex19' : 'Subject Suffix',
            'docindex20' : 'Date Scanned',
            'docindex21' : 'Judge Initials',
            'docindex22' : 'Scan Date'
        }


#update card clerk orders
class UpdateClerkOrders(BaseUpdateForm):
    class Meta:
        model = PvdmDocs18
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11', 'docindex12', 'docindex13', 'docindex14', 'docindex15',
                  'docindex16', 'docindex17', 'docindex18', 'docindex19', 'docindex20',
                  'docindex21', 'docindex22', 'docindex23']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Clerk Key',
            'docindex4' : 'Clerk Name',
            'docindex5' : 'Sealed',
            'docindex6' : 'Document Type Code',
            'docindex7' : 'Document Type',
            'docindex8' : 'Plaintiff Company',
            'docindex9' : 'Plaintiff Last Name',
            'docindex10' : 'Plaintiff First Name',
            'docindex11' : 'Plaintiff Middle Name',
            'docindex12' : 'Plaintiff Suffix',
            'docindex13' : 'Defendant Company',
            'docindex14' : 'Defendant Last Name',
            'docindex15' : 'Defendant First Name',
            'docindex16' : 'Defendant Middle Name',
            'docindex17' : 'Defendant Suffix',
            'docindex18' : 'Subject Company',
            'docindex19' : 'Subject Last Name',
            'docindex20' : 'Subject First Name',
            'docindex21' : 'Subject Middle Name',
            'docindex22' : 'Subject Suffix',
            'docindex23' : 'Date Scanned'
        }


#update card concealed weapons
class UpdateConcealedWeapons(BaseUpdateForm):
    class Meta:
        model = PvdmDocs112
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Judge Initials',
            'docindex4' : 'Judge Name',
            'docindex5' : 'Sealed',
            'docindex6' : 'Scan Date',
            'docindex7' : 'Subject Company',
            'docindex8' : 'Subject Last Name',
            'docindex9' : 'Subject First Name',
            'docindex10' : 'Subject Middle Name',
            'docindex11' : 'Subject Suffix'
            }
        

#update card criminal
class UpdateCriminal(BaseUpdateForm):
    class Meta:
        model = PvdmDocs11
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11', 'docindex12', 'docindex13', 'docindex14', 'docindex15',
                  'docindex16', 'docindex17', 'docindex18', 'docindex19', 'docindex20',
                  'docindex21', 'docindex22']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Judge Name',
            'docindex4' : 'Sealed',
            'docindex5' : 'Plaintiff Company',
            'docindex6' : 'Plaintiff Last Name',
            'docindex7' : 'Plaintiff First Name',
            'docindex8' : 'Plaintiff Middle Name',
            'docindex9' : 'Plaintiff Suffix',
            'docindex10' : 'Defendant Company',
            'docindex11' : 'Defendant Last Name',
            'docindex12' : 'Defendant First Name',
            'docindex13' : 'Defendant Middle Name',
            'docindex14' : 'Defendant Suffix',
            'docindex15' : 'Subject Company',
            'docindex16' : 'Subject Last Name',
            'docindex17' : 'Subject First Name',
            'docindex18' : 'Subject Middle Name',
            'docindex19' : 'Subject Suffix',
            'docindex20' : 'Date Scanned',
            'docindex21' : 'Judge Initials',
            'docindex22' : 'Scan Date'
        }


#update card criminal cases
class UpdateCriminalCases(BaseUpdateForm):
    class Meta:
        model = PvdmDocs17
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5']

        labels = {
            'docindex1' : 'Date',
            'docindex2' : 'Case Number',
            'docindex3' : 'Last/Corporation',
            'docindex4' : 'First',
            'docindex5' : 'Middle'
            }
        


#update card criminal Juvenile
class UpdateCriminalJuvenile(BaseUpdateForm):
    class Meta:
        model = PvdmDocs13
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8', 'docindex9', 'docindex10',
                  'docindex11', 'docindex12', 'docindex13', 'docindex14', 'docindex15',
                  'docindex16', 'docindex17', 'docindex18', 'docindex19', 'docindex20',
                  'docindex21', 'docindex22']

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Order Date',
            'docindex3' : 'Judge Name',
            'docindex4' : 'Sealed',
            'docindex5' : 'Plaintiff Company',
            'docindex6' : 'Plaintiff Last Name',
            'docindex7' : 'Plaintiff First Name',
            'docindex8' : 'Plaintiff Middle Name',
            'docindex9' : 'Plaintiff Suffix',
            'docindex10' : 'Defendant Company',
            'docindex11' : 'Defendant Last Name',
            'docindex12' : 'Defendant First Name',
            'docindex13' : 'Defendant Middle Name',
            'docindex14' : 'Defendant Suffix',
            'docindex15' : 'Subject Company',
            'docindex16' : 'Subject Last Name',
            'docindex17' : 'Subject First Name',
            'docindex18' : 'Subject Middle Name',
            'docindex19' : 'Subject Suffix',
            'docindex20' : 'Date Scanned',
            'docindex21' : 'Judge Initials',
            'docindex22' : 'Scan Date'
        }


#update card Destructiojn Orders
class UpdateDestructionOrders(BaseUpdateForm):
    class Meta:
        model = PvdmDocs115
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7']

        labels = {
            'docindex1' : 'Order Type',
            'docindex2' : 'Order Date',
            'docindex3' : 'Start Date',
            'docindex4' : 'End Date',
            'docindex5' : 'Destruction Complete Date',
            'docindex6' : 'First Case Number',
            'docindex7' : 'Last Case Number'
            }


#update card Destructiojn Orders
class UpdateDestructionOrders(BaseUpdateForm):
    class Meta:
        model = PvdmDocs115
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7']

        labels = {
            'docindex1' : 'Order Type',
            'docindex2' : 'Order Date',
            'docindex3' : 'Start Date',
            'docindex4' : 'End Date',
            'docindex5' : 'Destruction Complete Date',
            'docindex6' : 'First Case Number',
            'docindex7' : 'Last Case Number'
            }


#update card historic index cards
class UpdateHistoricIndexCards(BaseUpdateForm):
    class Meta:
        model = PvdmDocs114
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4', 'docindex5',
                  'docindex6', 'docindex7', 'docindex8']

        labels = {
            'docindex1' : 'Last Name',
            'docindex2' : 'First Name',
            'docindex3' : 'Subject',
            'docindex4' : 'Record Source',
            'docindex5' : 'Book Record',
            'docindex6' : 'Page',
            'docindex7' : 'Date',
            'docindex7' : 'Comments'
            }


#update card historic order books
class UpdateHistoricOrderBooks(BaseUpdateForm):

    BOOK_TYPE_CHOICES = [
    ('bond_book_1', 'Bond Book 1'),
    ('court_order_superior', 'Court Order Superior'),
    ('court_quarterly_sessions', 'Court Quarterly Sessions'),
    ('estray_book', 'Estray Book'),
    ('land_causes_1', 'Land Causes 1'),
    ('land_causes_2', 'Land Causes 2'),
    ('land_records_long_standing', 'Land Records Long Standing'),
    ('minute_book', 'Minute Book'),
    ('ordinary_bond_book', 'Ordinary Bond Book'),
    ('quite_rents', 'Quite Rents'),
    ('reg_free_negroes_val_2', 'Reg Free Negroes Val 2'),
    ('reg_free_negroes_val_3', 'Reg Free Negroes Val 3'),
    ('roads', 'Roads'),
    ('surveys', 'Surveys'),
]
    
    docindex1 = forms.ChoiceField(choices=BOOK_TYPE_CHOICES, required=True)


    class Meta:
        model = PvdmDocs113
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4']

        labels = {
            'docindex1' : 'Book Type',
            'docindex2' : 'Year',
            'docindex3' : 'Page A',
            'docindex4' : 'Page B'
            }
        
        
    def __init__(self, *args, **kwargs):
        super(UpdateHistoricOrderBooks, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})

        self.fields['docindex1'].label = 'Book Type'


#update card hr
class UpdateHr(BaseUpdateForm):

    EMPLOYMENT_TYPE_CHOICES = [
        ('attached', 'Attached'),
        ('court_intern', 'Court Intern'),
        ('judicial_intern', 'Judicial Intern'),
        ('lt', 'LT'),
        ('merit', 'Merit'),
        ('volunteer', 'Volunteer'),
    ]

    DOCUMENT_TYPE_CHOICES = [
        ('medical', 'Medical'),
        ('personnel', 'Personnel'),
    ]


    docindex4 = forms.ChoiceField(choices=EMPLOYMENT_TYPE_CHOICES, required=True)
    docindex5 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    docindex6 = forms.ChoiceField(choices=DOCUMENT_TYPE_CHOICES, required=True)


    class Meta:
        model = PvdmDocs15
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4',
                  'docindex5', 'docindex6'
                  ]

        labels = {
            'docindex1' : 'Last Name',
            'docindex2' : 'First Name',
            'docindex3' : 'EIN',
            'docindex4' : 'Employment Type',
            'docindex5' : 'Scan Date',
            'docindex6' : 'Document Type'
            }
        
    def __init__(self, *args, **kwargs):
        super(UpdateHr, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'autocomplete': 'off'})

        self.fields['docindex4'].label = 'Employment Type'
        self.fields['docindex5'].label = 'Scan Date'
        self.fields['docindex6'].label = 'Document Type'


#update card indictments
class UpdateIndictments(BaseUpdateForm):
    class Meta:
        model = PvdmDocs110
        fields = ['docindex1', 'docindex2', 'docindex3', 'docindex4',
                  'docindex5', 'docindex6', 'docindex7', 'docindex8',
                  'docindex9'
                  ]

        labels = {
            'docindex1' : 'Case Number',
            'docindex2' : 'Defendant Company',
            'docindex3' : 'Defendant First Name',
            'docindex4' : 'Defendant Middle',
            'docindex5' : 'Defendant Last Name',
            'docindex6' : 'Defendant Suffix',
            'docindex7' : 'ROA Code',
            'docindex8' : 'ROA Date',
            'docindex9' : 'Scan Date'
            }


#update card Law Chancery
class UpdateLawChancery(BaseUpdateForm):
    class Meta:
        model = PvdmDocs16
        fields = ['docindex1', 'docindex2'
                  ]

        labels = {
            'docindex1' : 'Date',
            'docindex2' : 'Law/Chancery#'
            }


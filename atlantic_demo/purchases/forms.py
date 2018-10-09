from django import forms

class PurchaseFileForm(forms.Form):
    csv_upload_file = forms.FileField()
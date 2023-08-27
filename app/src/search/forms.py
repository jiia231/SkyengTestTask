from crispy_forms.helper import FormHelper
from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

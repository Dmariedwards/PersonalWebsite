from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from webmodels.models import Section
from django.contrib import messages



class AddSectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddSectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        """ this line sets your form's method to post"""
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', u'Submit', css_class='btn btn-success'))

    name = forms.CharField(
        label="Section Name",
        max_length=50,
        required=True,
    )
    text = forms.CharField(
        label="Description",
        widget=forms.Textarea,
        max_length=500,
        required=False,
    )
    pdffile = forms.FileField(
        label="PDF file",
        required=False)
    image = forms.ImageField(
    label="Image file",
    required=False)

    def clean_photo(self,request):
        image_file = self.cleaned_data.get('image')
        error = 0
        if image_file:
            if image_file.size > 2621440:
                messages.add_message(request, messages.ERROR, 'Image File too large')
                error = 1
            elif image_file.name.endswith(".jpg") is True or image_file.name.endswith(".png") is True or image_file.name.endswith(".gif") is True:
                return image_file,error
            else:
                messages.add_message(request, messages.ERROR, "Only .jpg, .png, .gif images are accepted")
                error = 1
        return image_file,error

    def clean_file(self,request):
        pdf = self.cleaned_data.get('pdffile')
        error = 0
        if pdf:
            if pdf.size > 5242880:
                messages.add_message(request, messages.ERROR, 'PDF File too large')
                error = 1
            elif not pdf.name.endswith(".pdf"):
                messages.add_message(request, messages.ERROR, 'This is not a PDF file')
                error=1
        return pdf,error

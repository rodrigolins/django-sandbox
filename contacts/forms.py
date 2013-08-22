from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms

from contacts.models import Author

class AuthorForm(forms.Form):
    name = forms.CharField()

class AuthorCreate(CreateView):
    model = Author
    template_name_suffix = '_create_form'
    # fields = ['name']

class AuthorUpdate(UpdateView):
    model = Author
    template_name_suffix = '_update_form'
    # fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    template_name_suffix = '_delete_form'
    success_url = '/contacts/author/viewall/'
    # fields = ['name']

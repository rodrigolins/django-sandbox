from django.db import models
from django import forms
from django.core.urlresolvers import reverse

class Contact(models.Model):
    name = models.CharField('Name', max_length=200)
    email = models.EmailField()
    address = models.CharField('Address', max_length=200)
    #number = models.IntegerField('Number', max_length=10)
    #city = models.CharField('City', max_length=50)
    #state = models.CharField('State', max_length=50)
    #country = models.CharField('Country', max_length=50)
    #birthDate = models.DateTimeField('Birth date')

    def __unicode__(self):
        return self.name

class ContactForm(forms.ModelForm):
    #template_name = 'contacts/addcontactform.html'
    class Meta:
        model = Contact

class Author(models.Model):
    name = models.CharField('Name', max_length=200)

    def get_absolute_url(self):
        return reverse('contacts:author-detail', kwargs={'pk': self.pk})


from django.views import generic
from contacts.models import Contact, ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contacts.models import Author

class IndexView(generic.TemplateView):
    template_name = 'contacts/index.html'

# Use TemplateView just to show a simple page without recovering data.
# Renders a given template, with the context containing parameters captured in the URL.
class AddContactView(generic.TemplateView):
    model = Contact
    template_name = 'contacts/addcontactform.html'

# Use ListView to show a list of elements.
# The method get_queryset must be implemented.
class ListView(generic.ListView):
    model = Contact
    template_name = 'contacts/listcontacts.html'

    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        all_contacts = Contact.objects.all()
        return all_contacts

# Use DetailView to show something based on one value, like the id
class DetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/detail.html'

def save(request):
    print('salvou')

def addcontact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print(form.cleaned_data)
            print(request.POST['name'])
            form.save()

            return HttpResponseRedirect('/contacts/listcontacts') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contacts/addcontactform.html', {
        'form': form,
    })

class AuthorIndexView(generic.TemplateView):
    template_name = 'contacts/author_index.html'

class AuthorViewAllView(generic.ListView):
    model = Author
    template_name = 'contacts/author_viewall.html'
    context_object_name = 'authors_list'

    def get_queryset(self):
        all_authors = Author.objects.all()
        return all_authors

class AuthorView(generic.DeleteView):
    model = Author
    template_name = 'contacts/author_detail.html'

class AuthorViewSearchResult(generic.ListView):
    model = Author
    template_name = 'contacts/author_viewall.html'
    context_object_name = 'authors_list'
    def get_queryset(self):
        #ListView.POST['word']
        word = self.kwargs['word']
        #all_authors = Author.objects.filter(name__contains = word)
        all_authors = Author.objects.filter(name__startswith = word)
        return all_authors

'''
class AuthorView(generic.edit.FormView):
    template_name = 'contacts/author_detail.html'
    form_class = AuthorForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.name)
        return super(AuthorView, self).form_valid(form)
'''

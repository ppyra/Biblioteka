from django.views.generic import DetailView, FormView
#from .models import Message
from .forms import MessageForm

#class MessageDetailView(DetailView):
#    mode = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'
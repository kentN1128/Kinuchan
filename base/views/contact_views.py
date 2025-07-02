from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from base.forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('done')

    def form_valid(self, form):
        form.save()  # DB保存
        # メール送信もここに書ける
        return super().form_valid(form)
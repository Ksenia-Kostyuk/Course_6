from django.forms import ModelForm, BooleanField

from mailings.models import Mailings, Messages


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField) :
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class MailingsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailings
        fields = '__all__'


class MessagesForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'

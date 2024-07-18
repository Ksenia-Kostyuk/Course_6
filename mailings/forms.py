from django.forms import ModelForm, BooleanField

from mailings.models import Mailings, Messages


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class MailingsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailings
        exclude = ('owner',)


class MessagesForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Messages
        exclude = ('owner',)


class MailingsModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailings
        fields = ('status', 'is_active')


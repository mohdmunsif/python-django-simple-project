from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Entries


class EntriesForm(forms.ModelForm):

    class Meta:
        model = Entries
        fields = ('toyname', 'descr', 'url', 'age_lower', 'age_upper',
                  'image_upload',)
        labels = {
            'name': _('Toy Name'),
            'descr': _('Description'),
            'url': _('URL'),
            'age_lower': _('Min Age'),
            'age_upper': _('Max Age'),
            'image_upload': _('Image Uploaded'),
        }

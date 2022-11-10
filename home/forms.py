from django import forms
from .models import Item

class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'image_url']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        image_url = data.get('image_url')
        qs = Item.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} already in use!')
        if 'http' not in image_url:
            self.add_error('image_url', 'Image is not the URL!')
        return data


class ItemFormsOld(forms.Form):
        title = forms.CharField()
        status = forms.BooleanField()
        image_url = forms.CharField()
    
        # def clean_title(self):
        #     cleaned_data = self.cleaned_data
        #     title = cleaned_data.get('title')
        #     if title.lower().strip() == 'test':
        #         raise forms.ValidationError('Exist!')
        #     return title

        def clean(self):
            cleaned_data = self.cleaned_data
            title = cleaned_data.get('title')
            image_url = cleaned_data.get('image_url')
            if title.lower().strip() == 'test':
                self.add_error('title', 'Exists!')
            if 'http' not in image_url:
                self.add_error('image_url', 'Image is not the URL!')
            return cleaned_data

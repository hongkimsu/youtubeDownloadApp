from django import forms

class DirectoryForm(forms.Form):
    directory = forms.CharField(label='Save to directory:', max_length=200)
    file = forms.FileField(label='Upload file:')
    
    def clean_directory(self):
        directory = self.cleaned_data.get('directory')
        # Add your custom validation for the directory field here
        return directory


class userForm(forms.Form):
    url = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Past YouTube url here...'}))
    CHOICES = (
        ('lowRes','Low Resolution (360p)'),
        ('highRes','High Resolution (1080p)'),
    )
    resolution = forms.ChoiceField(widget=forms.RadioSelect,
                choices=CHOICES,initial='lowRes')
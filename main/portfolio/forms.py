from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Name",
                'autocomplete': 'off',
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Email",
                'autocomplete': 'off',
                "class": "form-control"
            }
        ),
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject",
                'autocomplete': 'off',
                "class": "form-control"
            }
        )
    )
    content = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Input text",
                'autocomplete': 'off',
                "class": "form-control"
            }
        )
    )

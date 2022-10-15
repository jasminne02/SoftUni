from django import forms


class PersonForm(forms.Form):
    OCCUPANCES = (
        (1, 'Child'),
        (2, 'Teen'),
        (3, 'Adult')
    )

    your_name = forms.CharField(
        max_length=30,
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(),
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )

    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )

    story = forms.CharField(
        widget=forms.Textarea(),
    )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCES,
        widget=forms.Select()
    )

    occupancy2 = forms.ChoiceField(
        choices=OCCUPANCES,
        widget=forms.RadioSelect(),
    )


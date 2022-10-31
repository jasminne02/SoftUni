from django import forms

from CarCollectionApp.web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super(ProfileCreateForm, self).__init__(*args, **kwargs)
        self.__set_hidden_password_input()
        self.__set_hidden_fields()

    def __set_hidden_password_input(self):
        self.fields['password'].widget = forms.PasswordInput()

    def __set_hidden_fields(self):
        self.fields['first_name'].widget = forms.HiddenInput()
        self.fields['last_name'].widget = forms.HiddenInput()
        self.fields['profile_picture'].widget = forms.HiddenInput()


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super(ProfileDeleteForm, self).__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()


class CarBaseFrom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseFrom):
    pass


class CarEditForm(CarBaseFrom):
    pass


class CarDeleteForm(CarBaseFrom):
    def __init__(self, *args, **kwargs):
        super(CarDeleteForm, self).__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.required = False

from django import forms

from GamesPlay.web.models import Profile, Game


class ProfileBaseClass(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseClass):
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


class ProfileEditForm(ProfileBaseClass):
    field_order = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']


class ProfileDeleteForm(ProfileBaseClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

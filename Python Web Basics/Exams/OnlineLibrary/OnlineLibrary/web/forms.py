from django import forms

from OnlineLibrary.web.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookAddForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass

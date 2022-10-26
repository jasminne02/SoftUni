from django import forms

from Recipes.web.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

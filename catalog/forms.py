from django.forms import ModelForm, ValidationError, BooleanField

from catalog.models import Product, Version


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'purchase_price', 'category', 'is_published', 'user']

    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    def check_words(self, text):
        if any(word in text.lower() for word in self.FORBIDDEN_WORDS):
            raise ValidationError(f'Текст не должен содержать слова: {self.FORBIDDEN_WORDS}')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        self.check_words(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        self.check_words(cleaned_data)
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category', 'is_published']


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'number', 'name', 'is_active']

    def clean_is_active(self):
        is_active = self.cleaned_data["is_active"]
        active_version = Version.objects.filter(is_active=True)
        if active_version and is_active:
            raise ValidationError(
                'Может быть указана только одна активная версия.'
                '(Для изменения активной версии, сначала сохраните Продукт без активной версии.)')
        return is_active

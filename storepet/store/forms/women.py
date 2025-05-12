from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from ..models import Categories, Husbands, Women


ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- "


@deconstructible
class RussianValidator:
    """Валидатор на случай, если нужно использовать много раз"""

    code = "russian"

    def __init__(self, message: str = None):
        self.message = message if message else "Должны быть только русские символы"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddWomenForm(forms.Form):
    """Форма не связанная с моделью Women"""
    title = forms.CharField(
        label="Заголовок",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        validators=[
            MinLengthValidator(limit_value=3, message="Слишком короткий заголовок!"),
            MaxLengthValidator(limit_value=100, message="Превышен максимум!"),
            # RussianValidator()
        ],
        error_messages={"required": "Без заголовка никак!"}
    )
    slug = forms.SlugField(
        label="Слаг",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100)
        ]
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "cols": 50,
                "rows": 5
            }
        ),
        required=False,
        label="Описание"
    )
    is_published = forms.BooleanField(required=False, initial=True, label="Статус")
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="Не выбрана",
        label="Категории"
    )
    husband = forms.ModelChoiceField(
        queryset=Husbands.objects.all(),
        required=False,
        empty_label="Не замужем",
        label="Муж"
    )

    def clean_title(self):
        """Метод валидации данных заголовка"""
        title = self.cleaned_data["title"]

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("Должны быть только русские символы")


class AddWomenModelForm(forms.ModelForm):
    """Форма, связанная с моделью Women"""

    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="Не выбрана",
        label="Категории"
    )
    husband = forms.ModelChoiceField(
        queryset=Husbands.objects.all(),
        required=False,
        empty_label="Не замужем",
        label="Муж"
    )

    class Meta:
        model = Women
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "slug": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "cols": 50,
                    "rows": 5
                }
            )
        }

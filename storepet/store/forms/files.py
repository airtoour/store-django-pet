from django import forms


class UploadFilesForm(forms.Form):
    """Форма для загрузки файлов"""

    file = forms.ImageField(label="Изображение")

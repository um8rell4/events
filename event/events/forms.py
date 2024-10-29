from django import forms
from .models import Event, Booking


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bg_image'].required = False

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time', 'max_participants', 'bg_image']
        labels = {'title': 'Название', 'description': 'Описание', 'location': 'Место проведения',
                  'date': 'Дата проведения', 'time': 'Время', 'max_participants': 'Количество участников',
                  'bg_image': 'Фото'}
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control", "placeholder": "dd.mm.yyyy", "type": "date"}),
            'time': forms.TimeInput(attrs={"class": "form-control", "placeholder": "чч:мм", "type": "time"}),
            'max_participants': forms.NumberInput(attrs={"class": "form-control"}),
            'bg_image': forms.FileInput(attrs={"class": "form-control"}),
        }
        date = forms.DateField(
            widget=forms.DateInput(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y']
        )

        time = forms.TimeField(
            widget=forms.TimeInput(format='%H:%M'),
            input_formats=['%H:%M']
        )


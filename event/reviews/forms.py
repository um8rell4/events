from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['comment', 'rating']
        labels = {
            'comment': 'Ваш отзыв', 'rating': 'Ваш рейтинг'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'name': 'review_text',
                                             'id': 'reviewText', 'class': 'form-control', 'rows': '4'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем опцию по умолчанию вручную
        self.fields['rating'].choices = [("", "Выберите рейтинг")] + Review.RATING_CHOICES
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating == "":
            raise forms.ValidationError("Пожалуйста, выберите рейтинг.")
        return rating

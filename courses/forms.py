from django import forms
from django.forms import ModelForm, Textarea

# Model
from courses.models import Review, Comment


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 2})
        }
        # widgets = {
        #     'comment': CKEditorWidget()
        # }


class CommentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['course_slug'] = forms.CharField(
    #         widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['msg']
        widgets = {
            'msg': Textarea(attrs={'cols': 40, 'rows': 2})
        }
        # widgets = {
        #     'msg': CKEditorWidget()
        # }

from django import forms
from .models import CourseInquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = CourseInquiry
        fields = ['full_name', 'email', 'phone', 'selected_course', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'required': True}),
            'selected_course': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any specific goals or questions?'}),
        }
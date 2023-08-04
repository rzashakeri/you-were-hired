from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from disposable_email_checker.validators import validate_disposable_email
from users.models import Profile

signup_form_class_list = "w-full input input-bordered"


class CustomSignupForm(SignupForm):
    is_employer = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'toggle toggle-success'}),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
            "class"
        ] = signup_form_class_list
        self.fields["password1"].widget.attrs[
            "class"
        ] = signup_form_class_list
        self.fields["password1"].widget.attrs[
            "onkeyup"
        ] = "inputChange(this.value)"
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            validate_disposable_email(email)
        except ValidationError:
            raise ValidationError("Please Enter Validation Email, Maybe You Are Use Disposable Email")
        return email
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        is_employer = self.cleaned_data['is_employer']
        profile = Profile(user=user)
        if is_employer:
            profile.role = "employer"
        else:
            profile.role = "applicant"
        profile.save()
        return user

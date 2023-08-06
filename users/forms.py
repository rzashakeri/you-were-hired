from allauth.account.forms import SignupForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

signup_form_class_list = "w-full input input-bordered"


class CustomSignupForm(SignupForm):
    captcha = ReCaptchaField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['captcha'].label = False
        self.fields["username"].widget.attrs[
            "class"
        ] = signup_form_class_list
        self.fields["email"].widget.attrs[
            "class"
        ] = signup_form_class_list
        self.fields["password1"].widget.attrs[
            "class"
        ] = signup_form_class_list
        self.fields["password1"].widget.attrs[
            "onkeyup"
        ] = "inputChange(this.value)"
    
    def save(self, request, user):
        user = super(CustomSignupForm, self).save(request)
        return user

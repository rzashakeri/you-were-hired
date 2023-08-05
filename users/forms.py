from allauth.account.forms import SignupForm

signup_form_class_list = "w-full input input-bordered"


class CustomSignupForm(SignupForm):
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

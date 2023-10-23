import re
from django.core.exceptions import ValidationError



class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ("Le mot de passe doit comporter au moins 8 caractères."),
                code='password_too_short',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least %(min_length)d characters."
        ) % {'min_length': self.min_length}


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                ("Le mot de passe doit contenir au moins 1 chiffre"),
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 digit, 0-9."
        )



class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                ("Le mot de passe doit contenir au moins 1 lettre majuscule"),
                code='password_no_upper',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                ("Le mot de passe doit contenir au moins 1 lettre miniscule"),
                code='password_no_lower',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 lowercase letter, a-z."
        )
from rest_framework.serializers import ValidationError


def validate_name(name: str) -> bool :
    if len(name) < 2 or len(name) > 50:
        raise ValidationError("Name should be between 2 and 50 characters")
    # if any(["$", ""])
    

def validate_password(password: str):
    if not any(x.islower() for x in password):
        raise ValidationError("Password was contain at least one lower case letter")
    if len(password) > 15 or len(password) < 6:
        raise ValidationError("Password must be between 6 and 15 characters")
    if not any(x.isdigit() for x  in password):
        raise ValidationError("Password must have at least one number")
    if not any(x.isalpha() for x in password):
        raise ValidationError("Password must have at least one letter")
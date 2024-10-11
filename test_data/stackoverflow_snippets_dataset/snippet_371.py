# Extracted from https://stackoverflow.com/questions/6618002/using-property-versus-getters-and-setters
class Account(object):
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Invalid email address.')
        self._email = value

a = Account()
a.email = 'badaddress'

class Account(object):
    ...
    def validate(self):
        if '@' not in self.email:
            raise ValueError('Invalid email address.')


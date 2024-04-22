from django.contrib.auth.models import AbstractUser


class AbstractCustomUser(AbstractUser):

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "{} {} ({})".format(self.first_name, self.last_name, self.username)
        if self.last_name:
            return "{} ({})".format(self.last_name, self.username)
        if self.first_name:
            return "{} ({})".format(self.first_name, self.username)
        return "{}".format(self.username)

    def __str__(self):
        if self.first_name and self.last_name:
            return "{} {} ({})".format(self.first_name, self.last_name, self.username)
        if self.last_name:
            return "{} ({})".format(self.last_name, self.username)
        if self.first_name:
            return "{} ({})".format(self.first_name, self.username)
        return self.username

    def get_email_link(self):
        if self.email:
            email_icon = '<i class="fa fa-envelope" aria-hidden="true"></i>'
            return '{}&nbsp;&nbsp;<a href="mailto:{}">{}</a>'.format(
                self.get_full_name(), self.email, email_icon
            )
        return self.get_full_name()

    def get_email_link_with_username(self):
        if self.email:
            return '<a href="mailto:{}">{}</a>'.format(self.email, str(self))
        return self.get_full_name()

    class Meta:
        abstract = True

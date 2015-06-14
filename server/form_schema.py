

from wtforms import (Form,
                     SelectMultipleField,
                     FloatField,
                     IntegerField,
                     validators)


class MultiValueField(SelectMultipleField):

    """ Inherits SelectMultipleField for multiple value
        for a field. This is a lazy way to get multiple value
        implementation in SelectMultipleField so be aware
        that the data sent is free text or whatever it can be.
        Make sure you use validators and correct coerce for
        input data.

    """

    def pre_validate(self, form):
        """ Skip assertion if value is in the predefined list

        """
        pass


class SearchForm(Form):
    lng = FloatField(
        'Longitude', [validators.Required()])
    lat = FloatField(
        'Latitude', [validators.Required()])
    radius = IntegerField('Radius', [validators.Required()])
    count = IntegerField('Limit', default=10)
    tags = MultiValueField('Tags')

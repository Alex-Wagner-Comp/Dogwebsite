from django.forms import ModelForm
from dogwebsite.model import Dog, Appointment

class createDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

class createApptForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
from django import forms

from hut_meal_order.models import OrderDetail


class UserNewOrderForm(forms.Form):
    count = forms.IntegerField(
        widget= forms.NumberInput(attrs={"class":"input-text qty", "id":"qty", "name": "qty", "type": "text", "maxlength":"12", "value": "1"}),
        initial = 1
    )



    class Meta:
        model = OrderDetail
        fields = ['organization', 'product_id', 'count']
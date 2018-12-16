from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productid','productname','productcost','productcolor','productweight']
    productid = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter product id here..'
            }
        )
    )
    productname = forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter product name here..'
            }
        )
    )
    productcost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter product cost here..'
            }
        )
    )
    productcolor = forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter product color here..'
            }
        )
    )
    productweight = forms.IntegerField(
        label='Enter Product Weight',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter product weight here..'
            }
        )
    )

class UpdateForm(forms.Form):
    productid = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter product id here..'
            }
        )
    )
    productcost = forms.IntegerField(
        label='Enter New Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please enter new product cost here..'
            }
        )
    )
class DeleteForm(forms.Form):
    productid = forms.IntegerField()
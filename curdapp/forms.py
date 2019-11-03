from django import forms

class ProductInsertForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Your Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter Your Product color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Your Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )


class ProductUpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
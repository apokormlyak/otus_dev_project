from django import forms
from .models import Warehouse, StorageType, Cargo

# ModelForm, Form



class WarehouseForm(forms.ModelForm):
    name = forms.CharField(
        label='Склад',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Наименование склада',
                'class': 'form-control',
            }
        )
    )

    address = forms.CharField(
        label='Адрес',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Адрес склада',
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Описание склада',
                'class': 'form-control'
            }
        )
    )

    useful_value = forms.CharField(
        label='Площадь',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Полезный объем склада',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Warehouse
        fields = '__all__'


class StorageTypeForm(forms.ModelForm):
    name = forms.CharField(
        label='Тип хранения',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Наименование типа хранения',
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Описание типа хранения',
                'class': 'form-control'
            }
        )
    )

    storage_value = forms.CharField(
        label='Вместимость',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Полезный объем типа хранения',
                'class': 'form-control'
            }
        )
    )

    warehouse = forms.ModelMultipleChoiceField(
        queryset=Warehouse.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            # attrs={
            #     'class': 'form-control'
            # }
        )
    )

    class Meta:
        model = StorageType
        fields = '__all__'


class CargoForm(forms.ModelForm):
    name = forms.CharField(
        label='Груз',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Наименование груза',
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Описание груза',
                'class': 'form-control'
            }
        )
    )

    cargo_value = forms.CharField(
        label='Объем',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Объем груза',
                'class': 'form-control',
            }
        )
    )

    cargo_weight = forms.CharField(
        label='Вес',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Вес груза',
                'class': 'form-control',
            }
        )
    )

    warehouse = forms.ModelMultipleChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple(
            # attrs={
            #     'class': 'form-control'
            # }
        )
    )

    storage_type = forms.ModelMultipleChoiceField(
        queryset=StorageType.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple(
            # attrs={
            #     'class': 'form-control'
            # }
        )
    )

    class Meta:
        model = Cargo
        fields = '__all__'
from django import forms
class SignInForm(forms.Form):
    prenom = forms.CharField(max_length=20, label = "Prénom :")
    nom = forms.CharField(max_length = 20, label = "Nom :")
    pseudo = forms.CharField(max_length = 20, label = "Votre pseudo :")
    mail = forms.EmailField(label = "Votre adresse mail :")
    datenaissance = forms.DateField(label = "Date de naissance :", input_formats = ['%d-%m-%Y'])
    nl = forms.BooleanField(label = "", help_text="Souhaitez-vous recevoir régulièrement notre Newsletter ?", required=False)
    

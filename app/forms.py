from django import forms
c=[('PYTHON','PYTHON'),('JAVA','JAVA'),('MERN','MERN'),['SQL','SQL']]
g=[('MALE','MALE'),('FEMALE','FEMALE'),['OTHERS','OTHERS']]
b=[('CSE','CSE'),('MECH','MECH'),['CIVIL','CIVIL'],['EEE','EEE'],['ECE','ECE']]
class Studentdetails(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    dob=forms.DateField()
    email=forms.EmailField()
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    branch=forms.ChoiceField(choices=b)
    #course=forms.MultipleChoiceField(choices=c)  
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)  
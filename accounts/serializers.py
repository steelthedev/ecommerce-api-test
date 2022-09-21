from rest_framework import serializers
from .models import Profile



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username','password','first_name','last_name','email','country','phone']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def save(self):
        account = Profile(
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            country = self.validated_data['country'],
            phone=self.validated_data['phone']
        )

        password = self.validated_data['password']
        
        if not password:
            raise serializers.ValidationError({'password':"passwords must match"})

        account.set_password(password)
       
        account.save()
        return account



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name','last_name','email','is_admin','username','country','phone')
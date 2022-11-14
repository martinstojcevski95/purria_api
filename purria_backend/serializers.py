from rest_framework import serializers
from purria_backend.models import Contract,Garden

        

class GardenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Garden
        fields = ['id','name']
        
        
class ContractSerializer(serializers.ModelSerializer):
    
    id = serializers.CharField(read_only=True)
    garden = serializers.SerializerMethodField('garden_extra_info')
    user = serializers.CharField(read_only=True)
 
    class Meta:
        model = Contract
        fields = ['id','name', 'description','level','garden','user']
        read_only_fields = ['garden']
  

    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            current_user_email = self.context['request'].user.email
            check_contract_user = Contract.objects.filter(user__email=current_user_email).filter(name=attrs['name']).exists()
            if check_contract_user:
                raise serializers.ValidationError(f"contract with name {attrs['name']} already exists in user {current_user_email}")
            return attrs
        return super().validate(attrs)

    
    def garden_extra_info(self,obj):
        return obj.garden.all().values('name','garden','id')
    

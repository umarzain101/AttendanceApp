from rest_framework import serializers
from .models import user,attendance,geolog

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        # fields = ['id','name','father_name','cnic','designation','district','mobile','imei','joining_date','date']
        fields = '__all__'

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ['id','user_id','cnic','imei','date','lat','long','type','date1']
class geologSerializer(serializers.ModelSerializer):
    class Meta:
        model = geolog
        # fields = ['id','user_id','cnic','imei','lat','long','date','date1']
        fields = '__all__'




# class userSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=60)
#     father_name = serializers.CharField(max_length=60)
#     cnic = serializers.IntegerField()
#     designation = serializers.CharField(max_length=60)
#     district = serializers.CharField(max_length=60)
#     mobile = serializers.IntegerField()
#     imei = serializers.IntegerField()
#     # date = serializers.DateTimeField(auto_now_add=True)

#     def create (self, validated_data):
#         return user.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.father_name = validated_data.get('father_name',instance.father_name)
#         instance.cnic = validated_data.get('cnic',instance.cnic)
#         instance.designation = validated_data.get('designation',instance.designation)
#         instance.district = validated_data.get('district',instance.district)
#         instance.mobile = validated_data.get('mobile',instance.mobile)
#         instance.imei = validated_data.get('imei',instance.imei)
#         instance.save()
#         # instance.date = validated_data.get('date',instance.date)
#         return instance

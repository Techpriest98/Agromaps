# from rest_framework import serializers
# from .models import Field, Culture, SeedProcess

# class FieldSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Field
# 		#fields = ('title', 'square', 'cultureID')
# 		fields = '__all__'
# 		read_only_fields = ['pk','title','cultureID','process']

# class  CultureSerializer(serializers.ModelSerializer):

# 	class Meta:		
# 		model = Culture
# 		fields = '__all__'
# 		read_only_fields = ['pk', 'name', 'color']
	
			
# class SeedSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = SeedProcess
#         fields = '__all__'
#         read_only_fields = ['pk', 'harvestDate', 'field', 'culture']        	

# 						
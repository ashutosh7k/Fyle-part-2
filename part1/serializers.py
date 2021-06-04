from rest_framework import serializers
from part1 import models


class BankBranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankBranches
        fields = ['ifsc', 'bank_id', 'branch',
                  'address', 'city', 'district', 'state']

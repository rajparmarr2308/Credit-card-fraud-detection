import pickle
from django.db import models
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Create your models here.
class DataFileUpload(models.Model):
    file_name = models.CharField(max_length=50)
    actual_file = models.FileField(upload_to ='uploads/')
    description = models.CharField(max_length=400,null=True,blank=True)
    trained_model_data = models.BinaryField()
    x_test_data = models.BinaryField(null=True, blank=True)  # Serialized X_test data
    y_test_data = models.BinaryField(null=True, blank=True)  # Serialized y_test data


    
    def __str__(self):
        return self.file_name
    
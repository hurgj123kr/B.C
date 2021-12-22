import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "gbm_model.pkl")
    model = joblib.load(MODEL_FILE)
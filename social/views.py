from django.shortcuts import render
from django.conf import settings
import pickle
from social.models import PredictionPauvrete
from django.core.paginator import Paginator

def predict_model(request):
    if request.method == 'POST':
        data = request.POST
        features = []
        for key in data.keys():
            try:
                value = float(data.get(key, 1))  # Convertir les valeurs en float
            except ValueError:
                value = 1.0  # Remplacer par une valeur par défaut si la conversion échoue
            features.append(value)
        
        # Chargement du modèle
        modele_path = settings.BASE_DIR / 'datas' / 'model.pkl'
        with open(modele_path, "rb") as f:
            modele = pickle.load(f)
        
        # Effectuer la prédiction avec votre modèle de machine learning
        prediction = modele.predict([features])  # Obtenir la première prédiction

        # Enregistrement de la prédiction dans la base de données
        prediction_obj = PredictionPauvrete(result=prediction)
        prediction_obj.save()

        # Récupérer toutes les prédictions enregistrées
        results = PredictionPauvrete.objects.all().order_by('created_at')
        context = {"results":results}
        # Retourner les résultats dans le même template
        return render(request, 'social/home.html', context)
    else:
        # Gérer les autres méthodes HTTP si nécessaire
        return render(request, 'social/home.html')

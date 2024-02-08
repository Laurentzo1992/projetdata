from django.shortcuts import render
import joblib
from django.http import HttpResponse, JsonResponse
import json
from django.conf import settings
import pickle
modele = settings.BASE_DIR / 'datas' / 'model.pkl'



def home(request):
    return render(request, 'social/home.html')



def predict_model(request):
    if request.method == 'POST':
        # Récupérez les données JSON envoyées dans le corps de la requête
        data = json.loads(request.body)
        
        MenPPStructSanteFK = data.get('MenPPStructSanteFK')
        MenPPdistStructSanteFK = data.get('MenPPdistStructSanteFK')
        MenPPEcolePrimFK = data.get('MenPPEcolePrimFK')
        MenPPCollegeFK = data.get('MenPPCollegeFK')
        MenPPdistEcolePrimFK = data.get('MenPPdistEcolePrimFK')
        MenPPdistCollegeFK = data.get('MenPPdistCollegeFK')
        MenPSAEBFK = data.get('MenPSAEBFK')
        MenPPSouceEauFK = data.get('MenPPSouceEauFK')
        MenPPdistSourceEauFK = data.get('MenPPdistSourceEauFK')
        MenPossGrpEl = data.get('MenPossGrpEl')
        MenSEEclFK = data.get('MenSEEclFK')
        MenSECuisFK = data.get('MenSECuisFK')
        MenPossSalon = data.get('MenPossSalon')
        MenPossLitMat = data.get('MenPossLitMat')
        MenPossRefr = data.get('MenPossRefr')
        MenPossClim = data.get('MenPossClim')
        MenPossVent = data.get('MenPossVent')
        MenPossMatelas = data.get('MenPossMatelas')
        MenPossAutreMeubl = data.get('MenPossAutreMeubl')
        MenPossFer = data.get('MenPossFer')
        MenPossTelv = data.get('MenPossTelv')
        MenPossCB = data.get('MenPossCB')
        MenPossCuisMdrn = data.get('MenPossCuisMdrn')
        MenPossTelFix = data.get('MenPossTelFix')
        MenPossTelPort = data.get('MenPossTelPort')
        MenPossChauffEau = data.get('MenPossChauffEau')
        MenPossMachLav = data.get('MenPossMachLav')
        MenTypToiletFK = data.get('MenTypToiletFK')
        MenNbrMembr = data.get('MenNbrMembr')
        MenLogStatFK = data.get('MenLogStatFK')
        MenNbrPiecesLog = data.get('MenNbrPiecesLog')
        MenPossLogmtFK = data.get('MenPossLogmtFK')
        MenTypLogeFK = data.get('MenTypLogeFK')
        MenMatToitLogeFK = data.get('MenMatToitLogeFK')
        MenMatMurLogeFK = data.get('MenMatMurLogeFK')
        MenNatSolLogeFK = data.get('MenNatSolLogeFK')
        MenPossPrg = data.get('MenPossPrg')
        MenPossCharet = data.get('MenPossCharet')
        MenPossBrt = data.get('MenPossBrt')
        MenPossAntenne = data.get('MenPossAntenne')
        MenPossRadio = data.get('MenPossRadio')
        MenPossVoiture = data.get('MenPossVoiture')
        MenPossOrd = data.get('MenPossOrd')
        MenPossInternet = data.get('MenPossInternet')
        MenPossMoto = data.get('MenPossMoto')
        MenPPTransportFK = data.get('MenPPTransportFK')
        MenPPTeleServicesFK = data.get('MenPPTeleServicesFK')
        MenPPdistTransportFK = data.get('MenPPdistTransportFK')
        MenPPdistTeleServicesFK = data.get('MenPPdistTeleServicesFK')
        nbrBovinCamelins = data.get('nbrBovinCamelins')
        ancienEtatBC = data.get('ancienEtatBC')
        nbrMoutonsChevres = data.get('nbrMoutonsChevres')
        ancienEtatMC = data.get('ancienEtatMC')
        nbrAnsChevaux = data.get('nbrAnsChevaux')
        ancienEtatAC = data.get('ancienEtatAC')
        nbrVolailles = data.get('nbrVolailles')
        ancienEtatVolailles = data.get('ancienEtatVolailles')
        MenTerHabit = data.get('MenTerHabit')
        MenTerAgr = data.get('MenTerAgr')
        etSupT = data.get('etSupT')
        autT = data.get('autT')
        etSupAutT = data.get('etSupAutT')
        
        # Recupérer les features
        features = []
        # Effectuez vos opérations, par exemple, faire une prédiction avec votre modèle de machine learning
        prediction = modele.predict([features])
        # Retournez les résultats sous forme de réponse JSON
        return JsonResponse({'prediction': 'prediction'})
    else:
        # Gérez les autres méthodes HTTP si nécessaire
        return JsonResponse({'error': 'Méthode HTTP non autorisée'}, status=405)


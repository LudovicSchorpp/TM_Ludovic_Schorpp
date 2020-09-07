# Tentative de modélisation hydrogéologique de la plaine du Roussillon
Modélisation hydrogéologique de la plaine du Roussillon avec Modflow à l'aide de l'interface Python FloPy.

Le répertoire est classé en différents dossiers détaillés ci-dessous :
  - Chabart : dossier à part contenant les notebooks, données de travail sur la reconstruction du modèle de Chabart (1996) de la plaine du Roussillon
  - data : contient la quasi totalité des données utilisées dans ce travail (données piézométriques, cartes piézométriques, position des conditions limites, carte de transmissivité, MNT et surfaces , etc.
  - exe et exe_l : contient les executables de la suite MODFLOW pour windows et linux resp.
  - Model_val : dossier provisoire pour travailler sur l'import de simulations géostatistiques (MPS) pour la distribution des faciès dans l'aquifère
  - Modeles2D  : notebooks contenant les différents modèles en 2 dimensions (permanent, transitoire et raffiné), le véritable modèle en permanent (décrit dans le master) est regroupé sous le nom de "test_premier_model"
  - Modeles3D : notebooks contenant les différents modèles permanents en 3 dimensions
  - modules : les modules pythons créés et utilisés dans ce travail
  - PEST++inv : dossier à part sur les inversions et calibrations à l'aide de PEST++, chaque dossier contient une inversion spécifique, détaillée dans le master.
  - pred_clim : dossier spécifique sur les prédictions climatiques avec 2 sous-dossiers, un pour chaque modèle utilisé.
  - traitement_data : multiples sous-dossiers et notebooks sur le traitement des données et la création de figures pour le master

**Pour une bonne utilisation des notebooks il est nécessaire de posséder la version 3.3.0 de Flopy (pas supérieure).**

Pour toute question relative au dossier, données ou au travail en général vous pouvez me contacter par [email](mailto:ludovic.schorpp@unine.ch)

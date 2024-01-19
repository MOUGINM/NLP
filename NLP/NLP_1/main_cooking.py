from fonction_clear import *
import pandas as pd
from pprint import pprint

# Charger votre DataFrame à partir de votre source de données
df = pd.read_csv('cooking.csv')  # Assurez-vous de remplacer le chemin avec le vôtre

clean_text = []

for text in df['Unnamed: 1'],['Unnamed: 2']:
    clean_text.append(text)

no_number_clean_text = [removing_number(text) for text in clean_text]
no_punc_clean_text = [remove_punctuaction(text, punct_list) for text in no_number_clean_text]
no_url_clean_text = [remove_urls(text) for text in no_punc_clean_text]
no_maj_clean_text = [textlower(text) for text in no_url_clean_text]
no_stopwords_clean_text = [remove_stopwords(text) for text in no_maj_clean_text]
all_clear = no_stopwords_clean_text
# print(all_clear)

#############################################################################################################

# Charger le fichier CSV
chemin_fichier_csv = 'cooking.csv'
df = pd.read_csv(chemin_fichier_csv)

#Appliquer la détection d'ingrédients et de techniques sur chaque cellule du fichier
for index, row in df.iterrows():
    texte_cel = str(row['Unnamed: 1'])  
    good_liste_ingredients = list(set(detecter_ingredients(texte_cel)))
    good_liste_techniques = list(set(detecter_techniques(texte_cel)))

    data_dict_1 = {
        'ingredient': good_liste_ingredients,
        'techniques': good_liste_techniques
    }

print('Unnamed: 1')
pprint(data_dict_1)

for index, row in df.iterrows():
    texte_cel = str(row['Unnamed: 2'])  
    good_liste_ingredients = list(set(detecter_ingredients(texte_cel)))
    good_liste_techniques = list(set(detecter_techniques(texte_cel)))

    data_dict_2 = {
        'ingredient': good_liste_ingredients,
        'techniques': good_liste_techniques
    }

print('Unnamed: 2')
pprint(data_dict_2)


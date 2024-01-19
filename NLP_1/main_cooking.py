from fonction_clear import *
import pandas as pd
from collections import Counter
from pprint import pprint

# Chargement des données depuis le fichier CSV
df = pd.read_csv('cooking.csv')

# Renommage des colonnes pour une meilleure compréhension
df.rename(columns={'Unnamed: 1': 'colonne1', 'Unnamed: 2': 'colonne2'}, inplace=True)

# Fonction pour appliquer une fonction de nettoyage de manière sécurisée
def safe_apply(func, text):
    return func(text) if isinstance(text, str) else text

# Appliquer les fonctions de nettoyage à une colonne spécifique
def apply_cleaning_functions(df, column):
    df[column] = df[column].apply(lambda x: safe_apply(removing_number, x))
    df[column] = df[column].apply(lambda x: safe_apply(lambda y: remove_punctuaction(y, punct_list), x))
    df[column] = df[column].apply(lambda x: safe_apply(remove_urls, x))
    df[column] = df[column].apply(lambda x: safe_apply(textlower, x))
    df[column] = df[column].apply(lambda x: safe_apply(remove_stopwords, x))
    df[column] = df[column].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
    return df

# Application du nettoyage aux deux colonnes sélectionnées
df = apply_cleaning_functions(df, 'colonne1')
df = apply_cleaning_functions(df, 'colonne2')

# Fonction pour extraire et compter les ingrédients et techniques
def extract_and_count(df, column):
    ingredients_count = Counter()
    techniques_count = Counter()

    for text in df[column]:
        if isinstance(text, str):
            ingredients_count.update(detecter_ingredients(text))
            techniques_count.update(detecter_techniques(text))

    return ingredients_count, techniques_count

# Extraction et comptage des ingrédients et techniques pour chaque colonne
ingredients_col1, techniques_col1 = extract_and_count(df, 'colonne1')
ingredients_col2, techniques_col2 = extract_and_count(df, 'colonne2')

# Conversion des compteurs en DataFrames pour une meilleure visualisation
def counter_to_dataframe(counter, column_name):
    return pd.DataFrame(counter.items(), columns=[column_name, 'Frequency']).sort_values(by='Frequency', ascending=False)

df_ingredients_col1 = counter_to_dataframe(ingredients_col1, 'Ingredient')
df_techniques_col1 = counter_to_dataframe(techniques_col1, 'Technique')
df_ingredients_col2 = counter_to_dataframe(ingredients_col2, 'Ingredient')
df_techniques_col2 = counter_to_dataframe(techniques_col2, 'Technique')

# Création d'un fichier Excel pour stocker les résultats
writer = pd.ExcelWriter('cooking_analysis.xlsx', engine='xlsxwriter')

# Écriture des résultats dans des feuilles séparées du fichier Excel
df_ingredients_col1.to_excel(writer, sheet_name='Ingredients Col1', index=False)
df_techniques_col1.to_excel(writer, sheet_name='Techniques Col1', index=False)
df_ingredients_col2.to_excel(writer, sheet_name='Ingredients Col2', index=False)
df_techniques_col2.to_excel(writer, sheet_name='Techniques Col2', index=False)

# Fermeture et sauvegarde du fichier Excel
writer.close()

# Affichage des résultats dans la console
print('Colonne 1:')
pprint({'Ingrédients': ingredients_col1, 'Techniques': techniques_col1})
print('\nColonne 2:')
pprint({'Ingrédients': ingredients_col2, 'Techniques': techniques_col2})

# Test des fonctions de détection avec un texte exemple
test_text = "Recette avec des tomatoes, du basil, et méthode de baking."
print(detecter_ingredients(test_text))  # Devrait retourner ['tomatoes', 'basil']
print(detecter_techniques(test_text))   # Devrait retourner ['baking']

# Inspection des premières lignes des données nettoyées
print('Données nettoyées - Colonne 1 :')
print(df['colonne1'].head())
print('\nDonnées nettoyées - Colonne 2 :')
print(df['colonne2'].head())

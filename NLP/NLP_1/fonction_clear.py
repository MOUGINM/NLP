import re
import string
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd



punct_list = ["!", "'", '"', "#", "$", "%", "&", "(", ")", "*","§", "+","£", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`"]

def remove_punctuaction(text, punct_list):
    for punc in punct_list:
        if punc in text:
            text = text.replace(punc,'')
    return text

def textlower(text):
    return text.lower()

# def removing_number(text):
#     result = re.sub(r"\d+","", text)
#     return result
import re

def removing_number(text):
    if isinstance(text, (int, float)):
        return ""
    result = re.sub(r"\d+","", str(text))
    return result


def handling_double_whitespace(text):
    return "".join(text.split())


#define a regex pattern to match URLs
url_pattern = re.compile(r'https?://\S+|www\.\S+')
def remove_urls(text):
    return url_pattern.sub('',text) # we replace URL with space


#enlever des mots, garder l'essentiel
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return filtered_text

# example_text ="Une simple phrase pour apprendre à faire des cookie en francais"
# print('Before removing stopwords', example_text)
# print('After removing stopwords', remove_stopwords(example_text))


#stemming
# stem words in the list of tokenized words
stemmer = PorterStemmer()
def stem_words(text):
    word_tokens = word_tokenize(text)
    stems = [ stemmer.stem(word) for word in word_tokens]
    return stems

# text = ' data science uses scientific methods algorithmes and many type of processes'
# stem_words(text)




#stopwords english
# import nltk
# from nltk.corpus import stopwords
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))

# print(stop_words)

# stop_words.add('TEST')
# print(stop_words)

def detecter_ingredients(texte):
    motif_ingredients = re.compile(r'\b(?:lettuce|broccoli|asparagus|peas|quinoa|almond butter|cashews|coconut milk|grapefruit|kiwi|blueberries|cranberries|avocado|soy sauce|tofu|seitan|quinoa|chickpeas|lentils|pomegranate|figs|kiwi|guava|turkey bacon|chorizo|prosciutto|pancetta|trout|lobster|mango|papaya|passion fruit|nectarine|radish|jalapeno|wasabi|edamame|salt|pepper|sugar|flour|eggs|oil|vinegar|garlic|onion|milk|butter|cream|cheese|tomato|bell pepper|eggplant|zucchini|carrot|potato|spinach|mushrooms|lemon|chicken|beef|pork|lamb|salmon|tuna|shrimp|mustard|ketchup|mayonnaise|honey|rice|pasta|bread|thyme|rosemary|oregano|basil|mint|parsley|coriander|cinnamon|ginger|nutmeg|vanilla|cocoa|powdered sugar|yeast|baking soda|almonds|walnuts|hazelnuts|raisins|dried apricots|dried figs|chocolate|cinnamon|cloves|star anise|paprika|turmeric|cumin|curry|sea salt|black pepper|white pepper|cayenne pepper|meat|chicken|beef|pork|lamb|veal|sausage|bacon|ham|turkey|duck)\b', re.IGNORECASE)
    ingredients = motif_ingredients.findall(texte)
    return ingredients

def detecter_techniques(texte):
    motif_techniques = re.compile(r'\b(?:saute|stirfry|smoke|poach|griddle|barbecue|steam|deepfry|braise|bake|roast|grill|boil|panroast|sousvide|broil|sear|simmer|blanch|marinate|panfry|stew|glaze|caramelize|poele|flambe|steamcook|smother|braiser|smoke|steamroast|cook|bake|fry|grill|remove|boil|mix|steamcook|roast|sear|braise|pan-fry|stew|blanch|flame|prepare in parchment|bread|brown|crush|chop|mince|slice|julienne|grate|knead|beat|whip|incorporate|sift|reduce|sweat|plate|fillet|reduce|deglaze|sprinkle|emulsify|poach|confit)\b', re.IGNORECASE)
    techniques = motif_techniques.findall(texte)
    return techniques
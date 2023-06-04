#spell checking algorithm 
#code submitted by devansh verma 
from spellchecker import SpellChecker
spell = SpellChecker()

def spell_check(text):
    tokens = text.split()
    
    # Create a dictionary to store misspelled tokens and their corrections
    corrections = {}
    
    for token in tokens:
        if not spell.correction(token) == token:
            # Find the most likely correct spelling
            corrected_token = spell.correction(token)
            
            # Add the misspelled token and its correction to the dictionary
            corrections[token] = corrected_token
    
    return corrections

# Example testcase 
input_text = "helo"


corrections = spell_check(input_text)

# Print the misspelled tokens and their corrections
for misspelled, corrected in corrections.items():
    print(f"Misspelled: {misspelled}, Corrected: {corrected}")

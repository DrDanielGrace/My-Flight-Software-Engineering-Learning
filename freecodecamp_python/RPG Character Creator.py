# RPG Character Creator
# Creates a text-based character sheet with visual stat bars
# Each stat is displayed as a row of filled and empty dots

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # 1. Name Validations
    if not isinstance(name, str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    # 2. Type Validation for Stats
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"
    
    # 3. Value Range Validations
    if min(strength, intelligence, charisma) < 1:
        return "All stats should be no less than 1"
    if max(strength, intelligence, charisma) > 4:
        return "All stats should be no more than 4"
        
    # 4. Total Points Validation
    if sum([strength, intelligence, charisma]) != 7:
        return "The character should start with 7 points"

    # Generates the dot bars with a total length of 3

    # Multiple "full_dot" by starting value, then multiple "empty_dot" by the remaining space after running calculations of the remaining value
    # Concatinate them together with +

    strength_bar = (full_dot * strength) + (empty_dot * (10 - strength))
    intelligence_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    charisma_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))

    # Return the final formatted value
    return f"{name}\nSTR {strength_bar}\nINT {intelligence_bar}\nCHA {charisma_bar}"

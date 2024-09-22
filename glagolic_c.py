# Mapping of Latin letters to Glagolitic letters
latin_to_glagolitic = {
    'a': 'Ⰰ', 'b': 'Ⰱ', 'v': 'Ⰲ', 'g': 'Ⰳ', 'd': 'Ⰴ', 'e': 'Ⰵ', 'zh': 'Ⰶ',
    'z': 'Ⰷ', 'i': 'Ⰻ', 'j': 'Ⰼ', 'k': 'Ⰽ', 'l': 'Ⰾ', 'm': 'Ⰿ', 'n': 'Ⱀ',
    'o': 'Ⱁ', 'p': 'Ⱂ', 'r': 'Ⱃ', 's': 'Ⱄ', 't': 'Ⱅ', 'u': 'Ⱆ', 'f': 'Ⱇ',
    'h': 'Ⱈ', 'ch': 'Ⱍ', 'sh': 'Ⱎ', 'sch': 'Ⱋ', 'ts': 'Ⱌ', 'y': 'Ⱓ'
}

# Reverse mapping from Glagolitic to Latin
glagolitic_to_latin = {v: k for k, v in latin_to_glagolitic.items()}

# Mapping of Slovenian letters to Glagolitic letters
slovenian_to_glagolitic = {
    'a': 'Ⰰ', 'b': 'Ⰱ', 'c': 'Ⱌ', 'č': 'Ⱍ', 'd': 'Ⰴ', 'e': 'Ⰵ', 'f': 'Ⱇ', 'g': 'Ⰳ',
    'h': 'Ⱈ', 'i': 'Ⰻ', 'j': 'Ⰼ', 'k': 'Ⰽ', 'l': 'Ⰾ', 'm': 'Ⰿ', 'n': 'Ⱀ', 'o': 'Ⱁ',
    'p': 'Ⱂ', 'r': 'Ⱃ', 's': 'Ⱄ', 'š': 'Ⱎ', 't': 'Ⱅ', 'u': 'Ⱆ', 'v': 'Ⰲ', 'z': 'Ⰷ', 'ž': 'Ⰶ'
}

# Reverse mapping from Glagolitic to Slovenian
glagolitic_to_slovenian = {v: k for k, v in slovenian_to_glagolitic.items()}

# Function to map text between Glagolitic and Latin/Slovenian with two-way conversion
def text_converter(text, mode='slovenian', direction='to_glagolitic'):
    result = []
    
    # Select the appropriate mapping based on the mode and direction
    if direction == 'to_glagolitic':
        if mode == 'latin':
            mapping = latin_to_glagolitic
        elif mode == 'slovenian':
            mapping = slovenian_to_glagolitic
        else:
            raise ValueError("Invalid mode. Please choose either 'latin' or 'slovenian'.")
        
        i = 0
        while i < len(text):
            char = text[i].lower()

            # For multi-character combinations in Latin mode ('zh', 'ch', etc.)
            if mode == 'latin' and i + 1 < len(text):
                two_char_combination = text[i:i+2].lower()
                three_char_combination = text[i:i+3].lower()
                if three_char_combination in mapping:
                    glagolitic_char = mapping[three_char_combination]
                    if text[i].isupper():  # Preserve case
                        result.append(glagolitic_char.upper())
                    else:
                        result.append(glagolitic_char)
                    i += 3
                    continue
                elif two_char_combination in mapping:
                    glagolitic_char = mapping[two_char_combination]
                    if text[i].isupper():
                        result.append(glagolitic_char.upper())
                    else:
                        result.append(glagolitic_char)
                    i += 2
                    continue

            # Single character conversion
            if char in mapping:
                glagolitic_char = mapping[char]
                if text[i].isupper():  # Preserve case
                    result.append(glagolitic_char.upper())
                else:
                    result.append(glagolitic_char)
            else:
                result.append(text[i])  # Leave it as is if not found in the mapping
            
            i += 1
    
    elif direction == 'from_glagolitic':
        if mode == 'latin':
            reverse_mapping = glagolitic_to_latin
        elif mode == 'slovenian':
            reverse_mapping = glagolitic_to_slovenian
        else:
            raise ValueError("Invalid mode. Please choose either 'latin' or 'slovenian'.")
        
        for char in text:
            # Check if the character exists in the reverse mapping
            if char.lower() in reverse_mapping:
                latin_char = reverse_mapping[char.lower()]
                if char.isupper():
                    result.append(latin_char.upper())
                else:
                    result.append(latin_char)
            else:
                result.append(char)  # Leave as is if not found in the reverse mapping

    else:
        raise ValueError("Invalid direction. Please choose either 'to_glagolitic' or 'from_glagolitic'.")
    
    return ''.join(result)

# Test the function with both modes and directions
slovenian_string = "Slava Sloveniji"
latin_string = "glory to the glagolic script"
glagolitic_string = "ⰔⰎⰀⰂⰀ ⰔⰎⰑⰐⰅⰐⰋⰖ"

# Slovenian to Glagolitic
print("Slovenian to Glagolitic:")
glagolitic_string_slovenian = text_converter(slovenian_string, mode='slovenian', direction='to_glagolitic')
print(f"Slovenian: {slovenian_string}")
print(f"Glagolitic: {glagolitic_string_slovenian}")

# Glagolitic to Slovenian
print("\nGlagolitic to Slovenian:")
slovenian_from_glagolitic = text_converter(glagolitic_string, mode='slovenian', direction='from_glagolitic')
print(f"Glagolitic: {glagolitic_string}")
print(f"Slovenian: {slovenian_from_glagolitic}")

# Latin to Glagolitic
print("\nLatin to Glagolitic:")
glagolitic_string_latin = text_converter(latin_string, mode='latin', direction='to_glagolitic')
print(f"Latin: {latin_string}")
print(f"Glagolitic: {glagolitic_string_latin}")

# Glagolitic to Latin
print("\nGlagolitic to Latin:")
latin_from_glagolitic = text_converter(glagolitic_string, mode='latin', direction='from_glagolitic')
print(f"Glagolitic: {glagolitic_string}")
print(f"Latin: {latin_from_glagolitic}")


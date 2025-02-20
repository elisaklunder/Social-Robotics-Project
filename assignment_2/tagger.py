import re
import pyphen

dic = pyphen.Pyphen(lang='en')

def count_syllables(word):
    """
    Count syllables in a word using pyphen's hyphenation. The number of syllables is the number of hyphenated parts.
    """
    word_clean = re.sub(r'[^\w]', '', word.lower())
    if not word_clean:
        return 0
    hyphenated = dic.inserted(word_clean)
    return len(hyphenated.split('-'))

def process_tagged_text(text):
    """
    Processes the text containing tags and returns:
    
    Returns:
        list[dict]: A list of dictionaries, each containing:
                        - "tag": the tag name
                        - "content": the text enclosed in the tag
                        - "syllable_position": the syllable count
        
        str: The cleaned up text (i.e., with tags removed)
    """
    tag_positions = [] 
    cleaned_text = ""   
    syllable_count = 1 
    
    pattern = re.compile(r'<(\w+)>(.*?)</\1>')  # match <tag>word</tag>
    
    pos = 0 
    for match in pattern.finditer(text):
        start, end = match.span()
        tag_type = match.group(1)
        tag_content = match.group(2)
        
        before = text[pos:start]
        cleaned_text += before

        for word in re.findall(r'\b\w+\b', before):
            syllable_count += count_syllables(word)
        
        tag_positions.append({
            "tag": tag_type,
            "content": tag_content,
            "syllable_position": syllable_count
        })
        
        cleaned_text += tag_content

        for word in re.findall(r'\b\w+\b', tag_content):
            syllable_count += count_syllables(word)
        
        pos = end

    after = text[pos:]
    cleaned_text += after
    for word in re.findall(r'\b\w+\b', after):
        syllable_count += count_syllables(word)
    
    return tag_positions, cleaned_text

if __name__ == "__main__":
    sample_text = " \
    You are a friendly robot that interacts with people. \
    The rules of the game are: \
    - the players take turns in having the roles of either the guesser or the word keeper \
    - the word keeper thinks of a word, and then signals that they are ready to answer questions \
    - the guesser is only allowed to ask yes or no questions or make a guess at the word \
    - hints can be given by the word keeper when the other player seems to be stuck"
    
    syllable_count = 0
    
    for word in re.findall(r'\b\w+\b', sample_text):
        syllable_count += count_syllables(word)
        
    print("Total syllables:", syllable_count)


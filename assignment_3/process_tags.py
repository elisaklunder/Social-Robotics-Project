import re

import pyphen

dic = pyphen.Pyphen(lang="en")

def calculate_text_syllables(text: str) -> int:
    syllable_count = 1
    for word in re.findall(r"\b\w+\b", text):
            syllable_count += count_syllables(word)

    return syllable_count

def count_syllables(word: str) -> int:
    """
    Count syllables in a word using pyphen's hyphenation. The number of syllables is the number of hyphenated parts.
    
    Args:
        word (str): The word to count syllables in
    
    Returns:    
        int: The number of syllables in the word
    """
    word_clean = re.sub(r"[^\w]", "", word.lower())
    if not word_clean:
        return 0
    hyphenated = dic.inserted(word_clean)
    return len(hyphenated.split("-"))


def process_tagged_text(text: str) -> tuple[list[dict], str]:
    """
    Processes the text containing tags and returns:
    
    Args:
        text (str): The text containing tags

    Returns:
        list[dict]: A list of dictionaries, each containing:
                        - "tag": the tag name
                        - "content": the text enclosed in the tag
                        - "start_position": the syllable count at the start of the tag

        str: The cleaned up text (i.e., with tags removed)
    """
    tag_positions = []
    cleaned_text = ""
    syllable_count = 1

    pattern = re.compile(
        r"<(\w+)>(.*?)</\1>", re.DOTALL
    )  # match <tag>multiple words</tag>

    pos = 0
    for match in pattern.finditer(text):
        start, end = match.span()
        tag_type = match.group(1)
        tag_content = match.group(2)

        before = text[pos:start]
        cleaned_text += before

        # calculating the start position
        for word in re.findall(r"\b\w+\b", before):
            syllable_count += count_syllables(word)

        # calculating the end position 
        end_position = syllable_count
        for word in re.findall(r"\b\w+\b", tag_content):
            end_position += count_syllables(word)

        tag_positions.append(
            {"tag": tag_type, "content": tag_content, "start_position": syllable_count, "end_position": end_position}
        )

        cleaned_text += tag_content

        for word in re.findall(r"\b\w+\b", tag_content):
            syllable_count += count_syllables(word)

        pos = end

    after = text[pos:]
    cleaned_text += after
    for word in re.findall(r"\b\w+\b", after):
        syllable_count += count_syllables(word)

    return tag_positions, cleaned_text


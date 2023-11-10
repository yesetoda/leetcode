class Solution:
    def detectCapitalUse( word: str) -> bool:
        if word==word.upper() or word==word.lower() or (word[0].isupper() and word[1:]==word[1:].lower()):
            return True
        return False
    word = "USA"
    print(detectCapitalUse(word))
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Define the Morse code table
        morseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # Define a dictionary to map Morse code to letters
        conv = {}

        # Fill the dictionary with mappings
        for i in range(26):
            conv[morseTable[i]] = chr(i + 97)

        # Initialize a set to store unique transformations
        uniqueTransformations = set()

        # Iterate through each word
        for word in words:
            # Initialize an empty string to store the transformed word
            transformedWord = ""

            # Iterate through each letter in the word
            for letter in word:
                # Map the letter to its Morse code representation
                morseCode = morseTable[ord(letter) - ord('a')]

                # Concatenate the Morse code to the transformed word
                transformedWord += morseCode

            # Add the transformed word to the set of unique transformations
            uniqueTransformations.add(transformedWord)

        # Return the size of the set of unique transformations
        return len(uniqueTransformations)
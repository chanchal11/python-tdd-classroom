class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        input_str = str(input_str)
        return_str = str()
        for i in range(len(input_str)-1,-1,-1):
            return_str = return_str + input_str[i]
        return return_str

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        switcher = {
            'A': True,
            'E': True,
            'I': True,
            'O': True,
            'U': True,
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True
        }
        return switcher.get(character,False)

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words = sentence.split(' ')
        longest_word = { 'pos': -1, 'size': 0 }
        for i in range(0,len(words)):
            if len(words[i]) > longest_word.get('size'):
                longest_word.__setitem__('size',len(words[i]))
                longest_word.__setitem__('pos',i)

        return words[longest_word.get('pos')]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text = str(text)
        words = text.split(' ')
        lengths = []
        for i in range(0,len(words)):
            lengths.append(len(words[i]))
        return lengths

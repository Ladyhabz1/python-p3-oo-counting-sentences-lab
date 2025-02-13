#!/usr/bin/env python3

import re  # Import regex for advanced splitting

class MyString:
    def __init__(self, value=""):
        # Ensure value is a string
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # ✅ Print instead of raising an error

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # ✅ Print instead of raising an error

    def is_sentence(self):
        """Returns True if value ends with a period (.)"""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if value ends with a question mark (?)"""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark (!)"""
        return self.value.endswith("!")

    def count_sentences(self):
        """Counts the number of sentences in value"""
        sentences = re.split(r'[.!?]+', self.value)  # Split on multiple punctuation
        sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings
        return len(sentences)

# ✅ Testing the class
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  # Output: 3

print(string.is_sentence())      # False (does not end with '.')
print(string.is_question())      # True (ends with '?')
print(string.is_exclamation())   # False (does not end with '!')

# ✅ Test non-string value assignment
string.value = 123  # Should print "The value must be a string."

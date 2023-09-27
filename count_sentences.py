#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        if isinstance(value, str):
            self.value=value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        return False
    
    def is_question(self):
        if self.value.endswith("?"):
            return True
        return False
    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        return False
    
    def count_sentences(self):
      # Split the self.value into sentences using ".", "!", or "?"
      sentences = self.value.split('.') + self.value.split('!') + self.value.split('?')
      print("my sente", sentences)
      # Filter out empty strings and whitespace-only strings
      sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
      print("my sente", len(sentence)
      return len(sentences)

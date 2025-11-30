import json
import os

class Translator:
    def __init__(self, source, target):
        self.source = source.lower().strip()
        self.target = target.lower().strip()
        self.data = {}
        self.filename = self.get_filename()
        self.load_dictionary()

    def get_filename(self):
        mapping = {
            ('georgian', 'english'): 'Georgian-English.json',
            ('english', 'georgian'): 'English-Georgian.json'
        }
        return mapping.get((self.source, self.target))

    def load_dictionary(self):
        if not self.filename:
            self.data = {}
            return

        base_dir = os.path.dirname(__file__)
        filepath = os.path.join(base_dir, self.filename)

        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            print(f"Dictionary file '{filepath}' not found. Starting empty.")
            self.data = {}

    def save_dictionary(self):
        if not self.filename:
            return

        base_dir = os.path.dirname(__file__)
        filepath = os.path.join(base_dir, self.filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def translate(self, text):
        words = text.split()
        translated_words = []

        for word in words:
            if word in self.data:
                translated_words.append(self.data[word])
            else:
                print(f"Word '{word}' not found in dictionary.")
                new_word = input(f"Please enter translation for '{word}': ").strip()
                if new_word:
                    self.data[word] = new_word
                    self.save_dictionary()
                    translated_words.append(new_word)
                else:
                    translated_words.append(f"[{word} not found]")

        return " ".join(translated_words)


class LaunchProcess:
    def __init__(self):
        self.translator = None

    def choose_language(self):
        print("******* Translator *******")
        print("1 >> Georgian-English")
        print("2 >> English-Georgian")

        while True:
            try:
                choice = int(input("Please choose which dictionary you want: "))
            except ValueError:
                print("Please enter number 1 or 2.")
                continue

            if choice == 1:
                self.translator = Translator("georgian", "english")
                print("You chose Georgian-English dictionary")
                break
            elif choice == 2:
                self.translator = Translator("english", "georgian")
                print("You chose English-Georgian dictionary")
                break
            else:
                print("Please try again (1 or 2).")

    def run(self):
        self.choose_language()

        while True:
            text = input("Write the text you want to translate or type 'exit' to exit: ").strip()
            if text.lower() == "exit":
                print("Process is over!")
                break

            result = self.translator.translate(text)
            print("Result:  →", result)


if __name__ == "__main__":
    app = LaunchProcess()
    app.run()

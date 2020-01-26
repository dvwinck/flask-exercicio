
class Morse:

    charMorse ={
        "" : "",
        " " : "__",
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
        ".\n" : ".-.-.-",
        "," : "--..--",
        ":" : "---...",
        "?" : "..--..",
        "'" : ".----.",
        "-" : "-....-",
        "/" : "-..-.",
        "@" : ".--.-.",
        "\n<BT>\n" : "-...-",
        "<SN>" : "...-.",
        "<KN>" : "-.--."
    }

    def toMorseCode(self, code):
        var_new = list(code.upper())
        print(">>",code, var_new)
        result = ""
        for character in var_new:
            result = result + self.charMorse.get(character)+" "
        return result

    def toText(self, code):
        string = str(code)
        var_new = string.split(" ")
        print('** ',var_new)
        result = ""
        for codechar in var_new:
            result =  result + self.morseToText(codechar)
        return  result

    def morseToText(self, codechar):
        for charKey in self.charMorse :
            if self.charMorse[charKey] == codechar:
                return charKey

        return  " "
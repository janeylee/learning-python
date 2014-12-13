vowels = ['a','e','i','o','u', 'A','E','I','O','U']
weirdos = ['th','st','qu','pl','tr']
 
def pig_latin(word):
    for letter in word:
        if word[0] in vowels:
            return word[:]+"hay"
        elif word[0:2] in weirdos:
            return word[2:] + word[0:2] + "ay"
        else:
            return word[1:] + word[0] + "ay"
 
 
phrase = raw_input("enter phrase: ")
 
def pig_latin_for_sentences(phrase):
    word_list = phrase.lower()
    word_list = word_list.split()
    new_sentence = ""
 
    for word in word_list:
        new_sentence = new_sentence + pig_latin(word)
        new_sentence = new_sentence + " "
    return new_sentence
 
 
print pig_latin_for_sentences(phrase)

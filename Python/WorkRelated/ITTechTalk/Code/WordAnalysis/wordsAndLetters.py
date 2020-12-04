import re
import os
import openpyxl
import string

"""
TODO: Implement a feature so that each book is given its own sheet for analysis
"""
path_to_texts = "C:/dev/workspace-vscode/Python/WorkRelated/ITTechTalk/Code/WordAnalysis/texts"


def word_count():
    paths = get_paths(path_to_texts)
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    words = {}
    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            for line in f:
                for word in line.split():
                    new_word = regex.sub('', word)
                    if new_word not in words:
                        words[new_word] = 1
                    else:
                        words[new_word] += 1
    f.close()
    return words


def generate_word_file(wawb, words):
    wordAnalysis = wawb['Word Analysis']
    counter = 2
    total_words = 0
    for x in words:
        wordAnalysis.cell(row=counter, column=1).value = x
        wordAnalysis.cell(row=counter, column=2).value = words[x]
        wordAnalysis.cell(row=counter, column=3).value = len(x)
        total_words += words[x]
        counter += 1
    wordAnalysis.cell(row=2, column=4).value = total_words
    wawb.save("Analysis.xlsx")


def letter_count():
    paths = get_paths(path_to_texts)
    letters = {}
    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            for line in f:
                for char in line:
                    if char.isalpha():
                        lower = char.lower()
                        if lower not in letters:
                            letters[lower] = 1
                        else:
                            letters[lower] += 1
    f.close()
    return letters


def generate_letter_file(wawb, letters):
    letterAnalysis = wawb['Letter Analysis']
    counter = 2
    letterAnalysis['A1'] = 'Letter'
    letterAnalysis['B1'] = 'Occurrences'
    for x in letters:
        letterAnalysis.cell(row=counter, column=1).value = x
        letterAnalysis.cell(row=counter, column=2).value = letters[x]
        counter += 1
    wawb.save("Analysis.xlsx")
    


def setup_wb(wawb):
    wawb.create_sheet(index=0, title='Word Analysis')
    wawb.create_sheet(index=1, title='Letter Analysis')
    wordAnalysis = wawb['Word Analysis']
    wordAnalysis['A1'] = 'Word'
    wordAnalysis['B1'] = 'Occurrences'
    wordAnalysis['C1'] = 'Word Length'
    wordAnalysis['D1'] = 'Total Words'
    letterAnalysis = wawb['Letter Analysis']
    letterAnalysis['A1'] = 'Letter'
    letterAnalysis['B1'] = 'Occurrences'
    wawb.save("Analysis.xlsx")


def get_paths(main_path):
    text_file_names = os.listdir(main_path)
    return [main_path + '/' + c for c in text_file_names]


def main():
    list_of_texts = get_paths(path_to_texts)
    wb = openpyxl.Workbook()
    setup_wb(wb)
    words = word_count()
    letters = letter_count()
    generate_word_file(wb, words)
    generate_letter_file(wb, letters)



if __name__ == '__main__':
    main()

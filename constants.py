import regex

JOBS_URL = "https://www.bsc.es/join-us/job-opportunities"

EDUCATION_PATTERN = regex.compile(
    "Education(.*?)Essential Knowledge", flags=regex.DOTALL
)
# EDUCATION_PATTERN = regex.compile("Education.*", flags=regex.DOTALL)

ESSENTIAL_PATTERN = regex.compile(
    "(.*?)Essential Knowledge and Professional Experience(.*?)(Additional Knowledge|Competences)",
    flags=regex.DOTALL,
)

ADDITIONAL_PATTERN = regex.compile(
    "(.*?)Additional Knowledge and Professional Experience(.*?)$", flags=regex.DOTALL
)
string = """
Education
PhD Computer Architecture with focus on HPES for critical systems
Essential Knowledge and Professional Experience
Demonstrated experience in the participation on at 3 EU project on this area where clear contributions have been made by the candidate
Practical experience in gem5 and system C
Practical experience in parallelizing and vectorizing applications
Practical experience in Apollo
Practical experience with OpenVPX- and SOSA-based systems
Competences
Familiarity with RISC-V is a plus
Familiarity with CPU/MPSoC performance evaluation is a plus
"""


# print(regex.search(ESSENTIAL_PATTERN, string).group(2))
# print(regex.search(ADDITIONAL_PATTERN, string).group(2))
def count_words(text):
    # 1. Split the text into words
    allowed_symbols = ["_", "-"]
    # List that will hold all words
    words = []
    # Variable that will hold a word
    word = ""
    for char in text:
        if char.isalnum() or char in allowed_symbols:
            word += char.lower()
        else:
            if word != "":
                words.append(word)
                word = ""
    # 2. Handle last word
    if word != "":
        words.append(word)

    # Count ocurrences
    word_count = {}
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count

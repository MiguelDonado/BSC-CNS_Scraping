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

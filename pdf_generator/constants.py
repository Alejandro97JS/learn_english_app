VOCABULARY_EXPRESSIONS_TITLE = "Vocabulary and Expressions"

# Folder for the generated PDF files:
GENERATED_PDFS_FOLDER = "generated_pdfs"

# Base filename for the generated PDF files,
# ready to be filled with a timestamp or identifier:
VOCABULARY_PDF_FILE_NAME = "{}_Vocabulary.pdf"

# Datetime format for the timestamp of the file names
# of the generated PDF files:
DATETIME_FILE_FORMAT = "%Y%m%d_%H%M%S"

# Configuration parameters for fpdf library:

PDF_WIDTH = 40
PDF_HEIGHT = 10
PDF_LN = 1

PDF_WRITE_WIDTH = 5
PDF_WRITE_HEIGHT = 10

FAMILY_ARIAL = "Arial"

STYLE_B = "B"

DEFAULT_FONT = {
    "family": FAMILY_ARIAL,
    "style": "",
    "size": 12
}

TITLE_FONT = {
    "family": FAMILY_ARIAL,
    "style": STYLE_B,
    "size": 16
}

VOCABULARY_TITLE_FONT = {
    "family": FAMILY_ARIAL,
    "style": STYLE_B,
    "size": 13
}

VOCABULARY_EXAMPLES_TITLE_FONT = {
    "family": FAMILY_ARIAL,
    "style": STYLE_B,
    "size": 11
}

# Texts for the content of the PDF file:
LABELS_HEADER_TEXT = "Labels: "
LANGUAGE_STYLE_HEADER_TEXT = "Language Style: "
PRONUNCIATION_NOTES_HEADER_TEXT = "Pronunciation Notes: "
DESCRIPTION_HEADER_TEXT = "Description: "
EXAMPLES_HEADER_TEXT = "Examples: "

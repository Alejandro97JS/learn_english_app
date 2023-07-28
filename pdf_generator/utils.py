from generic.models import LanguageStyle
from . import constants

def append_vocabulary_entry_to_doc(pdf, index, vocabulary_entry):
    # Title of the vocabulary entry:
    title = "{} - {}{}".format(
        index,
        vocabulary_entry.title,
        (" ({})".format(vocabulary_entry.spanish_title)
            if vocabulary_entry.spanish_title not in [None, ""] else "")
    )
    write_simple(pdf, title, constants.VOCABULARY_TITLE_FONT)
    # Labels (if exists):
    if vocabulary_entry.labels.exists():
        labels_text = constants.LABELS_HEADER_TEXT + ", ".join(
            vocabulary_entry.labels.all().values_list("name", flat = True))
        write_simple(pdf, labels_text, constants.DEFAULT_FONT)
    # Language style (if specified):
    if vocabulary_entry.language_style != LanguageStyle.NOT_SPECIFIED:
        language_style_text = constants.LANGUAGE_STYLE_HEADER_TEXT + vocabulary_entry.language_style_readable
        write_simple(pdf, language_style_text, constants.DEFAULT_FONT)
    # Pronunciation notes (if exists):
    pronunciation_notes = vocabulary_entry.pronunciation_notes
    if pronunciation_notes not in [None, ""]:
        pronunciation_notes_text = constants.PRONUNCIATION_NOTES_HEADER_TEXT + str(
            pronunciation_notes)
        write_simple(pdf, pronunciation_notes_text, constants.DEFAULT_FONT)
    # Description:
    description = vocabulary_entry.description
    spanish_description = vocabulary_entry.spanish_description
    if description not in [None, ""] or spanish_description not in [None, ""]:
        description_sol = description if description not in [None, ""] else ""
        spanish_description_sol = (" ({})".format(spanish_description)
            if spanish_description not in [None, ""]
            else "")
        description_text = constants.DESCRIPTION_HEADER_TEXT + str(
            description_sol) + str(spanish_description_sol)
        write_simple(pdf, description_text, constants.DEFAULT_FONT)
    # Examples (if exists):
    if vocabulary_entry.examples.exists():
        # Examples - Header:
        write_simple(pdf, constants.EXAMPLES_HEADER_TEXT, constants.VOCABULARY_TITLE_FONT)
        # Iterate over all the related examples and write its content:
        for example in vocabulary_entry.examples.all():
            example_text = "{}{}".format(
                example.text,
                (" ({})".format(example.text_spanish)
                    if example.text_spanish not in [None, ""] else ""
                )
            )
            write_simple(pdf, example_text, constants.DEFAULT_FONT)

def write_simple(pdf, text, font = None):
    # Auxiliary method to write text in pdf.
    # If font is specified, it is set before
    # writing.
    if font is not None:
        pdf.set_font(**font)
    pdf.multi_cell(0, constants.PDF_CELL_WRITE_HEIGHT, text)

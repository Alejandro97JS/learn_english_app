import os
from datetime import datetime
from fpdf import FPDF

from django.conf import settings
from django.http import FileResponse

from vocabulary_expressions.models import Entry as VocabularyEntry
from . import utils, constants

def generate_vocabulary_pdf(request):
    # DB to PDF:
    # Get all vocabulary entries from DB:
    vocabulary_entries = VocabularyEntry.objects.all()
    # Create PDF using fpdf library:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(
        **constants.TITLE_FONT
    )
    pdf.cell(constants.PDF_WIDTH, constants.PDF_HEIGHT,
        constants.VOCABULARY_EXPRESSIONS_TITLE, ln=constants.PDF_LN)
    # For each entry, add the formatted content to the PDF:
    for index, vocabulary_entry in enumerate(vocabulary_entries):
        utils.append_vocabulary_entry_to_doc(pdf, index+1, # index+1 to use 1-based indices.
            vocabulary_entry)
    # Create folder to save the file:
    media_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    if not os.path.exists(media_path):
        os.mkdir(media_path)
    generated_pdfs_path = os.path.join(media_path, constants.GENERATED_PDFS_FOLDER)
    if not os.path.exists(generated_pdfs_path):
        os.mkdir(generated_pdfs_path)
    # Save the file, whose name has a timestamp:
    now = datetime.utcnow()
    filename = constants.VOCABULARY_PDF_FILE_NAME.format(
        now.strftime(constants.DATETIME_FILE_FORMAT)
    )
    filepath = os.path.join(generated_pdfs_path, filename)
    pdf.output(filepath, 'F')
    # Additionally, return it in a FileResponse:
    return FileResponse(
        open(filepath, mode = 'rb'), 
        content_type='application/pdf'
    )
    
import os
import datetime
from fpdf import FPDF

from django.conf import settings
from django.http import FileResponse

from vocabulary_expressions.models import Entry as VocabularyEntry
from . import utils, constants

def generate_vocabulary_pdf(request):
    # DB to PDF:
    # Get potential filters to apply:
    # 1 - Category label name:
    category_label_names = request.GET.get("category_label_names")
    # 2 - Label Name:
    label_names = request.GET.get("label_names")
    # 3 - Language style:
    language_styles = request.GET.get("language_styles")
    # 4 - Date from:
    date_from = request.GET.get("date_from")
    # Get vocabulary entries from DB:
    vocabulary_entries = VocabularyEntry.objects.all()
    active_filters_text = ""
    if category_label_names:
        vocabulary_entries = vocabulary_entries.filter(
            category_labels__name__in=category_label_names.split(",")).distinct()
        active_filters_text += f"- Categories: {category_label_names.replace(",", ", ")}\n"
    if label_names:
        vocabulary_entries = vocabulary_entries.filter(
            labels__name__in=label_names.split(",")).distinct()
        active_filters_text += f"- Labels: {label_names.replace(",", ", ")}\n"
    if language_styles:
        vocabulary_entries = vocabulary_entries.filter(
            language_style__in=language_styles.split(","))
        active_filters_text += f"- Language styles: {language_styles}\n"
    if date_from:
        vocabulary_entries = vocabulary_entries.filter(
            created_at__gte=datetime.datetime.strptime(date_from,"%Y-%m-%d"))
        active_filters_text += f"- Entries from: {date_from}\n"
    # Create PDF using fpdf library:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(
        **constants.ANNOTATION_FONT
    )
    utils.write_simple(pdf, "PDF generated at "
        f"{datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")} UTC")
    # Write an annotation of active filters in PDF:
    if active_filters_text:
        utils.write_simple(pdf, "Applied filters:\n" + active_filters_text)
    pdf.set_font(
        **constants.TITLE_FONT
    )
    pdf.cell(0, constants.PDF_CELL_TITLE_HEIGHT,
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
    now = datetime.datetime.now(datetime.timezone.utc)
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
    
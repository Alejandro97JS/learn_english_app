import os, json

from django.http import HttpResponse
from django.conf import settings

from . import utils, constants

def recalculate_overall_statistics(request):
    # Generate dictionary with the statistics data:
    statistics_dict = utils.generate_overall_statistics()
    # Create folder to save the file:
    media_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    if not os.path.exists(media_path):
        os.mkdir(media_path)
    statistics_path = os.path.join(media_path, constants.STATISTICS_FOLDER)
    if not os.path.exists(statistics_path):
        os.mkdir(statistics_path)
    json.dump(statistics_dict, open(os.path.join(
        statistics_path, constants.STATISTICS_OVERALL_FILE), mode="w"), indent=3)
    # Response:
    response_text = "App statistics have been recalculated!"
    return HttpResponse(response_text, status = 200)

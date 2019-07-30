import logging

from django.shortcuts import render
from greeter.services import greeting

logger = logging.getLogger(__name__)


def index(request):
    # Get the text from the greeting service
    greet = greeting("en")
    logger.debug(f"Got greeting: {greet}")
    return render(request, "hello/index.html", {"greeting": greet})

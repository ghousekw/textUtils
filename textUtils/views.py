# i have created this file - Areeb
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    params = {"name": "Areeb", "place": "Mars"}
    return render(request, 'index.html', params)


def analyze(request):
    # Getting text
    djtext = request.POST.get("text", "default")

    # Checkbox values
    removePunc = request.POST.get("removePunc", "Off")
    capit = request.POST.get("capit", "Off")
    newLineRemover = request.POST.get("newLineRemover", "Off")
    spaceRemover = request.POST.get("spaceRemover", "Off")
    charCount = request.POST.get("charCount", "Off")

    # Check which checkbox is on

    # Remove punctuations from text
    if removePunc == "on":
        punctuations = '''!()-[]{};:\'"\,<>./?@#$%^&*=_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params);

    # Capitalize the text
    if capit == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed to UpperCase", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params);

    # Remove newline from text
    if newLineRemover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {"purpose": "Remove new lines", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params);

    # Remove spaces from text
    if spaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Remove spaces from text", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params);

    if removePunc != "on" and capit != "on" and spaceRemover != "on" and newLineRemover != "on":
        return HttpResponse("Please select any operation")

    return render(request, "analyze.html", params)

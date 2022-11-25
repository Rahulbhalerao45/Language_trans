from django.http import HttpResponse
from django.shortcuts import render
import googletrans
from googletrans import Translator

translator = Translator()


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    Marathi = request.POST.get('Marathi', 'off')
    Hindi = request.POST.get('Hindi', 'off')
    Tamil = request.POST.get('Tamil', 'off')
    Telgu = request.POST.get('Telgu', 'off')
    Malyalam = request.POST.get('Malyalam', 'off')

    count = 0
    if Marathi == "on":
        count += 1
    if Hindi == "on":
        count += 1
    if Tamil == "on":
        count += 1
    if Telgu == "on":
        count += 1
    if Malyalam == "on":
        count += 1
    if count > 3:
        params = {'purpose': "You can't select more than three languages"}
        return render(request, 'analyze.html', params)

    if count == 3:
        if Marathi == "on" and Hindi == "on" and Tamil == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="hi")
            newlan12 = translator.translate(djtext, dest="ta")
            analyzed = "Marathi - " + newlan.text + "\nHindi-  " + newlan1.text + "\nTamil- " + newlan12.text

            params = {'purpose': 'Marathi Hindi Tamil', 'analyzed_text': analyzed}
            djtext = analyzed

        if Marathi == "on" and Tamil == "on" and Telgu == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="Ta")
            newlan12 = translator.translate(djtext, dest="Te")
            analyzed = "Marathi - " + newlan.text + "\nTamil-  " + newlan1.text + "\nTelgu- " + newlan12.text

            params = {'purpose': 'Marathi Tamil Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        if Marathi == "on" and Hindi == "on" and Telgu == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="hi")
            newlan12 = translator.translate(djtext, dest="Te")
            analyzed = "Marathi - " + newlan.text + "\nHindi-  " + newlan1.text + "\nTelgu- " + newlan12.text

            params = {'purpose': 'Marathi Hindi Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        if Tamil == "on" and Hindi == "on" and Telgu == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="hi")
            newlan12 = translator.translate(djtext, dest="Te")
            analyzed = "Tamil - " + newlan.text + "\nHindi-  " + newlan1.text + "\nTelgu- " + newlan12.text

            params = {'purpose': 'Tamil Hindi Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        if Tamil == "on" and Hindi == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="hi")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Tamil - " + newlan.text + "\nHindi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Tamil Hindi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed
        if Hindi == "on" and Marathi == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="hi")
            newlan1 = translator.translate(djtext, dest="mr")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Hindi - " + newlan.text + "\nMarathi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Hindi Marathi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed
        if Telgu == "on" and Marathi == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="te")
            newlan1 = translator.translate(djtext, dest="mr")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Telgu - " + newlan.text + "\nMarathi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Telgu Marathi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed
        if Tamil == "on" and Telgu == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="te")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Tamil- " + newlan.text + "\Telgu-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Tamil Telgu Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed
            # if Tamil == "on" and Hindi == "on" and Malyalam == "on":
            #     analyzed = ""
            #     newlan = translator.translate(djtext, dest="ta")
            #     newlan1 = translator.translate(djtext, dest="hi")
            #     newlan12 = translator.translate(djtext, dest="ml")
            #     analyzed = "Tamil- "+newlan.text + "\nHindi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Tamil Hindi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed
        if Tamil == "on" and Marathi == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="mr")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Tamil- " + newlan.text + "\nMarathi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Tamil Marathi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed

        if Hindi == "on" and Telgu == "on" and Malyalam == "on":
            analyzed = ""
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="mr")
            newlan12 = translator.translate(djtext, dest="ml")
            analyzed = "Tamil - " + newlan.text + "\nMarathi-  " + newlan1.text + "\nMalyalm- " + newlan12.text

            params = {'purpose': 'Marathi', 'analyzed_text': analyzed}
            djtext = analyzed

    ###############TWO-------Language################################################
    if count == 2:
        # if Marathi == "on" and Hindi == "on":
        #     newlan = translator.translate(djtext, dest="mr")
        #     newlan1 = translator.translate(djtext, dest="hi")
        #     analyzed = "Marathi - "+newlan.text + "\nHindi-  " + newlan1.text

        #     params = {'purpose': 'Marathi Hindi', 'analyzed_text': analyzed}
        #     djtext = analyzed
        ##=mr,ta,te,ml
        ##-hi
        if Marathi == "on" and Tamil == "on":
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="ta")
            analyzed = "Marathi - " + newlan.text + "\nTamil-  " + newlan1.text

            params = {'purpose': 'Marathi Tamil', 'analyzed_text': analyzed}
            djtext = analyzed
        if Marathi == "on" and Malyalam == "on":
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="ml")
            analyzed = "Marathi - " + newlan.text + "\nMalyalm-  " + newlan1.text

            params = {'purpose': 'Marathi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed

        if Marathi == "on" and Telgu == "on":
            newlan = translator.translate(djtext, dest="mr")
            newlan1 = translator.translate(djtext, dest="te")
            analyzed = "Marathi - " + newlan.text + "\nTelgu-  " + newlan1.text

            params = {'purpose': 'Marathi Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        if Hindi == "on" and Telgu == "on":
            newlan = translator.translate(djtext, dest="hi")
            newlan1 = translator.translate(djtext, dest="te")
            analyzed = "Hindi - " + newlan.text + "\nTelgu-  " + newlan1.text

            params = {'purpose': 'Hindi Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        if Hindi == "on" and Tamil == "on":
            newlan = translator.translate(djtext, dest="hi")
            newlan1 = translator.translate(djtext, dest="ta")
            analyzed = "Hindi - " + newlan.text + "\nTamil-  " + newlan1.text

            params = {'purpose': 'Hindi Tamil', 'analyzed_text': analyzed}
            djtext = analyzed
        if Hindi == "on" and Malyalam == "on":
            newlan = translator.translate(djtext, dest="hi")
            newlan1 = translator.translate(djtext, dest="ml")
            analyzed = "Hindi - " + newlan.text + "\nMalyalm-  " + newlan1.text

            params = {'purpose': 'Hindi Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed

        if Hindi == "on" and Marathi == "on":
            newlan = translator.translate(djtext, dest="hi")
            newlan1 = translator.translate(djtext, dest="mr")
            analyzed = "Hindi- " + newlan.text + "\nMarathi-  " + newlan1.text
            print(newlan.text)

            params = {'purpose': 'Hindi Marathi', 'analyzed_text': analyzed}
            djtext = analyzed

            if Malyalam == "on" and Hindi == "on":
                newlan = translator.translate(djtext, dest="ml")
                newlan1 = translator.translate(djtext, dest="hi")
                analyzed = "Malyalm - " + newlan.text + "\nHindi-  " + newlan1.text

                params = {'purpose': 'Malyalm Hindi', 'analyzed_text': analyzed}
                djtext = analyzed
            ##=mr,ta,te,ml
            ##-hi
        # if Malyalam == "on" and Tamil == "on":
        #     newlan = translator.translate(djtext, dest="ml")
        #     newlan1 = translator.translate(djtext, dest="ta")
        #     analyzed = "Malyalm- "+newlan.text + "\nTamil-  " + newlan1.text

        #     params = {'purpose': 'Malyalm Tamil', 'analyzed_text': analyzed}
        #     djtext = analyzed

        # if Malyalam == "on" and Marathi == "on":
        #     newlan = translator.translate(djtext, dest="ml")
        #     newlan1 = translator.translate(djtext, dest="mr")
        #     analyzed = "Malyalm - "+newlan.text + "\nMarathi-  " + newlan1.text

        #     params = {'purpose': 'Malyalm Marathi', 'analyzed_text': analyzed}
        #     djtext = analyzed

        if Malyalam == "on" and Telgu == "on":
            newlan = translator.translate(djtext, dest="ml")
            newlan1 = translator.translate(djtext, dest="te")
            analyzed = "Malyalm - " + newlan.text + "\nTelgu-  " + newlan1.text

            params = {'purpose': 'Malyalm Telgu', 'analyzed_text': analyzed}
            djtext = analyzed

        # if Telgu == "on" and Hindi == "on":
        #     newlan = translator.translate(djtext, dest="te")
        #     newlan1 = translator.translate(djtext, dest="hi")
        #     analyzed = "Telgu- "+newlan.text + "\nHindi-  " + newlan1.text

        #     params = {'purpose': 'Telgu Hindi', 'analyzed_text': analyzed}
        #     djtext = analyzed

        if Telgu == "on" and Tamil == "on":
            newlan = translator.translate(djtext, dest="te")
            newlan1 = translator.translate(djtext, dest="ta")
            analyzed = "Telgu- " + newlan.text + "\nTamil-  " + newlan1.text

            params = {'purpose': 'Telgu Tamil', 'analyzed_text': analyzed}
            djtext = analyzed

        # if Telgu == "on" and Malyalam == "on":
        #     newlan = translator.translate(djtext, dest="te")
        #     newlan1 = translator.translate(djtext, dest="ml")
        #     analyzed = "Telgu- "+newlan.text + "\nMalyalm-  " + newlan1.text

        #     params = {'purpose': 'Telgu Malyalm', 'analyzed_text': analyzed}
        #     djtext = analyzed

        # if Telgu == "on" and Marathi == "on":
        #     newlan = translator.translate(djtext, dest="te")
        #     newlan1 = translator.translate(djtext, dest="mr")
        #     analyzed = "Telgu- "+newlan.text + "\nMarathi-  " + newlan1.text

        #     params = {'purpose': 'Telgu Marathi', 'analyzed_text': analyzed}
        #     djtext = analyzed

        # if Tamil == "on" and Hindi == "on":
        #     newlan = translator.translate(djtext, dest="ta")
        #     newlan1 = translator.translate(djtext, dest="hi")
        #     analyzed = "Tamil- "+newlan.text + "\nHindi-  " + newlan1.text

        #     params = {'purpose': 'Tamil Hindi', 'analyzed_text': analyzed}
        #     djtext = analyzed

        # if Tamil == "on" and Telgu == "on":
        #     newlan = translator.translate(djtext, dest="ta")
        #     newlan1 = translator.translate(djtext, dest="te")
        #     analyzed = "Tamil- "+newlan.text + "\nTelgu-  " + newlan1.text

        #     params = {'purpose': 'Tamil Telgu', 'analyzed_text': analyzed}
        #     djtext = analyzed

        if Tamil == "on" and Malyalam == "on":
            newlan = translator.translate(djtext, dest="ta")
            newlan1 = translator.translate(djtext, dest="ml")
            analyzed = "Tamil- " + newlan.text + "\nMalyalm-  " + newlan1.text

            params = {'purpose': 'Tamil Malyalm', 'analyzed_text': analyzed}
            djtext = analyzed

        # if Tamil == "on" and Marathi == "on":
        #     newlan = translator.translate(djtext, dest="ta")
        #     newlan1 = translator.translate(djtext, dest="mr")
        #     analyzed = "Tamil- "+newlan.text + "\nMarathi-  " + newlan1.text

        #     params = {'purpose': ' Tamil Marathi', 'analyzed_text': analyzed}
        #     djtext = analyzed

    # if(Hindi=="on"):
    #
    #     analyzed = ""
    #     newlan=translator.translate(djtext,dest="hi")
    #     analyzed=newlan.text
    #
    #
    #
    #     params = {'purpose':'Hindi', 'analyzed_text': analyzed}
    #     djtext = analyzed

    # if(Tamil=="on"):
    #     analyzed = ""
    #
    #
    #     params = {'purpose': 'Tamil', 'analyzed_text': analyzed}
    #     djtext = analyzed

    if count == 1:

        if Tamil == "on":
            newlan = translator.translate(djtext, dest="ta")
            analyzed = newlan.text
            params = {'purpose': 'Tamil', 'analyzed_text': analyzed}
        if Marathi == "on":
            newlan = translator.translate(djtext, dest="mr")
            analyzed = newlan.text
            params = {'purpose': 'Marathi', 'analyzed_text': analyzed}
        if Telgu == "on":
            newlan = translator.translate(djtext, dest="te")
            analyzed = newlan.text
            params = {'purpose': 'Telgu', 'analyzed_text': analyzed}
        if Malyalam == "on":
            newlan = translator.translate(djtext, dest="ml")
            analyzed = newlan.text
            params = {'purpose': 'Malyalam', 'analyzed_text': analyzed}

        if Hindi == "on":
            newlan = translator.translate(djtext, dest="hi")
            analyzed = newlan.text
            params = {'purpose': 'Hindi', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)

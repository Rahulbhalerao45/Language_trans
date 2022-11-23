from django.http import HttpResponse
from django.shortcuts import render
import googletrans
from googletrans import Translator
translator=Translator()


def index(request):

    return render(request,'index.html')
    
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    Marathi = request.POST.get('Marathi', 'off')
    Hindi = request.POST.get('Hindi', 'off')
    Tamil = request.POST.get('Tamil', 'off')
    Telgu = request.POST.get('Telgu', 'off')
    Malyalam = request.POST.get('Malyalam','off')

    if Marathi == "on" and Hindi == "on" and Tamil =="on":

        analyzed = ""
        newlan=translator.translate(djtext,dest="mr")
        newlan1=translator.translate(djtext,dest="hi")
        newlan12=translator.translate(djtext,dest="ta")
        analyzed=newlan.text+"  " + newlan1.text+ " " + newlan12.text



        params = {'purpose':'Marathi', 'analyzed_text': analyzed}
        djtext = analyzed

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
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    #     djtext = analyzed

    if (Telgu == "on"):
        analyzed = ""

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    if (Malyalam == "on"):
        analyzed = ""

        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    
    

    return render(request, 'analyze.html', params)

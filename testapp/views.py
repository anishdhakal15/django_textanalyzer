from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe

# Create your views here.
def home(request):
     return render(request,'index.html')

def calculate(request):
    if request.POST:
        raw=request.POST.get('text','none')
        choice=request.POST.getlist('calculate','none')
        compiled=''
        if 'punctuation' in choice:
            rslt=''
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in raw:
                if char not in punctuations:
                    rslt+=char
            compiled+="After removed punctuations:      "+rslt+'<br>'
        if 'capitalfirst' in choice:
            rslt=''
            for word in raw.split(' '):
                rslt+=word.capitalize()+' '
            compiled+="After capitalize first:      "+rslt+'<br>'
        if 'removespace' in choice:
            rslt=''.join([i for i in raw.split()])
            compiled+="After removed space:     "+rslt+'<br>'
        if 'charcount' in choice:
            count=0
            for word in raw:
                count+=1
            compiled+="Number of characters:     "+str(count)+'<br>'

        parameter = {
            'raw_text' : raw,
            'calculated_text' : mark_safe(compiled)
        }
        return render(request,'calculate.html',parameter)
    else:
        return HttpResponse('''redirecting to home in 3sec<script type="text/JavaScript">
                    setTimeout("location.href = '/';", 3000);
                </script>''')

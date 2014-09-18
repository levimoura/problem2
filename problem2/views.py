import os
import uuid
from pyramid.view import view_config
import deform
import colander
from pyramid.response import Response
from manipula_arquivo import manipulaArquivo
from str_strArr import strToStrArr
from GasStation import gasStation
#import upload_file
#@view_config(route_name='upload', renderer='templates/form.pt')
#def upload_view(request):

@view_config(route_name='upload', renderer='templates\mytemplate.pt')
def upload(context, request):
    #pagename = request.subpath[0]
    if 'form.submitted' in request.params:
        return Response("you may Upload the file")
    #else:
     #   return Response("Failed")
    ''' if 'submit' in request.POST:
           filename = request.POST['arquivo'].filename
           input_file = request.POST['arquivo'].file
           return Response('File uploaded: ' + filename)
       file_path = os.path.join('/tmp', 'arquivo.txt')
       temp_file_path = file_path + '~'
       output_file = open(temp_file_path, 'wb')
       input_file.seek(0)
       while True:
           data = input_file.read(2<<16)
           if not data:
               break
           output_file.write(data)
       output_file.close()
       output_file.rename(temp_file_path, 'arquivo.txt')
       
       class Schema(colander.Schema):
        upload = colander.SchemaNode(deform.FileData(), widget=deform.widget.FileUploadWidget(tmpstore))
    schema = Schema()
    form = deform.Form(schema, buttons=('submit',))'''

    #return Response('OK')
@view_config(route_name='result')
def result_view(request):
    str1 = manipulaArquivo('arquivo.txt')
    str2 = strToStrArr(str1)
    result = gasStation(str2)
    return Response('the result is :'+ str(result))
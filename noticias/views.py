from django.shortcuts import render

def noticias_economicas(request):
    diarios_links = [
        {'nombre': 'Enlace para leer  La Riqueza de las Naciones de Adam Smith', 'link': 'https://web.seducoahuila.gob.mx/biblioweb/upload/1%20La%20riqueza%20de%20las%20Adam%20Smith.pdf'},
        {'nombre': 'Enlace para leer La Economía Argentina desde las colonias al siglo 21 por el Dr. Aldo Ferrer', 'link': 'https://bibliotecafrancisco.files.wordpress.com/2016/06/aldo-ferrer-la-economc3ada-argentina-desde-sus-orc3adgenes-hasta-principios-del-siglo-xxi1.pdf'},
        {'nombre': 'Ir a la página de Ámbito Financiero', 'link': 'https://www.ambito.com/'},
        {'nombre': 'Ir a la página de Cronista Comercial ', 'link': 'https://www.cronista.com/'},
        {'nombre': 'Ir a la página del Banco Central de la República Argentina ', 'link': 'https://www.bcra.gob.ar/'},
        {'nombre': 'Ir a la la página de Bolsa de Comercio de Buenos Aires', 'link': 'https://www.labolsa.com.ar/'},
        {'nombre': 'Ir a  la página de Iproup ', 'link': 'https://www.iproup.com/'},
        {'nombre': 'Ir a la página de Iprofesional ', 'link': 'https://www.iprofesional.com/'},
        {'nombre': 'Ir a a la página del Ministerio de economía ', 'link': 'https://www.argentina.gob.ar/economia'},
        {'nombre': 'Ir a la página de El Economista ', 'link': 'https://eleconomista.com.ar/'},
        {'nombre': 'Ir a la página de Infobae', 'link': 'https://www.infobae.com/economia/'},
       
    ]
    
   
    context = {'diarios_links': diarios_links}

    return render(request, 'noticias/noticias.html', context)

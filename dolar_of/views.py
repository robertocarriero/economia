from datetime import datetime
from django.shortcuts import render
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def formatear_valor(valor):
    valor_formateado = "{:,.0f}".format(valor).replace(',', '.')
    return valor_formateado



# Vista para la página principal
def valor_usd_of(request):
    usd_of_por_mes = None
    grafico = None

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Lógica para obtener los datos desde la API del BCRA
        url = "https://api.estadisticasbcra.com/usd_of"
        headers = {
            "accept": "application/json",
            "Authorization": 
                    "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjEwMjE5NTAsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJyb2JlcnRvX2NhcnJpZXJvMUB5YWhvby5jb20uYXIifQ.Rawv8Od4sB8cCMrYze6NHyxdm4m7R5wUC5qhm4yIyT20FXgv-zEOl6rEN1CYSC_C43PgV4Crkj-JXgLijfr-7w"
                    }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Filtrar los datos según las fechas ingresadas por el usuario
        usd_of_filtrados = [{'d': item['d'], 'v': item['v']} for item in data if (not fecha_inicio or item['d'] >= fecha_inicio) and (not fecha_fin or item['d'] <= fecha_fin)]

        # Agrupar los datos por mes
        usd_of_por_mes = {}
        for item in usd_of_filtrados:
            fecha = datetime.strptime(item['d'], '%Y-%m-%d')
            fecha_formateada = fecha.strftime('%d-%m-%Y')
            mes = fecha.strftime('%B %Y')
            if mes not in usd_of_por_mes:
                usd_of_por_mes[mes] = []
            valor_formateado = formatear_valor(item['v'])
            usd_of_por_mes[mes].append({'d': fecha_formateada, 'v': valor_formateado})

        # Crear el gráfico de línea
        plt.figure(figsize=(6,6))
        for mes, depositos in usd_of_por_mes.items():
            fechas = [item['d'] for item in depositos]
            montos = [float(item['v'].replace('.', '').replace(',', '.')) for item in depositos]
            #plt.plot(fechas, montos, marker='o', linestyle='-', label=mes)
            plt.bar(fechas, montos, label=mes)
        plt.ylabel('USD')
        plt.title('Valor Dolar')
        plt.xticks(fechas[::30],rotation=45)
        plt.legend()

        # Guardar el gráfico en un buffer de Bytes
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico = base64.b64encode(buffer.getvalue()).decode()

    # Renderiza el template y pasa los datos del gráfico y la cotización
    return render(request, 'dolar_of/dolar_of.html', {'usd_of_por_mes': usd_of_por_mes, 'grafico': grafico})




from django.shortcuts import render
import requests

# Create your views here.




# Función para calcular el interés financiero
def calcular_interes_financiero(capital, tasa_interes, tiempo):
    # Cálculos utilizando  fórmula para el interés financiero
    
    monto= capital*(1+((tasa_interes/100)/365)*tiempo)
    im=tasa_interes/12
    
    return monto

# Vista para la página principal
def index(request):
    if request.method == 'POST':
        capital = float(request.POST.get('capital'))
        tasa_interes = float(request.POST.get('tasa_interes'))
        tiempo = float(request.POST.get('tiempo'))

        # Llamada a la función para calcular el interés financiero
        resultado = calcular_interes_financiero(capital, tasa_interes, tiempo)
        intereses= resultado-capital
        tasa_mensual=tasa_interes/12
        
        resultado= round(resultado,2)
        intereses=round(intereses,2)
        tasa_mensual=round(tasa_mensual,2)
        return render(request, 'principal/index.html', {'resultado': resultado,'intereses': intereses, 'tasa_mensual':tasa_mensual})

    return render(request, 'principal/index.html')



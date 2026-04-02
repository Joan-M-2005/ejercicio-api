from flask import Flask, request, jsonify 

app = Flask(__name__) 

@app.route('/promedio', methods=['POST']) 
def calcular_promedio():
    datos = request.get_json()
    nombre = datos['nombre'] 
    calificaciones = datos['calificaciones'] 
    
    # Se suman todas las calificaciones y se dividen entre la cantidad de elementos [cite: 66, 67, 68, 69, 85]
    promedio = sum(calificaciones) / len(calificaciones) 
    
    respuesta = { 
        "nombre": nombre, 
        "promedio": promedio 
    } # [cite: 89]
    
    return jsonify(respuesta) 

if __name__ == '__main__': 
    app.run(debug=True) 
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    try:
        datos = request.get_json()
        valor = float(datos['valor'])
        escala_origen = datos['escala'].upper() # Pasamos a mayúscula para evitar errores

        if escala_origen == 'C':
            # Fórmula: (C * 9/5) + 32
            resultado = (valor * 9/5) + 32
            escala_destino = 'F'
        elif escala_origen == 'F':
            # Fórmula: (F - 32) * 5/9
            resultado = (valor - 32) * 5/9
            escala_destino = 'C'
        else:
            return jsonify({"error": "Escala no válida. Usa 'C' o 'F'"}), 400

        respuesta = {
            "valor_original": valor,
            "escala_origen": escala_origen,
            "resultado": round(resultado, 2),
            "escala_destino": escala_destino
        }

        return jsonify(respuesta), 200

    except KeyError:
        return jsonify({"error": "Faltan datos requeridos (valor o escala)"}), 400
    except ValueError:
        return jsonify({"error": "El valor debe ser un número"}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
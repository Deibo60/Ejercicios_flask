# ejercicio2.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    # Validar que se enviaron datos
    if not datos:
        return jsonify({'error': 'No se recibieron datos'}), 400

    valor = datos.get('valor')
    escala = datos.get('escala')

    # Validar que existan los campos requeridos
    if valor is None:
        return jsonify({'error': 'Falta el campo valor'}), 400

    if not escala:
        return jsonify({'error': 'Falta el campo escala'}), 400

    escala = escala.upper()

    # Aplicar la fórmula de conversión según la escala de origen
    if escala == 'CELSIUS':
        resultado = (valor * 9 / 5) + 32
        escala_destino = 'Fahrenheit'

    elif escala == 'FAHRENHEIT':
        resultado = (valor - 32) * 5 / 9
        escala_destino = 'Celsius'

    else:
        return jsonify({
            'error': f'Escala "{escala}" no válida. Use CELSIUS o FAHRENHEIT'
        }), 400

    # Devolver respuesta en formato JSON
    return jsonify({
        'valor_original': valor,
        'escala_origen': escala.capitalize(),
        'resultado': round(resultado, 2),
        'escala_destino': escala_destino
    })

if __name__ == '__main__':
    app.run(debug=True)
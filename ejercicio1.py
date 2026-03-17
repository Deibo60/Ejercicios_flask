# ejercicio1.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    # Validar que se enviaron los datos necesarios
    if not datos:
        return jsonify({'error': 'No se recibieron datos'}), 400

    nombre = datos.get('nombre')
    calificaciones = datos.get('calificaciones')

    # Validar que existan los campos requeridos
    if not nombre:
        return jsonify({'error': 'Falta el nombre del estudiante'}), 400

    if not calificaciones or not isinstance(calificaciones, list):
        return jsonify({'error': 'Falta la lista de calificaciones'}), 400

    if len(calificaciones) == 0:
        return jsonify({'error': 'La lista de calificaciones está vacía'}), 400

    # Calcular el promedio
    promedio = sum(calificaciones) / len(calificaciones)

    # Devolver respuesta en formato JSON
    return jsonify({
        'estudiante': nombre,
        'calificaciones': calificaciones,
        'promedio': round(promedio, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
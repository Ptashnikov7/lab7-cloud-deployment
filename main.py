import os
from flask import Flask, request, jsonify

# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь, група АІ-235

app = Flask(__name__)

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(x0, eps=0.0001):
    x = x0
    for _ in range(1000):
        if f_prime(x) == 0:
            return None
        x_next = x - f(x)/f_prime(x)
        if abs(x_next - x) < eps:
            return x_next
        x = x_next
    return x

@app.route('/calculate', methods=['GET'])
def calculate():
    # Безпечне зчитування конфігурації через змінні середовища (Environment variables)
    student = os.getenv("STUDENT_NAME", "Ptashnikov Vasyl")
    group = os.getenv("GROUP", "AI-235")
    mode = os.getenv("MODE", "eco")
    
    x_param = request.args.get('x', default='1.0')
    try:
        x0 = float(x_param)
        root = newton_method(x0)
        if root is None:
            return jsonify({"error": "Method did not converge"}), 400
            
        return jsonify({
            "model": "Newton Method",
            "student": student,
            "group": group,
            "mode": mode,
            "input_x0": x0,
            "result_root": root,
            "status": "Deployed on Cloud (Render)"
        })
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    # Порт для Render має зчитуватись динамічно з системи
    port = int(os.getenv("PORT", 5000))
    # БЕЗПЕКА: debug mode повністю вимкнено (debug=False)
    app.run(host='0.0.0.0', port=port, debug=False)

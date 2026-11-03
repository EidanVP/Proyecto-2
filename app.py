from flask import Flask, render_template_string

app = Flask(__name__)

# Código HTML y CSS combinados para mayor facilidad
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículum - Eidan Vargas Prado</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            color: #333333;
            margin: 0;
            padding: 40px 20px;
        }

        .container {
            max-width: 650px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 86, 179, 0.1);
            border-top: 6px solid #0056b3;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        header h1 {
            margin: 0;
            color: #003366;
            font-size: 2.2em;
        }

        .location {
            color: #555555;
            margin: 8px 0;
            font-size: 1.1em;
        }

        .contact-info {
            font-size: 0.95em;
            color: #0056b3;
            font-weight: bold;
        }

        .section {
            margin-bottom: 25px;
        }

        .section h2 {
            color: #0056b3;
            border-bottom: 2px solid #e1ecf4;
            padding-bottom: 6px;
            font-size: 1.3em;
        }

        .skills-list {
            list-style-type: square;
            padding-left: 20px;
        }

        .skills-list li {
            margin-bottom: 10px;
            font-size: 1.05em;
            color: #444444;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Eidan Vargas Prado</h1>
            <p class="location">📍 San José, Costa Rica</p>
            <div class="contact-info">
                <span>📞 8557 1374</span> | 
                <span>✉️ eidan.vargas.2010@gmail.com</span>
            </div>
        </header>

        <section class="section">
            <h2>Perfil Profesional</h2>
            <p>Estudiante entusiasta de la tecnología con interés y bases en ciberseguridad, programación en Python y desarrollo web.</p>
        </section>

        <section class="section">
            <h2>Habilidades</h2>
            <ul class="skills-list">
                <li><strong>Ciberseguridad:</strong> Conceptos básicos de seguridad informática y buenas prácticas.</li>
                <li><strong>Python:</strong> Desarrollo de scripts y lógica de programación básica.</li>
                <li><strong>Desarrollo Web:</strong> Maquetación básica con HTML y estilos CSS.</li>
            </ul>
        </section>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("Iniciando aplicación web...")
    print("Abre tu navegador y entra a: http://127.0.0.1:5000")
    app.run(debug=True)
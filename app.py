from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/news')
def news():
    return render_template('news.html')

sent_forms = []

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Agregar el formulario enviado a la lista
        sent_forms.append({
            'name': name,
            'email': email,
            'message': message
        })

        # Redireccionar para evitar reenvío de formularios al refrescar
        return redirect(url_for('contact'))

    return render_template('contact.html', sent_forms=sent_forms)

if __name__ == '__main__':
    app.run(debug=True)

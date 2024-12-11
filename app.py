from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Modelo (Model)
# Simulamos una base de datos con una lista de items
items = []

def obtener_items():
    return items

def agregar_item(item_name):
    items.append(item_name)

def eliminar_item(item_name):
    items.remove(item_name)

def actualizar_item(old_name, new_name):
    index = items.index(old_name)
    items[index] = new_name


# Controlador (Controller)
# Página de inicio: muestra los elementos
@app.route('/')
def index():
    # Obtener los items desde el "modelo"
    items_data = obtener_items()
    return render_template('index.html', items=items_data)


# Crear un nuevo item
@app.route('/add', methods=['POST'])
def add():
    item_name = request.form['name']
    agregar_item(item_name)  # Llamar al "modelo" para agregar un nuevo item
    return redirect(url_for('index'))


# Eliminar un item
@app.route('/delete/<item>')
def delete(item):
    eliminar_item(item)  # Llamar al "modelo" para eliminar el item
    return redirect(url_for('index'))


# Actualizar un item
@app.route('/update/<old_name>', methods=['GET', 'POST'])
def update(old_name):
    if request.method == 'POST':
        new_name = request.form['name']
        actualizar_item(old_name, new_name)  # Llamar al "modelo" para actualizar el item
        return redirect(url_for('index'))
    return render_template('update.html', old_name=old_name)


# Vista (View)
# index.html
@app.route('/index')
def index_html():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Items</title>
    </head>
    <body>
        <h1>Lista de Items</h1>
        <ul>
            {% for item in items %}
                <li>{{ item }} <a href="{{ url_for('delete', item=item) }}">Eliminar</a></li>
            {% endfor %}
        </ul>
        <form action="{{ url_for('add') }}" method="POST">
            <input type="text" name="name" placeholder="Nuevo item" required>
            <button type="submit">Agregar Item</button>
        </form>
    </body>
    </html>
    '''

# update.html (plantilla para actualizar un item)
@app.route('/update')
def update_html():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Actualizar Item</title>
    </head>
    <body>
        <h1>Actualizar Item</h1>
        <form action="{{ url_for('update', old_name=old_name) }}" method="POST">
            <input type="text" name="name" value="{{ old_name }}" required>
            <button type="submit">Actualizar</button>
        </form>
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(debug=True)

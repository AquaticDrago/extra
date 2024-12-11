from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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



# Página de inicio: muestra los elementos
@app.route('/index')
def index():

    items_data = obtener_items()
    return render_template('index.html', items=items_data)


# Crear un nuevo item
@app.route('/add', methods=['POST'])
def add():
    item_name = request.form['name']
    agregar_item(item_name)  
    return redirect(url_for('index'))


# Eliminar un item
@app.route('/delete/<item>')
def delete(item):
    eliminar_item(item)  
    return redirect(url_for('index'))


# Actualizar un item
@app.route('/update/<old_name>', methods=['GET', 'POST'])
def update(old_name):
    if request.method == 'POST':
        new_name = request.form['name']
        actualizar_item(old_name, new_name)  
        return redirect(url_for('index'))
    return render_template('update.html', old_name=old_name)





if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulamos una base de datos con una lista
items = []

# Página de inicio: muestra los elementos
@app.route('/')
def index():
    return render_template('index.html', items=items)

class ControladorItems:
    def agregar(item_name):
        global items
        items.append(item_name)
        return redirect(url_for('index'))
        
    def actualizar():
        print("")
    def eliminar():
        print("")

# Crear un nuevo item
@app.route('/add', methods=['POST'])
def add():
        item_name = request.form['name']
        return controlador.agregar(item_name)
        

# Eliminar un item
@app.route('/delete/<item>')
def delete(item):
    items.remove(item)
    return redirect(url_for('index'))

# Actualizar un item 
@app.route('/update/<old_name>', methods=['GET', 'POST'])
def update(old_name):
    if request.method == 'POST':
        new_name = request.form['name']
        index = items.index(old_name)
        items[index] = new_name
        return redirect(url_for('index'))
    return render_template('update.html', old_name=old_name)

if __name__ == "__main__":
    app.run(debug=True)

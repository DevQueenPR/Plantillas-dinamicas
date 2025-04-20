from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos 
usuarios = []
productos = []


@app.route('/')
def index():
    return render_template('index.html')

# Usuarios
@app.route('/usuarios')
def mostrar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        if nombre and correo:
            usuarios.append({"nombre": nombre, "correo": correo})
        return redirect(url_for('mostrar_usuarios'))
    return render_template('agregar_usuario.html')

# Productos
@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        if nombre and precio:
            productos.append({"nombre": nombre, "precio": float(precio)})
        return redirect(url_for('mostrar_productos'))
    return render_template('agregar_producto.html')

# Edición y Borrar

# Editar usuario
@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if id < 0 or id >= len(usuarios):
        return "Usuario no encontrado", 404

    if request.method == 'POST':
        usuarios[id]['nombre'] = request.form['nombre']
        usuarios[id]['correo'] = request.form['correo']
        return redirect(url_for('mostrar_usuarios'))

    return render_template('editar_usuario.html', usuario=usuarios[id], id=id)

# Borrar usuario
@app.route('/borrar_usuario/<int:id>')
def borrar_usuario(id):
    if id < 0 or id >= len(usuarios):
        return "Usuario no encontrado", 404

    usuarios.pop(id)
    return redirect(url_for('mostrar_usuarios'))

# Editar producto
@app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    if id < 0 or id >= len(productos):
        return "Producto no encontrado", 404

    if request.method == 'POST':
        productos[id]['nombre'] = request.form['nombre']
        productos[id]['precio'] = request.form['precio']
        return redirect(url_for('mostrar_productos'))

    return render_template('editar_producto.html', producto=productos[id], id=id)

# Borrar producto
@app.route('/borrar_producto/<int:id>')
def borrar_producto(id):
    if id < 0 or id >= len(productos):
        return "Producto no encontrado", 404

    productos.pop(id)
    return redirect(url_for('mostrar_productos'))


if __name__ == '__main__':
    app.run(debug=True)

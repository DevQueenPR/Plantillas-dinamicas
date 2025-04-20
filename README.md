# Plantillas-dinámicas

Aplicación de los conceptos aprendidos sobre sistemas de plantillas Front-End con Flask. Contiene plantillas de HTML dinámicas que muestran datos provenientes del Back-End.

GitHub: [https://github.com/DevQueenPR/Plantillas-dinamicas](https://github.com/DevQueenPR/Plantillas-dinamicas)

## Arquitectura de la aplicación

### 1. Cliente (Front-End)
- **HTML**: Páginas que muestran la interfaz de usuario.
- **CSS/Bootstrap**: Diseño y estilos de las páginas.

### 2. Servidor (Back-End)
- **Flask**: Servidor web en Python que maneja las solicitudes HTTP.
- **Jinja2**: Renderiza el contenido dinámico en el lado del servidor antes de enviarlo al cliente.
  - **Plantilla base (base.html)**: Contiene el marco general (navbar y contenido).
  - **Plantillas hijas**: Cada página específica (usuarios.html, productos.html) hereda de `base.html` y define el contenido principal.

- **Rutas**:
  - `/info` (GET): Devuelve información básica sobre el sistema.
  - `/usuarios` (GET): Muestra la lista de usuarios.
  - `/productos` (GET): Muestra la lista de productos.
  - `/agregar_usuario` (GET/POST): Crea un nuevo usuario.
  - `/agregar_producto` (GET/POST): Crea un nuevo producto.
  - `/editar_usuario/<id>` (GET/POST): Edita un usuario existente.
  - `/editar_producto/<id>` (GET/POST): Edita un producto existente.
  - `/borrar_usuario/<id>` (GET): Borra un usuario.
  - `/borrar_producto/<id>` (GET): Borra un producto.

### 3. Base de Datos (Memoria)
- **Usuarios**: Lista de diccionarios, cada uno con nombre y correo.
- **Productos**: Lista de diccionarios, cada uno con nombre y precio.

## Reflexión

La separación entre el Back-End y el Front-End es uno de los principios fundamentales del desarrollo de software moderno, y su implementación en un proyecto mejora tanto la claridad como la escalabilidad. Ayuda en la claridad por medio de la organización, con cada parte teniendo una responsabilidad específica. Mejora el flujo de trabajo, siendo fácil de entender y seguir. Además, su flujo independiente permite que los desarrolladores realicen sus tareas sin depender directamente del otro, creando una separación clara y conveniente.

En términos de escalabilidad, facilita el crecimiento del proyecto. Al tener todo separado y legible, permite que sea escalable por su independencia. Además, la colaboración en equipo es más eficiente debido a la independencia entre las partes. Permite integrar tecnologías nuevas fácilmente y que estas se puedan mantener y actualizar con mayor facilidad. Es sumamente importante tomar en cuenta estos factores para permitir la continuidad de una aplicación eficiente y efectiva en su UX y UI.

## Pantallas

### Página principal (index.html)
- Se gestionan usuarios y productos.
- Permite ver usuarios y añadir usuarios.

### agregar_usuario.html
- Se añaden usuarios.

### usuarios.html
- Se ven, editan y borran usuarios.

### editar_usuario.html
- Se edita el usuario seleccionado.

### agregar_producto.html
- Se agregan productos.

### productos.html
- Se ven, editan y borran productos.

### editar_producto.html
- Se edita el producto seleccionado.

Guía de:
• Configuración
• Uso
• Contacto

Archivos de Configuración:

1. Configuración Principal (config.json)
En la carpeta raíz de esta aplicación, encontrarás un archivo llamado config.json. Este archivo contiene tres elementos clave:

IP: Debe estar configurada como 127.0.0.1 en el caso que se ejecute el servidor en el mismo equipo en que está abierto Holyrics. Este valor solo debe ser modificado si se pretende correr el servidor en un equipo diferente al que tiene abierto Holyrics.

Token: Este es el token que has obtenido y configurado previamente en Holyrics (Archivo > Configuraciones > API Server > Administrar permisos > Añadir, darle un nombre,  confirmar, luego editar y habilitar los permisos "ActionNext" y "ActionPrevious" solo en la columna "Local", copiar Token).

Puerto: El puerto que se haya establecido en la pestaña API Server (dice "porta" y está como predeterminado el 8091)

Puedes abrir y editar este archivo utilizando un editor de texto, como el Bloc de Notas.

2. Configuración Interna (_internal/config.txt)
Este segundo archivo de configuración debe contener la dirección IP de la transmisión de HTML 3 de Holyrics.

Ejemplo de IP: 192.168.100.5
Este archivo solo debe contener la IP de transmisión sin el resto de la URL "/stage-view/text3".

--------------------------------------------------------------

Uso:

Antes de ejecutar por primera vez "PPT Control_G.exe" debe asegurarse de que los archivos antes mencionados hayan sido configurados correctamente. De lo contrario el programa podría cerrarse al instante. Si por error borra los datos de los archivos de configuración o elimina los archivos deberá crearlos desde algún editor de texto y guardarlos en la misma carpeta donde se encuentra el ejecutable, por ejemplo con el bloc de notas. La carpeta "_internal" y su contenido son esenciales para el funcionamiento del programa.

- Ejemplo del contenido de config.json :

{
    "ip": "127.0.0.1",
    "token": "9270UeTNfOf2M6Id",
    "puerto": "8091"
}

- Ejemplo del contenido de config.txt

192.168.0.187

*En la primera ejecución se solicitará un permiso del Firewall de Windows para permitir al programa comunicarse a través del puerto configurado. Debe aceptar para que funcione.

--------------------------------------------------------------

Información de Contacto:
Si necesitas asistencia o tienes alguna duda, o te interesaría ver el código fuente, hacer mejoras/cambios, y/o hacer tu propia compilación puedes contactarme a través de:

Telegram: @mark_ost7

Abrazo cordial. Espero te sea de bendición.
Marcos Tapia - Iglesia Cristiana Evangélica La Paz.
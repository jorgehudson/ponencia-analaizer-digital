==== INSTRUCCIONES PARA PODER USAR EL COMPARADOR DE ENTIDADES ====
1. Crea un entorno virtual en tu editor de código para Python con el comando py -m venv venv
2. Activa dicho entorno virtual con ./venv/Scripts/activate
3. Ejecuta el comando pip install -r requirements.txt para instalar todas las dependencias que necesita este script para funcionar.
4. Crea un Custom Search Engine desde esta URL https://programmablesearchengine.google.com/ y copia su código CX y pégalo en la variable CX de claves.py.
5. Crea tu proyecto con una cuenta de servicio en Google Cloud https://cloud.google.com/?hl=es y habilita las siguientes APIs:
    4.1 Custom Search API (Debes generar para esta API una clave que tendrás que copiar en API_KEY de claves.py)
    4.2 Cloud Natural Language API (Requiere que añadas un método de pago y debes generar también una clave de API que luego deberás pegar en API_KEY_CNL claves.py)


==== MANUAL DE USO DEL COMPARADOR DE ENTIDADES ====
1. Debes ejecutar el comando py main.py y te pedirá que ingreses una URL de un contenido que quieras analizar, además te pedirá la keyword donde quieres rankear.
2. Debes esperar hasta que se genere un archivo en formato CSV llamado entidades_faltantes.csv que te dará todas las entidades que tiene tu competencia y tú no.
3. Pueden salir centenares de entidades y no todas tienen porque ser relevantes, la cuestión es que filtres de ese CSV las que tengan que ver con el tema que trata el contenido.
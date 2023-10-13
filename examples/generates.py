#!/usr/bin/python

import os
import subprocess


def generate_directory_list_with_format(directorio_raiz,pre_name,generate_img=True):
    # Obtener una lista de directorios que coinciden con el formato 'pre_name*'
    directorios = [nombre for nombre in os.listdir(directorio_raiz) if nombre.startswith(pre_name) and os.path.isdir(os.path.join(directorio_raiz, nombre))]

    # Iterar a traves de los directorios y ejecutar 'exec.sh' en cada uno
    if generate_img:
        for directorio in directorios:
            
            directorio_completo = os.path.join(directorio_raiz, directorio)
            script_ejecucion = 'work.sh'
            
            print('\n')
            print('directorio_completo:',directorio_completo)
            print('   script_ejecucion:',script_ejecucion)

            # Verificar si 'script_ejecucion' existe en el directorio
            if os.path.exists(os.path.join(directorio_completo, script_ejecucion)):
                print("Ejecutando '{}' en '{}'...".format(script_ejecucion,directorio_completo))
                proceso = subprocess.Popen(['sh', script_ejecucion], cwd=directorio_completo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                salida, errores = proceso.communicate()

                print('salida:',salida)
                print('errores:',errores)
            else:
                print("'{}' no encontrado en '{}'".format(script_ejecucion,directorio_completo))
    return directorios;

def write_file(directorio_raiz,directorios, nombre_archivo):
    # Ruta completa del archivo
    ruta_archivo = os.path.join(directorio_raiz, nombre_archivo)

    # Escribir el contenido en el archivo
    with open(ruta_archivo, 'w') as archivo:
        cadena='''
<html>
<head>
    <?php 
    include '../include/head-sub.php';
    ?>
</head>
<body>

<?php
ini_set('default_charset','UTF8');
include '../include/header-sub.php';
?>

    <div class="header gradient">
    <div class="promo-area">
<p>
Here you can see some examples
</p>
    </div>
    </div>
        ''';
        archivo.write(cadena);
        # Iterar a traves de los directorios y ejecutar 'exec.sh' en cada uno
        for directorio in directorios:
        
            cadena='''
<!-- *********************************************************************** -->
<div class="header libgradient">
    <p>
        <div class="whiteblock">
        <a href="{}/example.php"><img src="{}/example.png"/></a>
        </div>
        </a> 
    </p>
</div>
            '''.format(directorio,directorio);
            archivo.write(cadena);

        cadena='''
<!-- *********************************************************************** -->

<?php 
include '../include/footer-sub.php';
?>

</body>
</html>
        ''';
        archivo.write(cadena);


# Directorio raiz donde buscar los directorios
directorio_raiz = './';
generate_img=True;#False;

directorios=generate_directory_list_with_format(directorio_raiz,
                                                pre_name='env-highlight-',
                                                generate_img=generate_img);
write_file( directorio_raiz,
            directorios, 
            nombre_archivo = 'env-highlight-examples.php')


directorios=generate_directory_list_with_format(directorio_raiz,
                                                pre_name='env-box-',
                                                generate_img=generate_img);
write_file( directorio_raiz,
            directorios, 
            nombre_archivo = 'env-box-examples.php')

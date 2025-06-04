import re

# Cargar las categorías desde el archivo proporcionado (puedes integrarlo como un módulo si lo deseas)
estructuras_control = {'if', 'else', 'while', 'for', 'break', 'continue', 'pass'}
tipos_dato = {'int', 'float', 'str', 'bool'}
declaracion_variables = {'=', ':='}
asignacion = {'=', '+=', '-=', '=', '/=', '%=', '//=', '*='}
delimitadores = {'{', '}', '[', ']', '(', ')'}
separadores = {';', ',', '.', ':', ' '}
operadores_aritmeticos = {'+', '-', '*', '/', '%', '//'}
operadores_relacionales = {'==', '!=', '<', '>', '<=', '>='}
operadores_logicos = {'and', 'or', 'not'}
comentarios = {'#'}
palabras_funcionales = {
    'def', 'return', 'class', 'import', 'from', 'as', 'lambda',
    'with', 'try', 'except', 'finally', 'raise', 'assert',
    'yield', 'global', 'nonlocal'
}
funciones_built_in = {'print', 'input', 'length', 'range', 'type', 'int', 'float', 'str'}
literales = {'True', 'False', 'None'}
palabras_reservadas_extra = {'del', 'in', 'is'}

palabras_reservadas = (
    estructuras_control |
    tipos_dato |
    declaracion_variables |
    asignacion |
    delimitadores |
    separadores |
    operadores_aritmeticos |
    operadores_relacionales |
    operadores_logicos |
    comentarios |
    palabras_funcionales |
    funciones_built_in |
    literales |
    palabras_reservadas_extra
)

def analizar_token(token):
    if token in palabras_reservadas:
        print(f"[✔] Token reconocido: '{token}'")
    elif re.match(r'^[a-zA-Z_]\w*$', token):
        print(f"[✔] Identificador válido: '{token}'")
    elif re.match(r'^\d+(\.\d+)?$', token):
        print(f"[✔] Literal numérico: '{token}'")
    elif token.startswith('#'):
        print(f"[✔] Comentario detectado: '{token}'")
    elif token.strip() == '':
        pass  # ignorar espacios
    else:
        print(f"[✘] Error léxico: Token no reconocido -> '{token}'")

def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"Analizando archivo: {nombre_archivo}\n")
            for linea_num, linea in enumerate(archivo, 1):
                tokens = re.findall(r'\w+|==|!=|<=|>=|:=|[-+*/%=<>():{}[\];,.#]', linea)
                print(f"\nLínea {linea_num}: {linea.strip()}")
                for token in tokens:
                    analizar_token(token)
    except FileNotFoundError:
        print(f"[✘] Error: El archivo '{nombre_archivo}' no se encuentra.")
    except Exception as e:
        print(f"[✘] Error inesperado: {str(e)}")

# Cambia "archivo_fuente.txt" por el nombre real de tu archivo
analizar_archivo("C:/Users/Usuario/OneDrive/Escritorio/Automatas y Copiladores/archivo_fuente.txt")

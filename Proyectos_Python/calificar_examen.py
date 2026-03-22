import pandas as pd

# Cargar los archivos
df_estudiantes = pd.read_csv("./archivos/respuestas_estudiantes.csv")
df_correctas = pd.read_excel("./archivos/respuestas_correctas.xlsx")
# Obtener lista de preguntas
preguntas = df_correctas['Pregunta'].values

# Crear diccionario con respuestas correctas
clave_respuestas = {}
for i in range(df_correctas.shape[0]):
    pregunta = df_correctas['Pregunta'].iloc[i]
    respuesta = df_correctas['Respuesta'].iloc[i]
    clave_respuestas[pregunta] = respuesta

# Inicializar columna de puntuación
df_estudiantes['Puntuación'] = 0

# Calcular puntuación para cada estudiante
for p in preguntas:
    respuesta_correcta = clave_respuestas[p]
    df_estudiantes['Puntuación'] += (df_estudiantes[p] == respuesta_correcta).astype(int)

# Crear copia para reporte detallado
df_detalle = df_estudiantes.copy()

# Marcar respuestas incorrectas con 'X'
for p in preguntas:
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p],
        df_detalle[p] + 'X'
    )

# Ordenar por puntuación
df_detalle = df_detalle.sort_values('Puntuación', ascending=False)
print("Leyenda: RespuestaX = Incorrecta")
print(df_detalle.to_string(index=False))

# Mostrar resultados resumidos
print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
print(df_estudiantes[['Nombre', 'Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))

# Guardar resultados
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en 'resultados_examen.csv'")
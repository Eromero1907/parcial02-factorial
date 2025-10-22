# Parcial 02 – Microservicio Factorial

Este microservicio recibe un **número por URL** y devuelve una **respuesta JSON** con:
- El número recibido  
- Su factorial  
- Una etiqueta `"par"` o `"impar"` según corresponda (evaluando el número recibido)

---

## Ejecución del microservicio

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
python app.py
```

El servicio quedará disponible en:
```
http://127.0.0.1:8000
```

### 3. Probar en el navegador:
```bash
http://127.0.0.1:8000/calc/6
```

**Salida esperada:**
```json
{
  "numero": 6,
  "factorial": 720,
  "etiqueta": "par"
}
```

---

## Análisis

Si este microservicio necesitara comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa, se modificaría de la siguiente forma:

- Se agregaría una comunicación HTTP con el otro servicio para enviar el número, su factorial y la etiqueta.
- La URL del servicio externo se definiría mediante una variable de entorno, evitando dependencias directas entre servicios.
- Si el servicio de historial no está disponible, el microservicio seguiría funcionando normalmente para mantener la disponibilidad.

Esta separación permite mantener un bajo acoplamiento y facilita la escalabilidad de ambos servicios.

---

**Autor:** Esteban Jacob Romero Ríos  
**Fecha:** 22 de Octubre 2025

print("*** Precedencia de operadores ***")
"""
    º1 Operador de paréntesis ()
	º2 Exponente **
 	º3 Unarios +x,-x
	º4 Multiplicación,División,Módulo *,/,//,%
	º5 suma y resta +,-
	º6 Comparación ==,!=,<,<=,>,>=
	º7 Operadores Lógicos not,and y or
	º8 Operadores Asignación =,+=.-=,/=,%=,//=,**=
"""
# Ejemplo de precedencia de operadores
resultado = 12//((3 + 2)* (3-1))
print(f"Resultado: {resultado}")
precedencia = 12 // 3+2*3-1
print(f"\nResultado: {precedencia}")

import sys

def dv(rut):
    value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
    return {10: letter, 11: '0'}.get(value, str(value))


def usage():
    print(f"""Usage: {sys.argv[0]} <rut> [format]
  rut: Rut sin guion ni digito verificador
  format: Formato de salida
    K: Con digito verificador en mayuscula
    .: Con punto
    -: Con guion
  Ejemplo:
    python3 {sys.argv[0]} 40000000
       > 40000000k
    python3 {sys.argv[0]} 11111111 -
       > 11111111-1
    python3 {sys.argv[0]} 11111111 .-
       > 11.111.111-1
    python3 {sys.argv[0]} 40000000 .-K
       > 40.000.000-K
       
Created by Elborikua & Vay3t""")

if len(sys.argv) == 1:
    usage()
    exit()

elif len(sys.argv) > 1:
    rut = sys.argv[1]
    if rut == '-h' or rut == '--help' or rut == '-help' or rut == 'help':
        usage()
        exit()

    elif rut.isdigit():
        formato = sys.argv[2] if len(sys.argv) == 3 else ''
        rut_formatted = f'{int(rut):,}'.replace(',','.') if '.' in formato else rut
        letter = 'K' if 'K' in formato else 'k'
        separator = '-' if '-' in formato else ''
        print(f"{rut_formatted}{separator}{dv(rut)}")

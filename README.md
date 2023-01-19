# dv-gen
Generador de digito verificador para RUT

## Usage
```
$ /bin/python3 dv-gen.py -h
Usage: dv-gen.py <rut> [format]
  rut: Rut sin guion ni digito verificador
  format: Formato de salida
    K: Con digito verificador en mayuscula
    .: Con punto
    -: Con guion
  Ejemplo:
    python3 dv-gen.py 40000000
       > 40000000k
    python3 dv-gen.py 11111111 -
       > 11111111-1
    python3 dv-gen.py 11111111 .-
       > 11.111.111-1
    python3 dv-gen.py 40000000 .-K
       > 40.000.000-K
       
Created by Elborikua & Vay3t
```

## Ejemplos practicos
Diccionario de RUTs

```bash
$ sudo pip3 install exrex
$ seq 1 100 | xargs -I{} bash -c 'exrex -r "1[0-9]{7}"' | xargs -I@ bash -c "python3 dv-gen.py @ .-" > ruts.test
```

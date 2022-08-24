Dê uma olhada no programa a seguir:

```python
volume = 40

def subir_volume(decibeis):
    global volume
    volume += decibeis

def diminuir_volume(decibeis):
    global volume
    volume -= decibeis

def e_volume_saudavel():
    return volume <= 75
```

> Marque as afirmações corretas:

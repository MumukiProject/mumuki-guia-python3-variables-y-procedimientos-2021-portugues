Há momentos em que não queremos, ou simplesmente não faz sentido, que nossas variáveis sejam acessadas por todas as funções. Felizmente, podemos inicializar variáveis diretamente no programa e dentro de um `def`:

```python
def o_mais_longo_sem_espacos(uma_string, outra_string):
  uma_string_sem_espacos = str.strip(uma_string)
  outra_string_sem_espacos = str.strip(outra_string)
 
  if(len(uma_string_sem_espacos) > len(outra_string_sem_espacos)):
	return uma_string_sem_espacos
  else:
	return outra_string_sem_espacos
```

Variáveis inicializadas dentro de um `def`, conhecidas como _variáveis locais_, apresentam pouco mistério. No entanto, você deve ter um cuidado especial com :warning: pois eles só podem ser usados dentro do `def` em questão. Se eu quiser referenciá-lo a partir de um programa ...

```python
pergunta = uma_string_sem_espacos + "?"
```

...¡boom! vai quebrar! :collision:

Entretanto, variáveis inicializadas diretamente no programa, conhecidas como _variáveis globais_, podem ser lidas de qualquer `def`. Por exemplo:

```python
peso_maximo_da_bagagem_em_gramas = 5000

def pode_levar(peso_bagagem):
  return peso_bagagem <= peso_maximo_da_bagagem_em_gramas
````
 
> Como você deve ter notado, nunca nos esquecemos de cumprimentar e agora não é exceção!

> Modifique a função `cumprimentar_a` para evitar a repetição da lógica. Para isso declare e utilize uma variável local `final_do_cumprimento`.

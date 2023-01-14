_Tudo muito interessante até agora, mas por que são chamadas de variáveis se não variam?_ :face_with_raised_eyebrow:

Bem, é que na verdade elas podem variar :sunglasses: . Vamos ver um exemplo:

```python
# inicializamos a variável para que o valor seja 0...
dias_sem_acidentes_com_velociraptores = 0

# ...e mais na frente, vamos atualizá-la
dias_sem_acidentes_com_velociraptores = dias_sem_acidentes_com_velociraptores + 1

# agora vale 1!
dias_sem_acidentes_com_velociraptores
```

No entanto, um cuidado especial deve ser tomado se trabalharmos com variáveis globais: se quisermos modificá-las dentro de uma função, devemos acrescentar `global` antes do nome da variável:

```python
# inicializamos a variável no início do nosso programa
dias_sem_acidentes_com_velociraptores = 0

def passar_um_dia_normal():
  # indicamos a Python que vamos realizar modificações sobre a variável global
  global dias_sem_acidentes_com_velociraptores

  # aqui dentro atualizamos a variável
  dias_sem_acidentes_com_velociraptores = dias_sem_acidentes_com_velociraptores + 1
```

> Teste no console, em ordem, o seguinte:
>
> 1. `dias_sem_acidentes_com_velociraptores`
> 2. `passar_um_dia_normal()`
> 3. `passar_um_dia_normal()`
> 4. `passar_um_dia_normal()`
> 5. `dias_sem_acidentes_com_velociraptores`

> Você pode usar as setas do teclado para navegar entre os comandos executados anteriormente. :arrow_up_small: :arrow_down_small:

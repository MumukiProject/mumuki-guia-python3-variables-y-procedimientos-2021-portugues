Você notou algo diferente sobre a "função" do exercício anterior :mag:? Vejamos novamente a função:

```python
def passar_um_dia_normal():
  global dias_sem_acidentes_com_velociraptores
  dias_sem_acidentes_com_velociraptores = dias_sem_acidentes_com_velociraptores + 1
```

Não tem `return`! Mas não é que todas as funções tem um `return`? :face_with_monocle:

Isso mesmo, é que na verdade `passar_um_dia_normal()` não é uma função, é um _procedimento_! :open_mouth: Embora ambas as funções e procedimentos sejam definidos da mesma maneira e ambos nos ajudem a simplificar nossas tarefas, eles têm algumas diferenças:

* as funções **retornam um valor e não têm efeito**, ou seja, não alteram nossas variáveis;
* os procedimentos **não retornam nada e têm um efeito** quando são invocados.


> Agora que você sabe a diferença, defina um procedimento `aumentar_fortuna` que dobre o valor da variável global `reais_na_minha_carteira`. Não inicialize a variável, porque já fizemos isso para você (com uma quantia secreta de dinheiro :wink:).

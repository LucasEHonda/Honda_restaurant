 # Honda_restaurant
 In this repository I created an API rest with Django for Honda's restaurant.

### Como rodar.
Na pasta /honda_restaurant rode o seguinte comando para rodar a aplicação:
*python manage.py runserver* 

### Recursos.
 Esta API serve para cadastrar e consultar receitas. Toda receita é criada por um chefe. Um usuario comum pode encontrar a receita desejada por nome da receita, ingredientes, modo de preparo, tempo de preparo, pelas receitas de um chefe ou por simplesmente qualquer coisa:
 */recipe/?name=*
 */recipe/?ingredients=*
 */recipe/?prepationMode=*
 */recipe/?prepationTime=*
 */recipe/?cookerName=*
 */recipe/?search=*
 
 respectivamente.
 
 O usuario pode procurar pelos chefes também:
  */cooker/?name=*
  
 Procure pela documentação em:
 */swagger*
 


### Portas.

O programa roda na porta :8000.



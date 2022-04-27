# Status dos testes
![git status](http://3.129.230.99/svg/fernandocfbf/logComp/)

Diagrama sintático:

![image](https://user-images.githubusercontent.com/49531192/165603693-67192747-08b1-48d7-a528-126f7aabc374.png)
![image](https://user-images.githubusercontent.com/49531192/165603989-5598327a-047e-439a-82e4-e31f9b097d9c.png)
![image](https://user-images.githubusercontent.com/49531192/165604004-2291fd73-d887-4990-a5e7-1a997214ff97.png)
![image](https://user-images.githubusercontent.com/49531192/165604018-69d8e5c2-e84c-4664-b35e-f37c9ac914f8.png)
![image](https://user-images.githubusercontent.com/49531192/165604025-0529d940-e28d-430d-bc95-f877cc67c93c.png)



EBNF:

BLOCK = "{", { STATEMENT }, "}" ;

STATEMENT = ( λ | ASSIGNMENT | PRINT), ";" ;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;

PRINT = "printf", "(", EXPRESSION, ")" ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

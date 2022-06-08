# Status dos testes
![git status](http://3.129.230.99/svg/fernandocfbf/logComp/)

Diagrama sintático:

![WhatsApp Image 2022-06-07 at 16 45 45](https://user-images.githubusercontent.com/49531192/172638296-19623f72-499e-44f4-baf1-9c19e827597b.jpeg)
![WhatsApp Image 2022-06-07 at 16 48 27](https://user-images.githubusercontent.com/49531192/172638304-0f2e2299-66b9-44a9-8277-6afa2a6c46b0.jpeg)
![WhatsApp Image 2022-06-07 at 16 48 14](https://user-images.githubusercontent.com/49531192/172638305-cc7d6e0b-199b-4d36-9bef-d7c4d82bd03f.jpeg)
![WhatsApp Image 2022-06-07 at 16 47 56](https://user-images.githubusercontent.com/49531192/172638306-595ca648-46c2-462b-a656-20f16c729a40.jpeg)
![WhatsApp Image 2022-06-07 at 16 47 35](https://user-images.githubusercontent.com/49531192/172638308-2b155959-bd77-4275-8eda-cd35c82d505f.jpeg)
![WhatsApp Image 2022-06-07 at 16 47 16](https://user-images.githubusercontent.com/49531192/172638311-be7ccfb2-b64f-4452-a11f-7a574bd46b81.jpeg)
![WhatsApp Image 2022-06-07 at 16 46 30](https://user-images.githubusercontent.com/49531192/172638314-a566717e-7b9d-43ad-a759-e816e01e2aa2.jpeg)
![WhatsApp Image 2022-06-07 at 16 46 05](https://user-images.githubusercontent.com/49531192/172638316-3303018d-8610-4469-8255-9e7d0fc9a22a.jpeg)

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

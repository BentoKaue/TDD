# Test Driven Development (TDD) – Módulo de Calculadora

Projeto acadêmico desenvolvido no **Instituto Federal do Piauí (IFPI)** com o objetivo de aplicar a metodologia **Test Driven Development (TDD)** no desenvolvimento de software.

## 📌 Sobre o Projeto

Este projeto consiste na criação de um módulo simples de cálculos matemáticos, desenvolvido seguindo rigorosamente o ciclo do TDD:

**Red → Green → Refactor**

* **Red**: escrita de testes automatizados que inicialmente falham
* **Green**: implementação do mínimo de código necessário para os testes passarem
* **Refactor**: melhoria do código mantendo todos os testes funcionando

A abordagem garante código confiável, limpo, testável e de fácil manutenção.

## 🧪 Metodologia Utilizada

O **Test Driven Development (TDD)** prioriza a escrita de testes antes do código de produção. Cada funcionalidade foi validada por testes unitários desde o início do desenvolvimento.

## ⚙️ Funcionalidades Implementadas

O módulo de calculadora possui os seguintes métodos:

* `somar(a, b)` → Retorna a soma de dois números
* `subtrair(a, b)` → Retorna a subtração de dois números
* `multiplicar(a, b)` → Retorna a multiplicação de dois números
* `dividir(a, b)` → Retorna o quociente da divisão (lança exceção ao dividir por zero)
* `isPar(numero)` → Verifica se um número é par
* `validarNumeroPositivo(numero)` → Verifica se o número é positivo (zero é considerado positivo)

## ✅ Testes Unitários

Todos os testes foram escritos **antes** da implementação do código, conforme a metodologia TDD.

### Casos de teste cobertos:

* **Soma**: positivos, positivo com negativo, zeros
* **Subtração**: resultado correto, resultado negativo, valores iguais
* **Multiplicação**: positivos, zero, números negativos
* **Divisão**: divisão válida, divisão por zero, números decimais
* **Paridade**: números pares, ímpares e zero
* **Validação de número positivo**: positivos, negativos e zero

✔️ Todos os testes foram executados com sucesso.

## 🚧 Dificuldades Encontradas

Não foram identificadas dificuldades significativas durante o desenvolvimento. O ciclo do TDD foi seguido de forma direta e objetiva.

A decisão de considerar o **zero como número positivo** foi mantida para garantir consistência com a lógica dos testes e regras matemáticas adotadas.

## 🎯 Benefícios Observados

* Garantia de funcionalidades corretas desde o início
* Redução de erros silenciosos
* Código organizado, modular e fácil de manter
* Maior confiança na implementação
* Aprendizado prático sobre boas práticas de engenharia de software

## 🏁 Conclusão

O projeto demonstrou, na prática, a eficácia do **Test Driven Development (TDD)** no desenvolvimento de software. A escrita de testes antes do código resultou em uma aplicação mais confiável, segura e sustentável, reforçando o TDD como uma prática essencial no desenvolvimento moderno.

## 👨‍💻 Autores

* Antonio Hittalo Ramyres Paulo Rodrigues Macedo
* Bento Kauê de Sousa Lima
* João Manuel da Silva Paulo

## 📍 Instituição

**Instituto Federal do Piauí – IFPI**
Pedro II – PI
2025

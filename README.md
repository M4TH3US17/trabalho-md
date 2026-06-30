<h1>Problema 1 – Soma dos Primeiros Ímpares</h1>

<p><strong>RELATÓRIO TÉCNICO DE VERIFICAÇÃO FORMAL DE ALGORITMOS</strong></p>

<h2>1. Objetivo</h2>

<p>Este trabalho tem como objetivo verificar, por meio de asserções em Python, um algoritmo que calcula a soma dos n primeiros números ímpares positivos. A análise segue estritamente as etapas exigidas no roteiro da atividade: pré-condição, inicialização do invariante, manutenção do invariante, função variante, pós- condição, execução do data set e análise detalhada da falha.</p>

<h2>2. Especificação do Problema</h2>

<p>O programa deve calcular a soma dos primeiros n números ímpares positivos. A propriedade matemática fundamental utilizada é dada por:</p>

<p>[1 + 3 + 5 + … + (2n - 1) = n^2]</p>

<p>Assim, para uma entrada n, o resultado esperado é:</p>

<p>[s = n^2]</p>

<p><strong>Data set de referência fornecido:</strong></p>

<p>[n = 0 → s = 0]</p>

<p>[n = 4 → s = 16]</p>

<p>[n = 10 → s = 100]</p>

<h2>3. Pré-condição</h2>

<p>A pré-condição garante que a entrada seja válida antes do início da execução da função. Neste problema específico, a variável n deve ser um número inteiro maior ou igual a zero:</p>

<p>assert n >= 0, "Erro: Pré-condição violada!"</p>

<p>Essa verificação impede que o algoritmo receba uma quantidade negativa de números ímpares, prevenindo comportamentos indefinidos no laço.</p>

<h2>4. Inicialização do Invariante — Caso Base</h2>

<p>As variáveis internas do algoritmo começam com os seguintes valores:</p>

<p>[s = 0]</p>

<p>[s = i^2 e  0 ≤ i ≤ n]</p>

<p>Logo antes da estrutura de repetição while, verificamos esta condição:</p>

<p>assert s == i*i and 0 <= i <= n, "Erro: Invariante falhou na inicialização!"</p>

<p>Como s = 0 e i = 0, a substituição resulta na igualdade 0 = 0², provando que o caso base é perfeitamente válido.</p>

<h2>5. Manutenção do Invariante — Passo Indutivo</h2>

<p>Durante a execução do laço, o invariante precisa continuar verdadeiro após o término de cada iteração completa. A verificação ocorre no final do corpo do while :</p>

<p>assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"</p>

<p>Isso significa que, após cada atualização das variáveis de controle, a variável s deve representar com precisão matemática a soma dos i primeiros números ímpares.</p>

<h2>6. Função Variante</h2>

<p>A função variante utilizada para demonstrar a terminação do laço foi:</p>

<p>[V(i) = n - i]</p>

<p>Esta função indica quantas iterações teóricas ainda restam para que o laço termine. No início de cada iteração, capturamos o seu valor corrente:</p>

<p>velha_variante = n - i assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"</p>

<p>Ao final da iteração, após as modificações das variáveis, verificamos se o valor decresceu estritamente:</p>

<p>assert (n - i) < velha_variante, "Erro: Loop sem progresso!"</p>

<p>Dessa forma, garante-se matematicamente que o laço avança finitamente em direção ao critério de parada.</p>

<h2>7. Código Original Instrumentado com Erro</h2>

<p>Abaixo apresenta-se o código que contém uma falha estrutural na ordem de atualização de suas variáveis, comprometendo a consistência do invariante:</p>

<pre><code>def sum_of_odds_broken(n: int) -> int:
    # 1. Pré-condição
    assert n >= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0

    # 2. Inicialização do invariante – caso base
    assert s == i*i and 0 <= i <= n, "Erro: Invariante falhou na inicialização!"

    while i < n:
        # 3. Função variante
        velha_variante = n - i
        assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"

        # Erro: i é incrementado antes da soma
        i = i + 1

        # Aqui o invariante é quebrado
        assert s == i*i and 0 <= i <= n, "Erro: Invariante quebrado após incrementar i!"

        # Atualização da soma
        s = s + (2*i - 1)
        # 4. Manutenção do invariante
        assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"

        # 5. Progresso da variante
        assert (n - i) < velha_variante, "Erro: Loop sem progresso!"

    # 6. Pós-condição
    assert s == n*n, "Erro: Pós-condição falhou!"
    return s
</code></pre>

<h2>8. Análise da Falha</h2>

<p>O erro crítico ocorre porque o código incrementa a variável de controle i antes de atualizar a soma acumulada s. Considerando uma execução exemplar com n = 3, os estados evoluem da seguinte forma:</p>

<ul>
<li><strong>Estado Inicial:</strong> i = 0, s = 0. O critério de entrada do laço é satisfeito (0 < 3).</li>
<li><strong>Ao entrar no laço,</strong> executa-se a linha: i = i + 1 , alterando o estado para i = 1 e s = 0.</li>
<li><strong>Imediatamente após,</strong> o programa dispara a verificação: assert s == i*i . Substituindo os valores vigentes, temos:</li>
</ul>

<p>[0 = 1^2 → 0 = 1]</p>

<p>Esta afirmação lógica é falsa. Consequentemente, a execução é interrompida abruptamente lançando a exceção: AssertionError: Error: Invariante quebrado após incrementar i! . A falha expõe que a consistência indutiva foi violada no meio do passo de transição.</p>

<h2>9. Código Corrigido</h2>

<p>Para sanar o problema, a ordem de atualização deve respeitar a lógica de preservação do estado. Primeiro calcula-se o acréscimo na soma baseado no índice atual e, em seguida, avança-se o índice:</p>

<pre><code>def sum_of_odds_correct(n: int) -> int:
    # 1. Pré-condição
    assert n >= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0

    # 2. Inicialização do invariante – caso base
    assert s == i*i and 0 <= i <= n, "Erro: Invariante falhou na inicialização!"

    while i < n:
        # 3. Função variante
        velha_variante = n - i
        assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"

        # Soma o próximo número ímpar com base no índice atual
        s = s + (2*i + 1)
        # Atualiza o contador de iterações
        i = i + 1

        # 4. Manutenção do invariante
        assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"
        # 5. Progresso da variante
        assert (n - i) < velha_variante, "Erro: Loop sem progresso!"

    # 6. Pós-condição
    assert s == n*n, "Erro: Pós-condição falhou!"
    return s
</code></pre>

<h2>10. Teste do Data Set — Código Errado</h2>

<p>Executando a função com falha sum_of_odds_broken(n) para a faixa de valores de teste, os resultados obtidos são os seguintes:</p>

<table>
<tr><th>n</th><th>Resultado da Execução</th><th>Observação</th></tr>
<tr><td>0</td><td>Retorna 0</td><td>O laço não executa pois a condição i &lt; n (0 &lt; 0) é falsa. O bug fica mascarado.</td></tr>
<tr><td>1</td><td>AssertionError</td><td>Invariante quebrado imediatamente após incrementar i na primeira iteração.</td></tr>
<tr><td>2</td><td>AssertionError</td><td>Mesmo comportamento de interrupção por falha de asserção.</td></tr>
<tr><td>3</td><td>AssertionError</td><td>Mesmo comportamento de interrupção por falha de asserção.</td></tr>
<tr><td>4</td><td>AssertionError</td><td>Mesmo comportamento de interrupção por falha de asserção.</td></tr>
<tr><td>10</td><td>AssertionError</td><td>Mesmo comportamento de interrupção por falha de asserção.</td></tr>
</table>

<p><strong>Nota Informativa:</strong> Observa-se que unicamente o caso limite n = 0 não manifesta a falha visível, visto que a guarda do laço impede a execução do bloco interno defectível, ocultando a incorreção da lógica interna estrutural.</p>

<h2>11. Teste do Data Set — Código Correto</h2>

<p>A execução da função corrigida sum_of_odds_correct(n) sobre o conjunto completo de valores produzi resultados em total conformidade com o modelo matemático especificado:</p>

<h2>12. Explicação Textual da Falha</h2>

<p>O AssertionError ocorre sistematicamente na mesma asserção intermediária do código original. O problema reside no desalinhamento do estado das variáveis: o incremento precoce do contador i desfaz a relação quadrática com o acumulador s antes que este possa ser devidamente compensado pelo termo correspondente do somatório.</p>

<p>A inversão aplicada no código corrigido restabelece a ordem lógica correta. Ao realizar o cálculo do termo ímpar como sendo 2i + 1 (utilizando o valor corrente de i) e adicioná-lo à soma antes de efetuar i = i + 1 , garante-se que a igualdade fundamental s = i² permaneça inalterada toda vez que o fluxo de execução atingir as barreiras de checagem do laço.</p>

<h2>13. Pós-condição</h2>

<p>A pós-condição é validada na saída da função:</p>

<p>assert s == n*n, "Error: Pós-condição falhou!"</p>

<h2>14. Conclusão</h2>

<p>Este trabalho demonstrou de maneira prática a relevância e os mecanismos de condução de uma verificação estrutural e formal de software. Evidencia-se que a simples ausência de erros visíveis para entradas específicas (como o caso de n = 0) não é garantia suficiente de correção algorítmica. É indispensável o uso do método indutivo de asserções para blindar o software contra falhas lógicas e garantir consistência em todo o seu domínio de operação, respeitando rigorosamente a pré-condição, inicialização, manutenção, função variante e pós-condição.</p>
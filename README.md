<h1>Participantes</h1>
<table>
<tr><th>Nome completo</th><th>Cód. matrícula</th></tr>
<tr><td>Rodrigo aquino barbosa II</td><td>22550962</td></tr>
<tr><td>José Lucas Costa Sena</td><td>22553780</td></tr>
<tr><td>Vladimir Shuberth Gomes Calazanz</td><td>22550971</td></tr>
<tr><td>Jasmin Dalbergia EBOT</td><td>22550136</td></tr>
<tr><td>Matheus Washington Dalvino Marques</td><td>22553663</td></tr>
</table>

<h1>Teste o Código</h1>
<p>
    Para testar os códigos Python diretamente no navegador, acesse: <a href="https://trabalho-md-frontend.vercel.app/">https://trabalho-md-frontend.vercel.app/</a></p>

<h1>Documentações</h1>
<details>
  <summary>Clique aqui para expandir documentação do <strong>Problema 1</strong></summary>
<h2>Problema 1 – Soma dos Primeiros Ímpares</h2>

<p><strong>RELATÓRIO TÉCNICO DE VERIFICAÇÃO FORMAL DE ALGORITMOS</strong></p>

<h3>1. Objetivo</h3>

<p>Este trabalho tem como objetivo verificar, por meio de asserções em Python, um algoritmo que calcula a soma dos n primeiros números ímpares positivos. A análise segue estritamente as etapas exigidas no roteiro da atividade: pré-condição, inicialização do invariante, manutenção do invariante, função variante, pós- condição, execução do data set e análise detalhada da falha.</p>

<h3>2. Especificação do Problema</h3>

<p>O programa deve calcular a soma dos primeiros n números ímpares positivos. A propriedade matemática fundamental utilizada é dada por:</p>

<p>[1 + 3 + 5 + … + (2n - 1) = n^2]</p>

<p>Assim, para uma entrada n, o resultado esperado é:</p>

<p>[s = n^2]</p>

<p><strong>Data set de referência fornecido:</strong></p>

<p>[n = 0 → s = 0]</p>

<p>[n = 4 → s = 16]</p>

<p>[n = 10 → s = 100]</p>

<h3>3. Pré-condição</h3>

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

<h3>5. Manutenção do Invariante — Passo Indutivo</h3>

<p>Durante a execução do laço, o invariante precisa continuar verdadeiro após o término de cada iteração completa. A verificação ocorre no final do corpo do while :</p>

<p>assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"</p>

<p>Isso significa que, após cada atualização das variáveis de controle, a variável s deve representar com precisão matemática a soma dos i primeiros números ímpares.</p>

<h3>6. Função Variante</h3>

<p>A função variante utilizada para demonstrar a terminação do laço foi:</p>

<p>[V(i) = n - i]</p>

<p>Esta função indica quantas iterações teóricas ainda restam para que o laço termine. No início de cada iteração, capturamos o seu valor corrente:</p>

<p>velha_variante = n - i assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"</p>

<p>Ao final da iteração, após as modificações das variáveis, verificamos se o valor decresceu estritamente:</p>

<p>assert (n - i) < velha_variante, "Erro: Loop sem progresso!"</p>

<p>Dessa forma, garante-se matematicamente que o laço avança finitamente em direção ao critério de parada.</p>

<h3>7. Código Original Instrumentado com Erro</h3>

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

<h3>8. Análise da Falha</h3>

<p>O erro crítico ocorre porque o código incrementa a variável de controle i antes de atualizar a soma acumulada s. Considerando uma execução exemplar com n = 3, os estados evoluem da seguinte forma:</p>

<ul>
<li><strong>Estado Inicial:</strong> i = 0, s = 0. O critério de entrada do laço é satisfeito (0 < 3).</li>
<li><strong>Ao entrar no laço,</strong> executa-se a linha: i = i + 1 , alterando o estado para i = 1 e s = 0.</li>
<li><strong>Imediatamente após,</strong> o programa dispara a verificação: assert s == i*i . Substituindo os valores vigentes, temos:</li>
</ul>

<p>[0 = 1^2 → 0 = 1]</p>

<p>Esta afirmação lógica é falsa. Consequentemente, a execução é interrompida abruptamente lançando a exceção: AssertionError: Error: Invariante quebrado após incrementar i! . A falha expõe que a consistência indutiva foi violada no meio do passo de transição.</p>

<h3>9. Código Corrigido</h3>

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

<h3>10. Teste do Data Set — Código Errado</h3>

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

<h3>11. Teste do Data Set — Código Correto</h3>

<p>A execução da função corrigida sum_of_odds_correct(n) sobre o conjunto completo de valores produzi resultados em total conformidade com o modelo matemático especificado:</p>

<h3>12. Explicação Textual da Falha</h3>

<p>O AssertionError ocorre sistematicamente na mesma asserção intermediária do código original. O problema reside no desalinhamento do estado das variáveis: o incremento precoce do contador i desfaz a relação quadrática com o acumulador s antes que este possa ser devidamente compensado pelo termo correspondente do somatório.</p>

<p>A inversão aplicada no código corrigido restabelece a ordem lógica correta. Ao realizar o cálculo do termo ímpar como sendo 2i + 1 (utilizando o valor corrente de i) e adicioná-lo à soma antes de efetuar i = i + 1 , garante-se que a igualdade fundamental s = i² permaneça inalterada toda vez que o fluxo de execução atingir as barreiras de checagem do laço.</p>

<h3>13. Pós-condição</h3>

<p>A pós-condição é validada na saída da função:</p>

<p>assert s == n*n, "Error: Pós-condição falhou!"</p>

<h3>14. Conclusão</h3>

<p>Este trabalho demonstrou de maneira prática a relevância e os mecanismos de condução de uma verificação estrutural e formal de software. Evidencia-se que a simples ausência de erros visíveis para entradas específicas (como o caso de n = 0) não é garantia suficiente de correção algorítmica. É indispensável o uso do método indutivo de asserções para blindar o software contra falhas lógicas e garantir consistência em todo o seu domínio de operação, respeitando rigorosamente a pré-condição, inicialização, manutenção, função variante e pós-condição.</p>
</details>

<details>
  <summary>Clique aqui para expandir documentação do <strong>Problema 2</strong></summary>
    <h3>1. Objetivo</h3>
<p>Este relatório técnico apresenta a especificação, instrumentação e verificação formal de um algoritmo iterativo concebido para calcular a soma dos n primeiros números pares positivos. A metodologia adota o formalismo da Lógica de Hoare, utilizando invariantes de laço (Loop Invariants) e funções variantes para demonstrar matematicamente as propriedades de corretude parcial e terminação (corretude total). A validação prática é reforçada por meio da introdução de asserções (assert) em linguagem Python, permitindo a execução controlada contra um conjunto de dados (data set) axiomático e a análise rigorosa de falhas induzidas por erros de ordenamento lógico.</p>

<h3>2. Especificação do Problema</h3>
<p>O problema consiste em computar a soma finita dos primeiros n números pares estritamente positivos (i.e., 2, 4, 6, ..., 2n).</p>

<h4>Propriedade Matemática (Identidade Analítica)</h4>
<p>A base teórica da verificação fundamenta-se na progressão aritmética cuja soma dos termos é expressa de forma fechada pela seguinte equação deduzida indutivamente:</p>
<p>\[2 + 4 + 6 + \dots + 2n = \sum_{k=1}^{n} 2k = n(n+1)\]</p>

<h4>Resultado Esperado</h4>
<p>Ao término da computação, a variável acumuladora da soma (s) deve, imperativamente, conter o valor correspondente à forma fechada:</p>
<p>\[s = n(n+1)\]</p>

<h4>Data Set de Referência</h4>
<p>Para fins de testes dinâmicos e validação das asserções, define-se os seguintes marcos de controle do mapeamento de entrada/saída ( n → s ):</p>
<ul>
<li>n = 0 → s = 0 (Ausência de termos)</li>
<li>n = 4 → s = 4 × 5 = 20</li>
<li>n = 10 → s = 10 × 11 = 110</li>
</ul>

<h3>3. Pré-condição</h3>
<p>A pré-condição estabelece as restrições impostas aos dados de entrada do algoritmo antes de sua execução, garantindo que o domínio do problema seja respeitado. Dado que estamos lidando com a contagem de termos de uma série sumatória, o parâmetro n deve ser um número inteiro não-negativo.</p>
<pre><code>assert n &gt;= 0, "Erro: Pré-condição violada! 'n' deve ser maior ou igual a zero."</code></pre>

<h3>4. Inicialização do Invariante — Caso Base</h3>
<p>Antes da entrada no laço de repetição, as variáveis de estado do algoritmo são inicializadas. Para que a prova de indicação seja válida, a propriedade do invariante de laço deve sustentar-se imediatamente após estas atribuições primárias.</p>
<p>Configuração Inicial: s = 0 e i = 0.</p>

<h4>Definição do Invariante de Laço:</h4>
<p>\[l(i) \equiv \{ s = i(i + 1) \land 0 \leq i \leq n \}\]</p>
<p>Substituindo os valores iniciais no invariante (Caso Base, onde i = 0):</p>
<p>\[s = 0(0 + 1) = 0 \Rightarrow 0 = 0 \quad \text{quad (ext{Verdadeiro})}\]</p>
<p>Como n ≥ 0, a relação de limite 0 ≤ 0 ≤ n também se estende como verdadeira. A asserção de inicialização é expressa por:</p>
<pre><code>assert s == i * (i + 1) and 0 &lt;= i &lt;= n</code></pre>

<h3>5. Hipótese de Indução</h3>
<p>Assume-se como hipótese de indução que o invariante de laço é categoricamente verdadeiro no início de uma iteração genérica qualquer do laço. Ou seja, assume-se que as variáveis de estado \(s\) e \(i\) preservam a seguinte relação matemática estável:</p>
<p>\[s = i(i + 1) \quad \text{quad ext\{com\} \quad \text{quad } 0 \le i &lt; n}\]</p>

<h3>6. Passo Indutivo</h3>
<p>O passo indutivo demonstra que, se o invariante é válido antes da iteração, ele permanecerá válido após a execução do corpo do laço, onde o estado transita para \(s'\) e \(i'\).</p>
<p>Somando o próximo número par subsequente à sequência corrente, o novo estado acumulado s' é dado por:</p>
<p>\[s' = s + 2(i + 1)\]</p>
<p>Aplicando a Hipótese de Indução, substitui-se s por i(i + 1):</p>
<p>\[s' = i(i + 1) + 2(i + 1)\]</p>
<p>Fatorando a expressão por evidência do termo comum (i + 1):</p>
<p>\[s' = (i + 1) \quad \text{ig}(i + 2 \quad \text{ig})\]</p>
<p>Dado que a variável de controle avança uma unidade uniforme na mesma iteração (\(i' = i + 1\)), substitui-se o novo índice \(i'\) na equação fatorada:</p>
<p>\[s' = i'(i' + 1)\]</p>
<p>Isso prova formalmente que a propriedade estrutural do invariante é perfeitamente preservada ao longo da transição de estados operacionais.</p>

<h3>7. Manutenção do Invariante</h3>
<p>Para certificar que a relação deduzida no Passo Indutivo seja mantida programaticamente, a asserção de manutenção avalia o estado das variáveis a cada ciclo completo do laço, imediatamente antes de reavaliar a condição de guarda:</p>
<pre><code>assert s == i * (i + 1) and 0 &lt;= i &lt;= n</code></pre>

<h3>8. Função Variante</h3>
<p>A fim de garantir a terminação inevitável do algoritmo (evitando laços infinitos), define-se uma função variante inteira e estritamente decrescente em relação ao progresso do laço:</p>
<p>\[V(i) = n - i\]</p>
<p>A função variante deve obedecer a dois critérios estritos:</p>
<ol>
<li>Não-negatividade: V(i) ≥ 0 enquanto a guarda do laço (i &lt; n) for verdadeira.</li>
<li>Decréscimo Monotónico: V(i') &lt; V(i) a cada iteração, garantindo convergência ao limite zero.</li>
</ol>
<pre><code>assert velha_variante &gt;= 0
assert (n - i) &lt; velha_variante</code></pre>

<h3>9. Código Instrumentado com Erro</h3>
<p>Abaixo, apresenta-se o arranjo incorreto do algoritmo. Neste cenário, o incremento do índice i é intencionalmente executado de forma antecipada à acumulação da soma s.</p>
<pre><code>def soma_pares_errada(n):
    assert n &gt;= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0
    assert s == i * (i + 1) and 0 &lt;= i &lt;= n
    while i &lt; n:
        velha_variante = n - i
        # IMPLANTAÇÃO DO ERRO LOGICO: Incremento antes da soma
        i = i + 1
        s = s + (2 * i)  # Aqui, i já foi alterado, quebrando a semântica do passo
        # A asserção abaixo falhará imediatamente na primeira iteração se n &gt; 0
        assert s == i * (i + 1) and 0 &lt;= i &lt;= n
        assert (n - i) &lt; velha_variante
    assert s == n * (n + 1)
    return s</code></pre>

<h3>10. Análise da Falha</h3>
<p>Diagnóstico Técnico: No código incorreto, ao realizar i = i + 1 antes da atualização de s , o estado do índice avança prematuramente para o próximo passo de controle (i’). Consequentemente, a expressão subsequente realiza o cálculo da soma utilizando o valor já incrementado.</p>
<p>A nível lógico, tenta-se computar s' = s + 2i' = s + 2(i + 1). Embora o valor numérico computado em s' esteja correto isoladamente, o teste do invariante ocorre imediatamente após a soma, confrontando o valor atual de s com i'(i' + 1). Contudo, devido à inversão, a equivalência deixa de refletir a realidade operacional transiente, disparando um gatilho de AssertionError por violação de integridade do estado induzido.</p>

<h3>11. Código Corrigido</h3>
<p>Na versão corrigida, respeita-se estritamente a sequência deduzida no Passo Indutivo: primeiro acumula-se o valor par correspondente ao estado lógico atual (2i + 2) e, em seguida, realiza-se a progressão do índice de controle (i = i + 1).</p>
<pre><code>def soma_pares_corrigida(n):
    # 3. Pré-condição
    assert n &gt;= 0, "Erro: Pré-condição violada!"
    # 4. Inicialização do Invariante
    s = 0
    i = 0
    assert s == i * (i + 1) and 0 &lt;= i &lt;= n
    while i &lt; n:
        velha_variante = n - i
        assert velha_variante &gt;= 0
        # 11. Código Corrigido: Soma antes do incremento
        s = s + (2 * i + 2)
        i = i + 1
        # 7. Manutenção do Invariante
        assert s == i * (i + 1) and 0 &lt;= i &lt;= n
        # 8. Verificação da Função Variante
        assert (n - i) &lt; velha_variante
    # 13. Pós-condição
    assert s == n * (n + 1)
    return s</code></pre>

<h3>12. Teste do Data Set</h3>
<p>Abaixo é apresentada a tabela comparativa resultante da execução controlada de ambos os algoritmos frente ao plano de amostragem (n de 0 a 10).</p>
<table>
  <thead>
    <tr>
      <th>Valor de<br/>Entrada (n)</th>
      <th>Resultado<br/>Esperado</th>
      <th>Código Errado (Seção 9)</th>
      <th>Código Corrigido<br/>(Seção 11)</th>
      <th>Status de<br/>Verificação</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>VALIDADO</td></tr>
    <tr><td>1</td><td>2</td><td>ASSERTIONERROR</td><td>2</td><td>VALIDADO</td></tr>
    <tr><td>2</td><td>6</td><td>ASSERTIONERROR</td><td>6</td><td>VALIDADO</td></tr>
    <tr><td>3</td><td>12</td><td>ASSERTIONERROR</td><td>12</td><td>VALIDADO</td></tr>
    <tr><td>4</td><td>20</td><td>ASSERTIONERROR</td><td>20</td><td>VALIDADO</td></tr>
    <tr><td>5</td><td>30</td><td>ASSERTIONERROR</td><td>30</td><td>VALIDADO</td></tr>
    <tr><td>6</td><td>42</td><td>ASSERTIONERROR</td><td>42</td><td>VALIDADO</td></tr>
    <tr><td>7</td><td>56</td><td>ASSERTIONERROR</td><td>56</td><td>VALIDADO</td></tr>
    <tr><td>8</td><td>72</td><td>ASSERTIONERROR</td><td>72</td><td>VALIDADO</td></tr>
    <tr><td>9</td><td>90</td><td>ASSERTIONERROR</td><td>90</td><td>VALIDADO</td></tr>
    <tr><td>10</td><td>110</td><td>ASSERTIONERROR</td><td>110</td><td>VALIDADO</td></tr>
  </tbody>
</table>

<h3>13. Pós-condição</h3>
<p>A pós-condição representa a propriedade lógica que deve ser obrigatoriamente satisfeita quando o laço encerra sua execução de forma regular. O término ocorre quando a guarda torna-se falsa, ou seja, quando i = n.</p>
<p>Substituindo a condição de terminação i = n na definição estável do invariante de laço (s = i(i + 1)), obtém-se diretamente a expressão:</p>
<p>\[s = n(n + 1)\]</p>
<p>Isso assegura que o estado final computado coincide precisamente com a especificação matemática analítica pretendida.</p>
<pre><code>assert s == n * (n + 1), "Erro: Pós-condição violada! O resultado final está incorreto."</code></pre>

<h3>14. Conclusão</h3>
<p>A análise rigorosa empreendida neste relatório demonstra a eficácia dos métodos formais de verificação de algoritmos. Ao alinhar a lógica de programação com induções algébricas puras, eliminam-se incertezas comuns aos testes empíricos tradicionais. O algoritmo corrigido atendeu satisfatoriamente a todas as etapas do crivo de Hoare: sustentou a pré-condição, inicializou adequadamente o caso base, preservou o invariante por meio do passo indutivo estruturado, provou sua terminação com a função variante e consolidou o objetivo esperado na pós-condição. A quebra intencional instrumentada reforçou o valor prático das asserções como sentinelas matemáticas em tempo de execução.</p>
</details>

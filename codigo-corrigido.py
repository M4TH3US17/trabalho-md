def sum_of_odds_correct(n: int) -> int:
 # 1. Pré-condição
 assert n >= 0, "Erro: Pré-condição violada!"
 s = 0
 i = 0
 # 2. Inicialização do invariante — caso base
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

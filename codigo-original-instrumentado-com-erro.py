def sum_of_odds_broken(n: int) -> int:
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
 # Erro: i é incrementado antes da soma
 i = i + 1
 # Aqui o invariante é quebrado
 assert s == i*i and 0 <= i <= n, "Erro: Invariante quebrado após incrementar
i!"
 # Atualização da soma
 s = s + (2*i - 1)
 # 4. Manutenção do invariante
 assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"
 # 5. Progresso da variante
 assert (n - i) < velha_variante, "Erro: Loop sem progresso!"
 # 6. Pós-condição
 assert s == n*n, "Erro: Pós-condição falhou!"
 return s
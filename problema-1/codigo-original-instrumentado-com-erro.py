# @author: Jasmin Dalbergia EBOT
# @date: 2026-06-27

def sum_of_odds_broken(n: int) -> int:
    """
        Calcula a soma dos n primeiros números ímpares positivos.

        Versão instrumentada com asserções de verificação formal. Contém um erro
        intencional: o contador i é incrementado antes da atualização da soma s,
        o que viola o invariante do laço para n > 0.
    """
    assert n >= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0
    assert s == i*i and 0 <= i <= n, "Erro: Invariante falhou na inicialização!"
    while i < n:
        velha_variante = n - i
        assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"
        i = i + 1
        assert s == i*i and 0 <= i <= n, "Erro: Invariante quebrado após incrementar i!"
        s = s + (2*i - 1)
        assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"
        assert (n - i) < velha_variante, "Erro: Loop sem progresso!"
    assert s == n*n, "Erro: Pós-condição falhou!"
    return s


if __name__ == "__main__":
    for n in [0, 1, 3, 5]:
        try:
            print(f"n={n} => {sum_of_odds_broken(n)}")
        except AssertionError as e:
            print(f"n={n} => ERRO: {e}")


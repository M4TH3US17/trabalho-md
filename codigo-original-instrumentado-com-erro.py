# @author: Jasmin Dalbergia EBOT
# @date: 2026-06-27


def sum_of_odds_broken(n: int) -> int:
    """
        Calcula a soma dos n primeiros números ímpares positivos.

        Versão instrumentada com asserções de verificação formal. Contém um erro
        intencional: o contador i é incrementado antes da atualização da soma s,
        o que viola o invariante do laço para n > 0.

        @param n: Quantidade de termos ímpares a somar (inteiro não negativo).
        @returns: Soma dos n primeiros ímpares positivos (n^2), se todas as asserções forem satisfeitas.
        @raises AssertionError: Se a pré-condição, o invariante, a função variante ou a pós-condição forem violados durante a execução.
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

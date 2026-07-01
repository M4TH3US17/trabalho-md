# @author: Jasmin Dalbergia EBOT
# @date: 2026-06-27


def sum_of_odds_correct(n: int) -> int:
    """
        Calcula a soma dos n primeiros números ímpares positivos.

        Versão corrigida e instrumentada com asserções de verificação formal.
        A soma é atualizada antes do incremento de i, preservando o invariante
        s = i² em todas as iterações do laço.
    """
    assert n >= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0
    assert s == i*i and 0 <= i <= n, "Erro: Invariante falhou na inicialização!"
    while i < n:
        velha_variante = n - i
        assert velha_variante >= 0, "Erro: Variante violou o limite inferior!"
        s = s + (2*i + 1)
        i = i + 1
        assert s == i*i and 0 <= i <= n, "Erro: Invariante violado no corpo do loop!"
        assert (n - i) < velha_variante, "Erro: Loop sem progresso!"
    assert s == n*n, "Erro: Pós-condição falhou!"
    return s


if __name__ == "__main__":
    for n in [0, 1, 3, 5]:
        print(f"n={n} => {sum_of_odds_correct(n)}")

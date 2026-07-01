# @author: Matheus Washington Dalvino Marques
# @date: 2026-06-30

def soma_pares_corrigida(n):
    assert n >= 0, "Erro: Pré-condição violada!"
    s = 0
    i = 0
    assert s == i * (i + 1) and 0 <= i <= n

    while i < n:
        velha_variante = n - i
        assert velha_variante >= 0
        s = s + (2 * i + 2)
        i = i + 1
        assert s == i * (i + 1) and 0 <= i <= n
        assert (n - i) < velha_variante
    assert s == n * (n + 1), "Erro: Pós-condição violada!"
    return s


if __name__ == "__main__":
    for n in [0, 1, 4, 10]:
        print(f"n={n} => {soma_pares_corrigida(n)}")

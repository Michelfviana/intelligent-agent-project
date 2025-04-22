from pyswip import Prolog


class AgenteEscolhaLocalAvancado:
    def __init__(self, clima="chuvoso", horario="tarde"):
        self.prolog = Prolog()
        print("Carregando regras...")
        self.prolog.consult("regras.pl")
        print("Regras carregadas com sucesso.")
        self.clima = clima
        self.horario = horario

    def locais_adequados(self):
        query = f"adequado(Lugar, {self.clima}, {self.horario})"
        print(f"Consultando: {query}")
        resultados = list(self.prolog.query(query))
        print(f"Resultados encontrados: {resultados}")
        return [r["Lugar"] for r in resultados]

    def avaliar_pontuacao(self, locais):
        locais_pontuados = []
        for lugar in locais:
            query = f"pontuacao({lugar}, P)"
            resultado = list(self.prolog.query(query))
            if resultado:
                locais_pontuados.append((lugar, resultado[0]["P"]))
        return sorted(locais_pontuados, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    agente = AgenteEscolhaLocalAvancado(clima="chuvoso", horario="tarde")
    locais = agente.locais_adequados()

    if locais:
        print("\nLocais adequados com pontuação:")
        pontuados = agente.avaliar_pontuacao(locais)
        for lugar, pontos in pontuados:
            print(f"- {lugar} (Pontuação: {pontos})")
    else:
        print("Nenhum local adequado foi encontrado.")

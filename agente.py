from pyswip import Prolog

class AgenteEscolhaLocal:
    def __init__(self, clima="chuvoso", horario="tarde"):
        self.prolog = Prolog()
        print("Carregando regras...")
        self.prolog.consult("regras.pl")  # Carrega as regras em Prolog
        print("Regras carregadas.")
        self.clima = clima
        self.horario = horario

    def locais_adequados(self):
        # Faz a consulta no Prolog para obter locais adequados
        query = f"adequado(Lugar, {self.clima}, {self.horario})"
        print(f"Consultando: {query}")
        resultados = list(self.prolog.query(query))
        return [r["Lugar"] for r in resultados]

    def avaliar_pontuacao(self, locais):
        locais_pontuados = []
        for lugar in locais:
            query = f"pontuacao({lugar}, P)"
            resultado = list(self.prolog.query(query))
            if resultado:
                locais_pontuados.append((lugar, resultado[0]["P"]))
        # Ordena os locais pela pontuação (maior para menor)
        locais_pontuados.sort(key=lambda x: x[1], reverse=True)
        return locais_pontuados

# Execução do programa
if __name__ == "__main__":
    # Pergunta ao usuário o clima e o horário
    clima = input("Digite o clima (ensolarado ou chuvoso): ").strip().lower()
    horario = input("Digite o horário (manha, tarde, noite ou qualquer): ").strip().lower()

    # Valida as entradas
    if clima not in ["ensolarado", "chuvoso"]:
        print("Clima inválido! O clima deve ser 'ensolarado' ou 'chuvoso'.")
    elif horario not in ["manha", "tarde", "noite", "qualquer"]:
        print("Horário inválido! O horário deve ser 'manha', 'tarde', 'noite' ou 'qualquer'.")
    else:
        agente = AgenteEscolhaLocal(clima=clima, horario=horario)
        locais = agente.locais_adequados()

        if locais:
            print("\nLocais adequados com pontuação:")
            pontuados = agente.avaliar_pontuacao(locais)
            for lugar, pontos in pontuados:
                print(f"- {lugar} (Pontuação: {pontos})")
        else:
            print("Nenhum local adequado foi encontrado.")

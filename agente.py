from pyswip import Prolog  # Importa a biblioteca pyswip para interagir com Prolog

# Classe que representa o agente inteligente para escolha de locais
class AgenteEscolhaLocal:
    def __init__(self, clima="chuvoso", horario="tarde"):
        """
        Inicializa o agente com o clima e horário fornecidos.
        Também carrega as regras Prolog do arquivo 'regras.pl'.
        """
        self.prolog = Prolog()  # Cria uma instância do Prolog
        print("Carregando regras...")
        self.prolog.consult("regras.pl")  # Carrega as regras definidas no arquivo Prolog
        print("Regras carregadas.")
        self.clima = clima  # Define o clima atual
        self.horario = horario  # Define o horário atual

    def locais_adequados(self):
        """
        Consulta o Prolog para obter os locais adequados com base no clima e horário.
        Retorna uma lista de locais.
        """
        # Monta a consulta Prolog para verificar locais adequados
        query = f"adequado(Lugar, {self.clima}, {self.horario})"
        print(f"Consultando: {query}")
        # Executa a consulta no Prolog e converte os resultados em uma lista
        resultados = list(self.prolog.query(query))
        # Extrai os nomes dos locais dos resultados
        return [r["Lugar"] for r in resultados]

    def avaliar_pontuacao(self, locais):
        """
        Avalia a pontuação dos locais fornecidos consultando o Prolog.
        Retorna uma lista de tuplas (local, pontuação), ordenada pela pontuação (maior para menor).
        """
        locais_pontuados = []  # Lista para armazenar os locais com suas pontuações
        for lugar in locais:
            # Monta a consulta Prolog para obter a pontuação do local
            query = f"pontuacao({lugar}, P)"
            # Executa a consulta no Prolog
            resultado = list(self.prolog.query(query))
            if resultado:
                # Adiciona o local e sua pontuação à lista
                locais_pontuados.append((lugar, resultado[0]["P"]))
        # Ordena os locais pela pontuação em ordem decrescente
        locais_pontuados.sort(key=lambda x: x[1], reverse=True)
        return locais_pontuados

# Execução do programa principal
if __name__ == "__main__":
    # Solicita ao usuário o clima e o horário
    clima = input("Digite o clima (ensolarado ou chuvoso): ").strip().lower()
    horario = input("Digite o horário (manha, tarde, noite ou qualquer): ").strip().lower()

    # Valida as entradas do usuário
    if clima not in ["ensolarado", "chuvoso"]:
        print("Clima inválido! O clima deve ser 'ensolarado' ou 'chuvoso'.")
    elif horario not in ["manha", "tarde", "noite", "qualquer"]:
        print("Horário inválido! O horário deve ser 'manha', 'tarde', 'noite' ou 'qualquer'.")
    else:
        # Cria uma instância do agente com os parâmetros fornecidos
        agente = AgenteEscolhaLocal(clima=clima, horario=horario)
        # Obtém os locais adequados
        locais = agente.locais_adequados()

        if locais:
            print("\nLocais adequados com pontuação:")
            # Avalia a pontuação dos locais adequados
            pontuados = agente.avaliar_pontuacao(locais)
            # Exibe os locais e suas pontuações
            for lugar, pontos in pontuados:
                print(f"- {lugar} (Pontuação: {pontos})")
        else:
            # Caso nenhum local seja encontrado
            print("Nenhum local adequado foi encontrado.")

% --- Fatos: locais
lugar(biblioteca).
lugar(cafe).
lugar(sala_estudo).
lugar(apartamento_amigo).

% --- Fatos: características
silencioso(biblioteca).
silencioso(sala_estudo).
barulhento(cafe).
barulhento(apartamento_amigo).

tem_wifi(biblioteca).
tem_wifi(cafe).
tem_wifi(apartamento_amigo).

espacoso(biblioteca).
espacoso(sala_estudo).
apertado(cafe).
apertado(apartamento_amigo).

proximo(sala_estudo).
proximo(apartamento_amigo).
longe(biblioteca).
longe(cafe).

horario_funcionamento(biblioteca, manha).
horario_funcionamento(cafe, tarde).
horario_funcionamento(sala_estudo, noite).
horario_funcionamento(apartamento_amigo, qualquer).

ambiente_fechado(biblioteca).
ambiente_fechado(cafe).
ambiente_fechado(sala_estudo).
ambiente_aberto(apartamento_amigo).

% --- Regra de adequação com suporte a clima e horário
adequado(Lugar, Clima, Horario) :-
    lugar(Lugar),
    silencioso(Lugar),
    tem_wifi(Lugar),
    espacoso(Lugar),
    proximo(Lugar),
    (
        horario_funcionamento(Lugar, Horario);
        horario_funcionamento(Lugar, qualquer)
    ),
    (
        Clima = ensolarado;
        (Clima = chuvoso, ambiente_fechado(Lugar))
    ).

% --- Regra de pontuação com pesos e correção de variáveis singleton
pontuacao(Lugar, P) :-
    lugar(Lugar),
    (silencioso(Lugar) -> S = 3 ; S = 0),
    (tem_wifi(Lugar)   -> W = 2 ; W = 0),
    (espacoso(Lugar)   -> E = 2 ; E = 0),
    (proximo(Lugar)    -> D = 2 ; D = 0),
    P is S + W + E + D.

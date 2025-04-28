% Fatos: locais
lugar(biblioteca).
lugar(cafe).
lugar(sala_estudo).
lugar(apartamento_amigo).

% Características dos locais
silencioso(biblioteca).
silencioso(sala_estudo).
barulhento(cafe).
barulhento(apartamento_amigo).

tem_wifi(biblioteca).
tem_wifi(cafe).
tem_wifi(apartamento_amigo).

espacoso(biblioteca).
espacoso(apartamento_amigo).

apertado(sala_estudo).
apertado(cafe).

proximo(sala_estudo).
proximo(apartamento_amigo).
longe(biblioteca).
longe(cafe).

horario_funcionamento(biblioteca, noite).
horario_funcionamento(cafe, manha).
horario_funcionamento(sala_estudo, noite).
horario_funcionamento(apartamento_amigo, qualquer).

% Regras auxiliares para clima
adequado_clima(Lugar, ensolarado) :- lugar(Lugar).
adequado_clima(Lugar, chuvoso) :-
    lugar(Lugar),
    (silencioso(Lugar); tem_wifi(Lugar)).

% Regra de horário flexível
adequado_horario(Lugar, qualquer) :- lugar(Lugar).
adequado_horario(Lugar, Horario) :-
    lugar(Lugar),
    (horario_funcionamento(Lugar, Horario);
     horario_funcionamento(Lugar, qualquer)).

% Regra principal de adequação
adequado(Lugar, Clima, Horario) :-
    lugar(Lugar),
    tem_wifi(Lugar),
    adequado_clima(Lugar, Clima),
    adequado_horario(Lugar, Horario).

% Regra de pontuação mais refinada
pontuacao(Lugar, P) :-
    lugar(Lugar),
    (silencioso(Lugar) -> S = 4 ; S = 0),
    (tem_wifi(Lugar)   -> W = 3 ; W = 0),
    (espacoso(Lugar)   -> E = 2 ; E = 0),
    (proximo(Lugar)    -> D = 2 ; D = 0),
    (horario_funcionamento(Lugar, qualquer) -> H = 1 ; H = 0),
    P is S + W + E + D + H.

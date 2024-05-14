c_to_f(C,F):- F is C*9/5+32, write(F).

func(F):- F < 32, write('Below Freezing Point').

func(F):- F>=32, write('Above Freezing Point').
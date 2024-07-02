from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Arithmetic Progression (AP) with common difference d = my_int2 - my_int1
    d = my_int2 - my_int1
    ap_term1 = my_int1
    ap_term2 = my_int1 + d
    ap_term3 = my_int1 + Integer(2) * d

    # Geometric Progression (GP) with common ratio r = my_int2 / my_int1
    r = my_int2 / my_int1
    gp_term1 = my_int1
    gp_term2 = my_int1 * r
    gp_term3 = my_int1 * r * r

    # Harmonic Progression (HP) terms are reciprocals of AP terms
    hp_term1 = Integer(1) / my_int1
    hp_term2 = Integer(1) / ap_term2
    hp_term3 = Integer(1) / ap_term3

    return [
        # Output AP terms
        Output(ap_term1, "ap_term1", party1),
        Output(ap_term2, "ap_term2", party1),
        Output(ap_term3, "ap_term3", party1),
        
        # Output GP terms
        Output(gp_term1, "gp_term1", party1),
        Output(gp_term2, "gp_term2", party1),
        Output(gp_term3, "gp_term3", party1),

        # Output HP terms
        Output(hp_term1, "hp_term1", party1),
        Output(hp_term2, "hp_term2", party1),
        Output(hp_term3, "hp_term3", party1)
    ]

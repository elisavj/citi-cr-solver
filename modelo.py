from pulp import *

def resolver_citi(analistas=12, min_swift=4, min_cartas=2, cap_min=15):
    """Resuelve el LP de asignacion de analistas de Citi CR"""
    modelo = LpProblem('Citi_CR', LpMinimize)

    # Variables de decision
    x1 = LpVariable('SWIFT',      lowBound=0)  # analistas SWIFT
    x2 = LpVariable('CarCred',    lowBound=0)  # cartas de credito
    x3 = LpVariable('Garantias',  lowBound=0)  # garantias

    # Funcion objetivo: Min Z = 3x1 + 5x2 + 4x3
    modelo += 3*x1 + 5*x2 + 4*x3

    # Restricciones
    modelo += x1+x2+x3   <= analistas,  'total_analistas'
    modelo += x1         >= min_swift,   'min_SWIFT'
    modelo += x2         >= min_cartas,  'min_cartas'
    modelo += 2*x1+x2+x3 >= cap_min,     'capacidad'

    modelo.solve(PULP_CBC_CMD(msg=0))

    return x1.varValue, x2.varValue, x3.varValue, value(modelo.objective)

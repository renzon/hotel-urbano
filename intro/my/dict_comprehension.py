states = {"RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "SP": "São Paulo"}
print(states)

r_states = {k: v for k, v in states.items() if k.startswith("R")}
print(r_states)

def remove_mascara(cpf):
  return cpf.replace(".", "").replace("-", "")


def calcula_dv(cpf):
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (10 - i)
  dv1 = 11 - (soma % 11)
  if dv1 > 9:
    dv1 = 0
  
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (11 - i)
  soma += dv1 * 2
  dv2 = 11 - (soma % 11)
  if dv2 > 9:
    dv2 = 0
  
  return dv1, dv2


def verifica_cpf(cpf):
  cpf = remove_mascara(cpf)
  if len(cpf) != 11:
    return False
  dv1, dv2 = calcula_dv(cpf)
  return dv1 == int(cpf[9]) and dv2 == int(cpf[10])
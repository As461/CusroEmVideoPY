vls = float(input('Digite o valor do seu salario: '.replace(".", ",")))
vla = vls * 0.15
s = vls + vla

print(str('O seu salário com aumento é: R$ {:.2f}'.format(s) .replace(".", ",")))
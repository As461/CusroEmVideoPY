vlp = float(input('Digite o valor do produto sem o desconto: R$ '.replace(".", ",")))
vld = vlp - (vlp * 5 / 100)
print(str('O valor com desconto é: R$ {:.2f}'.format(vld) .replace(".", ",")))
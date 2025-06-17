cpf = input("Digite o CPF (somente números): ")

if not cpf.isdigit() or len(cpf) != 11:
    print("CPF inválido: deve conter exatamente 11 dígitos.")
else:
    multiplicadores = list(range(2, 11))[::-1]  # de 10 até 2
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(9))
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto

    print("Dígito verificador calculado:", dv1)
    if dv1 == int(cpf[9]):
        print("CPF Válido")
    else:
        print("CPF Inválido")

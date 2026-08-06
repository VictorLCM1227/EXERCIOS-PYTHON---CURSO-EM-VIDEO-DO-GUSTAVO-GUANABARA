
def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situacão da turma.
    """
    turma = {}
    turma['quantidade_de_notas'] = len(notas)
    turma['maior_nota'] = max(notas)
    turma['menor_nota'] = min(notas)
    turma['media'] = sum(notas) / turma['quantidade_de_notas']
    if situacao:
        if turma['media'] >= 7:
            turma['situacao'] = 'BOA'
        elif turma['media'] >= 5:
            turma['situacao'] = 'RAZOÁVEL'
        else:
            turma['situacao'] = 'RUIM'
    return turma

resp = notas(5.5, 2.5, 1.5, situacao=True)
print(resp)
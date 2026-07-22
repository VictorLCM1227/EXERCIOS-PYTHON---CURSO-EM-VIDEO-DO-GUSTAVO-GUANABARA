print('-=' * 30)
print('Analisador de Triângulos')
print('-=' * 30)
primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
print('-' * 40)
if (primeiro_segmento < (segundo_segmento + terceiro_segmento)) and (segundo_segmento < (primeiro_segmento + terceiro_segmento)) and (terceiro_segmento < (segundo_segmento + primeiro_segmento)):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print('EQUILÁTERO!')
    elif primeiro_segmento == segundo_segmento or primeiro_segmento == terceiro_segmento or segundo_segmento == terceiro_segmento:
        print('ISÓCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
print('-=' * 30)
print('Analisador de Triângulos')
print('-=' * 30)
primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
if (primeiro_segmento < (segundo_segmento + terceiro_segmento)) and (segundo_segmento < (primeiro_segmento + terceiro_segmento)) and (terceiro_segmento < (segundo_segmento + primeiro_segmento)):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
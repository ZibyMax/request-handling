from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing

    from_landing = request.GET.get('from-landing')
    if from_landing:
        counter_click[from_landing] += 1
    # if from_landing == 'original':
    #    counter_click['original'] += 1
    # if from_landing == 'test':
    #    counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    to_landing = request.GET.get('ab-test-arg')
    counter_show[to_landing] += 1
    if to_landing == 'test':
        # counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    # counter_show['original'] += 1
    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:

    # if counter_show['original'] != 0:
        # original_conversion = counter_click['original'] / counter_show['original']
    # else:
        # original_conversion = 0

    # if counter_show['test'] != 0:
        # test_conversion = counter_click['test'] / counter_show['test']
    # else:
        # test_conversion = 0

    return render_to_response('stats.html', context={
        'test_conversion': counter_click['test'] / counter_show['test'] if counter_show['test'] else 0,
        'original_conversion': counter_click['original'] / counter_show['original'] if counter_show['original'] else 0
    })

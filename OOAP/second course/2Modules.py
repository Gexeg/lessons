"""
Задание 4.
Приведите пример иерархии классов (словесное описание), где применяется принцип Открыт-Закрыт, и обоснуйте,
почему одни классы (модули) выбраны открытыми, а другие закрытыми.
"""

# Окей, тогда возможно такая ситуация:
# когда-то начинал писать текстовую игру и в ней был класс комната. В этой комнате генерировался какой-то сценарий и когда 
# в комнату поступал объект класса "Герой", то "Комната" должна была отыграть "Сценарий" и применить его на героя 
# "Героя". Основная идея в разделении метрик. "Сценарий" может работать с состоянием героя, тогда как прохождение "комнат"
# использовалось для подсчета времени и напрямую на герое не отражалось.
# На этапе планирования в виде абстрактных классов-шаблонов система закрыта. У нас зафиксированы методы-интерфейсы, с помощью
# которых происходит общение между классами. Потом появляются конкретные реализации классов. Открытость системы для расширений в том,
# что мы можем относительно бесконечно наследоваться от первого сценария, пока поддерживаем оговоренные в классах-шаблонах
# интерфейсы, расширяя поведение и добавляя различные варианты прохождения комнат. Закрытость для изменений в том,
# классы должны поддерживать определенную структуру, чтобы соответствовать шаблонам.


"""
Задание 5.
Какие из пяти принципов повторного использования модуля поддерживаются в используемом вами языке программирования 
(в дополнение к классам как базовой синтаксической единице)?
"""

# 1 пункт в Python не реализовать с помощью модулей∕пакетов. В Python нет возможности жестко параметрировать типы. Только в виде "рекомендаций",
# если использовать аннотации. Ну и профита для быстродействия это особенно не несет, т.к. язык интерпретируемый а не компилируемый.
# Как страховку от ошибок разработки скорее.

# 2 пункт поддерживается: Создание модуля, объединяющего несколько активно обращающихся друг к другу функций.

# 3 пункт поддерживается: В Python есть возможность объединения модулей в пакет. 

# 4 пункт поддерживается частично: насколько я понял, на уровне модулей нет "автоматического" полиморфизма.
# Имя функции будет привязано к модулю и нет возможности где-то в одном месте обозначить, что текущий модуль наследует весь dict импортируемого.
# Можно попытаться сообразить подобие, вручную импортировав только нужные функции из модуля "родителя" и переопределив оставшиеся.
# Т.е. у нас есть возможность применять композицию, но нет наследования. 

# 5 пункт поддерживается: С помощью композиции мы можем интегрировать несколько модулей с минорными отличиями в поведении в один.


"""
Задание 6.
Существуют ли ситуации, когда связи между модулями должны делаться публичными?
Какие метрики вы бы предложили для количественной оценки принципов организации модулей?
Если вы разрабатывали программы, в которых было хотя бы 3-5 классов, как бы вы оценили их модульность по этим метрикам?
"""

# Не совсем понял что именно подразумевается под "публичными связями"

# Навскидку на ум приходит только количество импортов конкретного модуля в другие модули и количество импортируемых модулей в текущий.
# На основании этих данных можно сделать вывод о зависимостях модулей внутри системы и оценить правильно ли расположена главная логика,
# которая должна иметь как можно меньше зависимостей 

Для тетсирвоания сайта https://b2c.passport.rt.ru/ прмиенялось следующее:
- Ручные и автоматизированные тесты
- Анализ граничных значений
- Разбиение на классы эквивалентности
- Тестирование состояний и переходов

Файлы с тестами:

test_auth -  Проверки: 
- Корректнок изменение поля ввода логина в соответствии с выбранным табом; 
- Корректность валидации типа логина (мобилный телефон, почта, логин, личный счёт) в автоматическом режиме;
- Вывод сообщение об ошибке попытки авторизации при каждом возможном типе авторизации
- Корректность перенаправления на страницу восстановления пароля;
- Корректность перенаправления на страницу регистрации нового пользователя.

test_reg - 1 тест иммитирующий действия пользователя по нескольким тест-кейсам.

test_recovery - Проверки:
- Корректность изменения поля ввода логина в соответствии с выбранным табом
- Вывод корректного сообщения об ошибке попытки восстановления пароля для каждого способа восстановления пароля
- Корректность обновления капчи
- Корректность перенаправления на страницу авторизации
 



Не получилось реализовать и половину функционала для тестирования ввиду серьёзной нехватки времени, как для итоговой работы, так и для прохождения модулей оснвоа питона и автоматизации на нём. 

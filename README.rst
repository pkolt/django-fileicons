django-fileicons
================

Возвращает нужную иконку по типу файла.

Использование в шаблонах
------------------------
::

    {% load fileicons_tags %}

    {# Возвращает имя файла без расширения #}
    {{ object.attachment|filename }}

    {# Возвращает URL к иконке файла #}
    {{ object.attachment|fileicon }}

Настройка приложения
--------------------

Добавить значения в settings.py::

    # Шаблон HTML-тега изображения, можно использовать переменные %(url)s, %(name)s.
    FILEICON_TEMPLATE_IMAGE_TAG = '<img src="%(url)s" width="16" height="16" class="fileicon">'

Тестирование
------------

Выполнить::

    ``python manage.py test fileicons --setting=fileicons.tests.settings``

Благодарности
^^^^^^^^^^^^^

File Icons <http://www.splitbrain.org/projects/file_icons>

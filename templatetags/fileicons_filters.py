# coding: utf-8

import os
from django import template
from django.template.defaultfilters import safe
from django.utils.encoding import force_unicode
from fileicons.conf.settings import BASE_URL, ICON_LIST, DEFAULT_ICON, TEMPLATE_IMAGE_TAG

register = template.Library()

########################################################################################################################
# Utils                                                                                                                #
########################################################################################################################

def validate_path(func):
    """
    Декоратор, проверяет путь к файлу на корректность
    """
    def wrapper(path):
        if '.' in path.split(os.path.sep)[-1]:
            return func(path)
        return ''
    return wrapper

@validate_path
def get_name_fileicon(path):
    """
    Возвращает имя файла (без расширения)
    """
    filename = os.path.basename(force_unicode(path))
    name, ext = os.path.splitext(filename)
    return name

@validate_path
def get_url_fileicon(path):
    """
    Возвращает url иконки по типу файла
    """
    name, ext = os.path.splitext(force_unicode(path))
    if ext:
        ext = ext[1:]
        ext = ext.lower()
        filename = ICON_LIST.get(ext, DEFAULT_ICON)
        return '%s/%s' % (BASE_URL, filename)
    return ''

########################################################################################################################
# Filters                                                                                                              #
########################################################################################################################

def filename(filefield):
    """
    Возвращает имя файла без расширения.

    {{ object.attachment|filename }}
    """
    return get_name_fileicon(filefield.name)

register.filter('filename', filename)

def fileicon_url(filefield):
    """
    Возвращает URL к иконке файла.

    {{ object.attachment|fileicon_url }}
    """
    return get_url_fileicon(filefield.name)

register.filter('fileicon_url', fileicon_url)

def fileicon(filefield):
    """
    Возвращает иконку файла в виде HTML тега <img>.

    {{ object.attachment|fileicons }}
    """
    name = get_name_fileicon(filefield.name)
    url = get_url_fileicon(filefield.name)
    html = TEMPLATE_IMAGE_TAG % {
        'name': name,
        'url': url,
        }
    return safe(html)

register.filter('fileicons', fileicon)

def fileicon_for_text(filefield):
    """
    Парсит HTML-разметку, добавляя иконки к ссылкам.
    Исключения: ссылки внутри которых содержится тег <img>.

    {{ object.text|text_fileicon }}
    """
    pass

#register.filter('text_fileicon', text_fileicon)



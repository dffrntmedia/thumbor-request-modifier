#!/usr/bin/python
# -*- coding: utf-8 -*-


from thumbor.loaders import http_loader
from tornado.concurrent import return_future


def _url_contains(context, url, params):
    [value] = params
    return value in url


condition_handlers = {
    'url_contains': _url_contains
}


def _set_header(context, url, params):
    [name, value] = params
    context.request_handler.request.headers[name] = value


modification_handlers = {
    'set_header': _set_header
}


def _modify_request(context, url):
    for modification in context.config.REQUEST_MODIFIER_HTTP_LOADER_MODIFICATIONS:
        [modification_type, modification_params, condition_type, condition_params] = modification
        condition_handler = condition_handlers[condition_type]
        if condition_handler(context, url, condition_params):
            modification_handler = modification_handlers[modification_type]
            modification_handler(context, url, modification_params)


@return_future
def load(context, url, callback):
    _modify_request(context, url)
    return http_loader.load_sync(context, url, callback, normalize_url_func=_normalize_url)

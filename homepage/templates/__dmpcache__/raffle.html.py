# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523136644.697129
_enable_loop = True
_template_filename = '/Users/brand/Desktop/history/history/homepage/templates/raffle.html'
_template_uri = 'raffle.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['meta', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        button = context.get('button', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def meta():
            return render_meta(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        button = context.get('button', UNDEFINED)
        def content():
            return render_content(context)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div id=\'former\' class="text-center">\n    <h1 id="winner">')
        __M_writer(filters.html_escape(str( name )))
        __M_writer('</h1>\n    <br />\n    ')
        __M_writer(str( button ))
        __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brand/Desktop/history/history/homepage/templates/raffle.html", "uri": "raffle.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 4, "49": 12, "55": 3, "61": 3, "67": 6, "75": 6, "76": 8, "77": 8, "78": 10, "79": 10, "85": 79}}
__M_END_METADATA
"""

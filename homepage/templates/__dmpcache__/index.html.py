# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523140421.248906
_enable_loop = True
_template_filename = '/Users/brand/Desktop/history/history/homepage/templates/index.html'
_template_uri = 'index.html'
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
        names = context.get('names', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        ordinances = context.get('ordinances', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
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
        __M_writer('\n  <meta http-equiv="refresh" content="5"/>\n  <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        names = context.get('names', UNDEFINED)
        def content():
            return render_content(context)
        ordinances = context.get('ordinances', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <div class="col-xs-4">\n        <ul>\n          <h1>Ward Totals</h1>\n          <li>\n            Names:\n          </li>\n          <li class="num">\n            ')
        __M_writer(str( names ))
        __M_writer('\n          </li>\n          <li>\n            Ordinances:\n          </li>\n          <li class="num">\n            ')
        __M_writer(str( ordinances ))
        __M_writer('\n          </li>\n        </ul>\n        <h2 class="text-center">\n          When we gather our family histories\n          and go to the temple on behalf of our\n          ancestors, God fulfills promised blessings\n          simultaneously on both sides of the veil.\n        </h2>\n        <h3 class="text-right">\n          - Elder Dale G. Renlund\n        </h3>\n      </div>\n      <div class="col-xs-8">\n        <a href="/homepage/rafflestart">\n          <img src="https://photos.smugmug.com/Temples/Organized-by-Temple/Provo-City-Center-LDS-Temple/i-3ML4932/0/44fd14f2/X2/Provo%20City%20Center%20Temple%20-%20Springtime%20Family_SJ07039-X2.jpg" />\n        </a>\n      </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brand/Desktop/history/history/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 6, "49": 43, "55": 3, "61": 3, "67": 8, "75": 8, "76": 17, "77": 17, "78": 23, "79": 23, "85": 79}}
__M_END_METADATA
"""

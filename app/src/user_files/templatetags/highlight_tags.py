import bleach
from django import template
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.python import PythonLexer

register = template.Library()


@register.filter
def highlight_code(code: bytes, style: str) -> str:
    lexer = PythonLexer()
    formatter = HtmlFormatter(style=style, linenos="inline", noclasses=True)
    highlighted_code = highlight(bleach.clean(code.decode()), lexer, formatter)
    return mark_safe(highlighted_code)

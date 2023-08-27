import pytest
from django.template import Context, Template


@pytest.fixture
def render_template(rf, user):
    # pylint: disable=invalid-name
    def _render_template(template_string, context=None):
        request = rf.get("/")
        request.user = user
        template = Template(template_string)
        context = context or {}
        context = Context(context)
        rendered = template.render(context)
        return rendered

    return _render_template


@pytest.mark.django_db
def test_highlight_code_tag(render_template):
    # pylint: disable=redefined-outer-name
    """
    Test the highlight_code template tag.
    """
    code = b"def my_function():\n    return 42"
    template_string = "{% load highlight_tags %}{{ code|highlight_code:'colorful' }}"
    rendered = render_template(template_string, {"code": code})

    assert 'class="highlight"' in rendered
    assert "42" in rendered

from aiohttp_jinja2 import render_template


async def main_handler(request):
    return render_template('MainTemplate.html', request, {})

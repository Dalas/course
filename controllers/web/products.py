from aiohttp_jinja2 import render_template


async def products_handler(request):
    return render_template('ProductsTemplate.html', request, {})

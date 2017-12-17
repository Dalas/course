from aiohttp_jinja2 import render_template


async def store_houses_handler(request):
    return render_template('StoreHousesTemplate.html', request, {})

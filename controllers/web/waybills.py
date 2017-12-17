from aiohttp_jinja2 import render_template


async def waybills_handler(request):
    return render_template('WaybillsTemplate.html', request, {})

from aiohttp_jinja2 import render_template


async def registration_handler(request):
    return render_template('RegistrationTemplate.html', request, {})

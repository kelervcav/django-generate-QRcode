from django.shortcuts import render
from io import BytesIO
import qrcode
import base64


def qrcode_generator(request):
    image = ''
    if request.method == 'POST' and request.POST.get('input_text'):
        text = request.POST.get('input_text')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )

        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image()
        buffer = BytesIO()
        img.save(buffer, 'PNG')

        image = base64.b64encode(buffer.getvalue())

    template_name = 'qrcodes/qrcode.html'
    context = {
        'image': image,
    }
    return render(request, template_name, context)

import qrcode

data = input("Enter a site: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('MyQRCode2.png')
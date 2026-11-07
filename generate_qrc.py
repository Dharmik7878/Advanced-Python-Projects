# QR Code Generator program
import qrcode as qr

img = qr.make("https://github.com/Dharmik7878")
img.save("github_profile.png")
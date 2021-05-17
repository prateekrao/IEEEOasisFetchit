import qrcode

start = 'green'
stop = 'red'
path = 'yellow'

data = [start, stop, path]

image = qrcode.make(data)
image.save("qrcode.png")
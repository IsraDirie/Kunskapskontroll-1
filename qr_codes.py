import qrcode
import pandas as pd

data 

for idx in df.index:
    qr = qrcode.make(idx)
    qr.save(f"qr_codes/{idx}.png")
else : 
    print ('Isra')

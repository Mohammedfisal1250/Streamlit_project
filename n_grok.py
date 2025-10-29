# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 14:50:06 2025

@author: ZT-055688
"""

from pyngrok import ngrok

# إضافة التوكن مرة واحدة
ngrok.set_auth_token("34jHRgSK142ElZrh2mNxIkqnwPr_3By3q1qL4W4BJG1nSF9BZ")

# فتح النفق على منفذ 8501
public_url = ngrok.connect(8501)
print("📡 رابط الوصول الخارجي:", public_url)

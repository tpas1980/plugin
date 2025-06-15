import locale
import importlib
import random as rd
from datetime import datetime
from googletrans import Translator
import subprocess
import sys


def get_today():
    lang, _ = locale.getdefaultlocale()
    if lang and lang.startswith("fa"):
        try:
            import jdatetime
            return jdatetime.date.today().strftime('%Y/%m/%d')
        except ImportError:
            return "jdatetime نصب نیست."
    else:
        return datetime.today().strftime('%Y-%m-%d')
def trans(text):
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "googletrans==4.0.0-rc1"])
    translator = Translator()

    try:
        importlib.import_module("googletrans")
        pass
    except ImportError:
        print(f"googletrans is not install, install pack...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    # تشخیص زبان سیستم
    system_lang = locale.getdefaultlocale()[0]
    if not system_lang:
        system_lang = 'en'  # پیش‌فرض اگر زبان شناسایی نشد
    dest_lang = system_lang.split('_')[0]  # مثلاً 'fa_IR' → 'fa'

    # تشخیص زبان متن ورودی
    detected_lang = translator.detect(text).lang

    # اگر زبان ورودی و خروجی یکی باشند، کاری نکن
    if detected_lang == dest_lang:
        return text

    # ترجمه
    result = translator.translate(text, src=detected_lang, dest=dest_lang)
    return result.text

def Saved(yes, namefile, format, content):
    yes1 = yes.lower()
    if yes1 not in ["y", "n"]:
        raise ValueError("Please enter 'y' or 'n' only.")
    
    if yes1 == "y":
        f = f"{rd.randint(1111, 9999)}-{namefile}.{format}"
        with open(f, "a") as file:
            file.write(content)
    elif yes1 == "n":
        f = f"{namefile}.{format}"
        with open(f, "a") as file:
            file.write(content)
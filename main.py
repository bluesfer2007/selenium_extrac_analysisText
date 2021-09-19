from infinaCuantia.sercop import Sercop
import time

with Sercop() as bot:

    bot.get_url_sercop()
    i=0
    while i<20:
        i+=1
        time.sleep(2)
        bot.sercop_report(i)
        bot.next_page()
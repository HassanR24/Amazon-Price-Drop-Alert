import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = ""       #insert your email address
MY_PASSWORD = ""    #insert your password (create an app specific password if you're using gmail)
REC_EMAIL = ""      #insert the alert receiver's email address
DESIRED_PRICE = 20

URL = "https://www.amazon.com/Padarsey-Replacement-Keyboard-MacBook-13-inch/dp/B01M03H4HO/ref=sr_1_3?" \
      "crid=2LY5NH7N34GBX&keywords=Padarsey+Backlight+Backlit+Keyboard+with+80+PCE+Screws+for+MacBook+Pro+Unibody" \
      "+13.3%22+A1278+2008-2015+Year+W%2FScrews+US+Layout&qid=1678355081&sprefix=padarsey+backlight+backlit+keyboard" \
      "+with+80+pce+screws+for+macbook+pro+unibody+13.3+a1278+2008-2015+year+w%2Fscrews+us+layout%2Caps%2C370&sr=8-3"

#Replace the link above with something you are looking to buy.

headers = {
    "Accept-Language": "en-gb",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/15.6.1 Safari/605.1.15"
}
#replace with your own headers above.

response = requests.get(URL, headers=headers)
site_html = response.text

soup = BeautifulSoup(site_html, "html.parser")

whole_price = soup.select_one(selector="span .a-price-whole").getText()
decimal_price = soup.select_one(selector="span .a-price-fraction").getText()
price = float(whole_price + decimal_price)

if price < DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:        #replce this according to your email
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=REC_EMAIL,
                            msg=f"Subject:Price Dropped!\n\n"
                                f"The price of 'Padarsey New Laptop Replacement Keyboard Compatible for "
                                f"MacBook Pro 13-inch A1278 2008 2009 2010 2011 2012 2013 2014 2015 Year with 80Pce "
                                f"Keyboard Screws' is now ${price}.\nBuy it now using the link below:\n"
                                f"{URL}")
        
                                #replace the message with to your own choice of words.
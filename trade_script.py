# cook your dish here

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import datetime
import smtplib
from email.message import EmailMessage
from time import sleep


from alpaca.trading import client as AlpacaClient
import config

# Alpaca Trading
class trading_bot(object):
    def __init__(self):
        self.key = config.API_KEY
        self.secret = config.SECRET_KEY
        self.alpaca_endpoint = "https://broker-api.sandbox.alpaca.markets"
        self.api = AlpacaClient
        self.symbol = input('Input a symbol')
        self.current_order = None
        self.last_price = 1
        self.curr_price = 1
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
            print(self.position)
        except:
           self.position = 0


        #self.last_price = float(self.api.get_position(self.symbol).price)

    def submit_order(self, target):
        if self.current_order is not None:
            self.api.canel_order(self.current_order.id)
        
    def Analyze_Alpaca(self, margin):
        active_assets = self.api.list_assests(status='active')
        nasdaq = [a for a in active_assets]
        print(nasdaq)
        result = 0;
        sign = 0;
        print(f'curr_price: ${curr_price} curr_position: ${curr_position}  Margin: {margin*100}%  ')
        print('')
        curr_ex_literal = 'current change % : ';
        asset_price = curr_price;
        margin = margin*100
        change = ((curr_position-asset_price)/curr_position)*100;
        changeinString = str(change);
        if asset_price > curr_position:
            sign = -1;
            print(curr_ex_literal + 'sell');
            print(f'UP /\ : %{changeinString}');
            if (change*sign >= margin):
                result = -1;
        elif asset_price < curr_position:
            sign = -1;
            print(curr_ex_literal + 'buy');
            print(f'DOWN \/ : %{changeinString*sign}');
            if (change >= margin):
                print(change*sign)
                result = 1;
        else:
            print(curr_ex_literal);
            print(change*sign);
        return result;




# Alpaca Trading

# Online Python - IDE, Editor, Compiler, Interpreter
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body + "\n")

    msg['subject'] = subject
    msg['to'] = to
    
    
    user = "alejandropc77@gmail.com"
    msg['from'] = user
    password = "nilumbbqmxvaxtml"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

## Trader Script
def Analyze(curr_price, curr_position, margin):
    result = 0;
    sign = 0;
    print(f'curr_price: ${curr_price} curr_position: ${curr_position}  Margin: {margin*100}%  ')
    print('')
    curr_ex_literal = 'current change % : ';
    asset_price = curr_price;
    margin = margin*100
    change = ((curr_position-asset_price)/curr_position)*100;
    changeinString = str(change);
    if asset_price > curr_position:
        sign = -1;
        print(curr_ex_literal + 'sell');
        print(f'UP /\ : %{changeinString}');
        if (change*sign >= margin):
            result = -1;
    elif asset_price < curr_position:
        sign = -1;
        print(curr_ex_literal + 'buy');
        print(f'DOWN \/ : %{changeinString*sign}');
        if (change >= margin):
            print(change*sign)
            result = 1;
    else:
        print(curr_ex_literal);
        print(change*sign);
    return result;
        

def BuyTake(curr_price, curr_position, margin):
    purchase_confirm = False;
    target_price = curr_position + (curr_position*margin);
    print('*Target Price')
    print(target_price)
    print('*Curr Price')
    print(curr_price)

    if (curr_price >= target_price):
        order = client.create_test_order(
        symbol='XLMUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce=Client.TIME_IN_FORCE_GTC,
        quantity=1000,
        price=0.33)
        purchase_confirm = True;
        print(order)
    return purchase_confirm
    
def SellClose(margin):
    purchase_confirm = False;
    target_price = curr_position - (curr_position*margin);
    print('*Target Price')
    print(target_price)
    print('*Curr Price')
    print(curr_price)

 #   if (curr_price <= target_price):
  #      order = client.create_test_order(
 #       symbol='XLMUSDT',
 #       side=Client.SIDE_BUY,
 #       type=Client.ORDER_TYPE_LIMIT,
 #       timeInForce=Client.TIME_IN_FORCE_GTC,
 #       quantity=1000,
 #       price=curr_price)
 #       purchase_confirm = True;
 #       print('purchase confirmed!');
 #       orders = client.get_all_orders(symbol='XLMUSDT')
 #       print(order)
 #       print(orders)


    sold_confirm = false;
    #Analyze(margin);
    target_price = position_price - (position_price*margin);
    
    if (position_price >= target_price):
        Close_Position();
        sold_confirm = true;
        print('purchase confirmed!');
    return sold_confirm

""" bot = trading_bot();
result = bot.Analyze_Alpaca(bot)
print('result from AnalAlpaca:')
print(result) """

uInput = input("Plese enter a Symbol (Ex: SHIBUSDT)\n")
symbolName = uInput
uInput = input("Plese enter a margin (0.1 = 10%)\n")
margin = float(uInput)
uInput = input("Plese enter current position price\n")
curr_position = float(uInput)
#email_alert('FLY ME TO THE MOON', str("WELCOME TO THE *FLY ME TO THE MOON* ALERT SYSTEM. WILL TRIGGER WHEN SHIB IS 10 % UP\n\n https://open.spotify.com/track/1PVTvvxpSkyJWemW1CwVVk?si=224bf572462c4f06"), "alejandropc77@gmail.com")

sim_time = 50000000;
buy_or_sell = 0;

## WTF IS THIS PLACEMENT
while(True):
    client = AlpacaClient
    buy_or_sell = 0
    assetList = {"SPY, BTCUSD"}
    myBot = trading_bot()
    WL = client(client, assetList[0])

    client.add_asset_to_watchlist_by_id(WL ,symbolName)
    client.get_asset(symbolName)
    curr_price = float(curr_price['price'])
    print(symbolName)
    print(f'TIMESTAMP :: {datetime.datetime.now()}');
    # Should I Buy or Sell
    buy_or_sell = Analyze(curr_price,curr_position, margin);

    if(buy_or_sell == -1):
        confirm = BuyTake(curr_price, curr_position, margin);
        if confirm:
            email_alert('SELL', str("The Asset {0} is at a high of ${1}FLY ME TO THE MOON".format(symbolName, curr_price )), "alejandropc77@gmail.com")


            print("Position Taken");
            # Check if this is price is correct
            curr_position = curr_price;
            print(f'Last Entrance Value was: ${curr_price}')
            print(f'Last Entrance Value now equals curr_position Value! $({curr_position})')
        print()
    elif(buy_or_sell == 1):
        email_alert('BUY', str("The Asset {0} is at a low of ${1}.\n\nYour Position is ${2}".format(symbolName, curr_price , curr_position)), "3053840202@pm.sprint.com")

        #SellClose(curr_price, curr_position, margin);
        print("Position Closed");
        curr_position = curr_price;
        print(f'Last Exit Value was: ${curr_price}')
        print(f'Last Exit Value now equals curr_position Value! (${curr_position}) ')
        print()
    elif(buy_or_sell == 0):
        print("no operation done");
    sleep(10)
    print('--------------------------------------------------------------------------------------------------------------------------')

print()
print('Analysis Finsihed')

        
        


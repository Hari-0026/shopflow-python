products={1:{"ID":1,"name":"MILK","amount":40,"stock":20},
          2:{"ID":2,"name":"EGG","amount":7,"stock":70},
          3:{"ID":3,"name":"WATER BOTTLE","amount":20,"stock":50},
          4:{"ID":4,"name":"SOFT DRINK","amount":20,"stock":40},
          5:{"ID":5,"name":"COOKIES","amount":10,"stock":65},
          6:{"ID":6,"name":"CHIPS","amount":10,"stock":75}}
def prevent_error(message):
    while True:
        try:
            choice=int(input(message))
            return choice

        except ValueError:
            print("please enter a number!!")
cart={}
customer_info={}
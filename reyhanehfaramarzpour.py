class Card:
    def __init__(self,cardnumber,tarikhengheza,mojoodi,darandecard):
        self.cardnumber=cardnumber
        self.tarikhengheza=tarikhengheza
        self.mojoodi=mojoodi
        self.darandecard=darandecard

list1=[Card("123456789101112","12/03",6000,"ali"),Card("987654321101211","8/25",4000,"akbar"),Card("90807060504030","10/17",8000,"zahra")]
for Card in list1:
    if Card.mojoodi > 5000:
        print(f"darandecard={Card.darandecard},cardnumber={Card.cardnumber},mojoodi={Card.mojoodi}")
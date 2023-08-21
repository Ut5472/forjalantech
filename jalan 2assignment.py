class touristdata:
    def totalbill(tourist):
        billtotal=0
        billlist=[]
        for age in tourist:
            if age<=2:
                billtotal=billtotal+0
                billlist.append(0)
            elif 2<age<18:
                billtotal=billtotal+100
                billlist.append(100)
            elif 18<=age<60:
                billtotal=billtotal+500
                billlist.append(500)
            else:
                billtotal=billtotal+300
                billlist.append(300)
        return billtotal,billlist
    
    def crosscheck(tourist,listingbill,number):
        print("The Ticket Contents are as Follows:")
        print("No. of People =",len(tourist))
        for i in range(number):
            print("The Age is:",tourist[i],"And Ticket Price is:",listingbill[i])
        totaling=sum(listingbill)
        print("Total Amount Payed:",totaling)
        print("Have A Nice Day , Enjoy you day in Zoo :) ")
def main():
    number=int(input("Enter the Number of Tourist Arriving:"))
    tourist=[]
    for i in range(number):
        print("Enter the Age of Tourist No.",i+1)
        age=int(input())
        tourist.append(age)
    total,listingbill=touristdata.totalbill(tourist)
    print("The Total amount You have To pay is :",total)
    print("But Before You proceed , There is a Security Check At Enterance:")
    print("Show This Ticket To Security Guard:")
    touristdata.crosscheck(tourist,listingbill,number)

main()   

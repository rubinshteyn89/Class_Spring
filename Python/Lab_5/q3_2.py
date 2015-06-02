def interest(rate):
    rate = rate+1
    amount = 100
    years = 0
     
    while amount<200:
        amount = amount*rate
        years = years+1
     
    return years   
 
 
def main():
     
    print('A Program to calculate how long it take to double investment\nbase on interest rate enter by user.\n')
     
    try:
        more = 'yes'
         
        while more[0] == 'y' or more[0] == 'Y':
             
            rate = eval(input('Enter annualized interest rate: '))  #priming read
             
            while rate <= 0:
                 
                print('\nPlease correct the interest number.')
                rate = eval(input('Enter annualized interest rate: '))
             
            result = interest(rate)
            print('\n>> It will take {} years to double investment.'.format(result))
             
            more = input('\nNeed to try again? [Yes or No]: ')
         
         
    except NameError:
        print('\nError! Please enter rate in number format.')
         
    except:
        print('\nUnknow Error!')
 
if __name__ =='__main__': main()

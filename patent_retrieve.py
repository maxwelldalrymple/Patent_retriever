import requests


def patents_from_year(year, patent_amount, starting_number): # function to save multiple patents from a specific year and starting patent number

    pat_am = patent_amount + 1
    url_list = list(range(0, pat_am))
    year = str(year)
    max_num = 10000000 # highest number 
    numbers = list(range(starting_number - 1, max_num)) # list of numbers from 

    for i in range(pat_am):
        num = str(format(numbers[i + 1],'07d')) # convert number to 7 signifcant digits
        url_list[i] = 'http://pimg-faiw.uspto.gov/fdd/' + num[5] + num[6] + '/'+year+'/'+num[3]+num[4]+'/' + num[0] + num[1] + num[2] + '/0.pdf' # url to patent using the url code diagnosed
        currentFile = requests.get(url_list[i])
        open('Patents_PDFs/' + year + '_'+ num + '.pdf', 'wb').write(currentFile.content) # write data to pdf file




def specific_patent_number(spec_number, starting_year, year_amount = 1): # function to save specific patent numbers every year, given a stating year

    year_am = year_amount + 1
    url_list = list(range(0, year_am))
    starting_year_int = starting_year
    number = spec_number

    for i in range(year_am):
        starting_year_str = str(starting_year_int)
        num = str(format(number,'07d'))
        url_list[i] = 'http://pimg-faiw.uspto.gov/fdd/' + num[5] + num[6] + '/'+ starting_year_str +'/'+num[3]+num[4]+'/' + num[0] + num[1] + num[2] + '/0.pdf'  # url to patent using the url code diagnosed
        currentFile = requests.get(url_list[i])
        print(url_list[i])
        open('Patents_PDFs/Specific_numbers/' + starting_year_str + '_'+ num + '.pdf', 'wb').write(currentFile.content) # write data to pdf file
        starting_year_int += 1


def max_patents(year): # function to determine the maximum patent number for specific year

    numbers = list(range(0,10000000))
    count = 0

    while True:

        num = str(format(numbers[count + 1],'07d')) # make the number 7 significant digits
        url_list = 'http://pimg-faiw.uspto.gov/fdd/' + num[5] + num[6] + '/'+ str(year) +'/'+num[3]+num[4]+'/' + num[0] + num[1] + num[2] + '/0.pdf'  # url to patent using the url code diagnosed
        currentFile = requests.get(url_list) # request site
        response = str(currentFile)
        if response == '<Response [200]>': # if request returns true do nothing
            continue
        else: # if request returns false return the patent number, this lets us know the max number of patent, in production a test case should be added to make sure the next 10 numbers/req also fail.
            print('\n')
            print("This is the largest patent number:  ", num)
            print('\n',"The URl is: ", url_list)
            print('\n')
            break
        count += 1


def main():

    patents_from_year(2023, 100, 1)

main()

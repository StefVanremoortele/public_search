from public_search.functions import get_company_details
from data.companies import btw_nr, companies



def run():
    print("public search works")
    company_details = get_company_details(btw_nr)
    print(company_details)


run()
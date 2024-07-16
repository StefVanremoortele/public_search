

mock_btw_nr = "BTW BE 0123 456 789"

companies = {
    mock_btw_nr: {
        'adress': {
            'street': 'Distellaan',
            'house_nr': '542',
            'postcode': '8400',
        }
    }
}

def get_company_details(btw_nr):
    return companies[btw_nr]


def run():
    print("public search works")
    company_details = get_company_details(mock_btw_nr)
    print(company_details)


run()
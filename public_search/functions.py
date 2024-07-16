from data.companies import companies

mock_btw_nr = "BTW BE 0123 456 789"


def get_company_details(btw_nr):
    return companies[btw_nr]

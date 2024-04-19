import requests
from bs4 import BeautifulSoup

def get_survay_number():
    response = requests.get('https://dharani.telangana.gov.in/knowLandStatus')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        district_select = soup.find('select', id='districtID')
        district_options = district_select.find_all('option')

        district_data = [
            {option['value'] : option.get_text(strip=True)}
            for option in district_options
            if option.text != 'Please Select'
        ]
        #print(district_data)

        district_value_lst = []

        for id in district_data:
            for k,v in id.items():
                district_value_lst.append(k)
        #print(district_value_lst)

        for i in district_value_lst:
            response_mandal = requests.get(f'https://dharani.telangana.gov.in/getMandalFromDivisionCitizenPortal?district={i}')
            if response_mandal.status_code == 200:
                soup = BeautifulSoup(response_mandal.content, 'html.parser')
                options = soup.find_all('option')

                mandal_data = [
                    {option['value']: option.get_text(strip=True)}
                    for option in options
                    if option.text != 'Please Select'
                ]

                #print(mandal_data)


            mandal_value_lst = []
            for id in mandal_data:
                for k, v in id.items():
                    mandal_value_lst.append(k)
            #print(mandal_value_lst)


            for i in mandal_value_lst:
                response_village = requests.get(f'https://dharani.telangana.gov.in/getVillageFromMandalCitizenPortal?mandalId={i}')
                if response_village.status_code == 200:
                    soup = BeautifulSoup(response_village.content, 'html.parser')
                    options = soup.find_all('option')

                    village_data = [
                        {option['value']: option.get_text(strip=True)}
                        for option in options
                        if option.text != 'Please Select'
                    ]

                    #print(len(village_data))

                    survey_value_lst = []
                    for id in village_data:
                        for k, v in id.items():
                            survey_value_lst.append(k)
                    # print(mandal_value_lst)

                    for survey in survey_value_lst:
                        response_survey = requests.get(f'https://dharani.telangana.gov.in/getSurveyCitizen?villId=1813014&flag={survey}')
                        if response_survey.status_code == 200:
                            soup = BeautifulSoup(response_survey.content, 'html.parser')
                            options = soup.find_all('option')

                            survey_data = [
                                {option['value']: option.get_text(strip=True)}
                                for option in options
                                if option.text != 'Please Select'
                            ]

                            #print(survey_data)


get_survay_number()
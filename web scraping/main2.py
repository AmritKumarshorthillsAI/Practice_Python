from bs4 import BeautifulSoup
import requests
import time

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml') # lxml parser
    job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(job)

    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').strip()
    # print(company_name)

    skills = job.find('div', class_ = 'more-skills-sections').text.replace(" ", "").strip().split()
    skillset =  ', '.join(skills)
    # print(skills)

    more_info = job.header.h2.a['href']

    with open(f'posts/jobDetail.txt', 'w') as f:
        f.write(f'''
        Company Name: {company_name}
        Required Skills: {skillset}
        More Info: {more_info}
            ''')
        
    print("File saved")
    

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 2
        # print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*5)



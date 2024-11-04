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
        
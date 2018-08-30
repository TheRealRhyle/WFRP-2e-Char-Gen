def format_sheet(charin):
    charin['weight'] = str(charin['weight'])

    # skills = charin['skills']
    skills = ', '.join(sorted(charin['skills']))
    talents = ', '.join(sorted(charin['talents']))
    adv_skill = ', '.join(sorted(charin['adv_skill']))
    adv_talent = ', '.join(sorted(charin['adv_talent']))
    trappings = ', '.join(sorted(charin['trappings']))
    career_entries = ', '.join(sorted(charin['career_entries']))
    career_exits = ', '.join(sorted(charin['career_exits']))

    sheet = """Name: {name} the {career}
    Race: {race} Gender: {gender} Age: {age}
    Height: {height} Hair Color: {hair_color} Siblings: {siblings}
    Weight: {weight} Eye Color: {eye_color}
    Birthplace: {birthplace}
    Star Sign: {starsign}
    Distinguishing Marks: {marks}
    
    Main Profile:\t{main_profile_header}
    Main Profile:\t{main_profile}
    Main Advance:\t{main_profile_adv}
    Advance Taken: [  ][  ][  ][  ][  ][  ][  ][  ]
        
    Sec Profile:\t{secondary_profile_header}
    Sec Profile:\t{secondary_profile}
    Sec Advance:\t{secondary_profile_adv}
    Advance Taken: [  ][  ][  ][  ][  ][  ][  ][  ]
        
    Trappings:
    -------
    {}
    
    Skills:
    -------
    {}
       
    Talents:
    -------
    {}
    
    Skill Advancements:
    -------
    {}
    
    Talent Advancements:
    -------
    {}
    
    Career Entries
    -------
    {}
    
    Career Exits
    -------
    {}
    
    """.format(trappings, skills, talents, adv_skill, adv_talent, career_entries,career_exits, **charin).replace('    ','')

    sheet_as_html = sheet.replace('\n','<br>')
    header = '<html><title>{name}</title><body>'.format(**charin)
    with open('characters\{name}.html'.format(**charin),'w+') as file:
        file.write(header)
        file.write(sheet_as_html)
        file.write('<font size="1"> Character auto generated bt WFRP-2e-Char-Gen by Phillip W. (<a href = "http://twitch'
                   '.tv/darkxilde">twitch.tv/darkxilde</a>)</font>')
        file.write('</body></html>')

    return sheet

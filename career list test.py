import career_listf as cf

career_name = 'Outrider'
scheme_name = career_name + ' Advance Scheme'
main_profile_dict = {'WS': 0, 'BS': 0, 'S': 0, 'T': 0, 'Ag': 0, 'Int': 0, 'WP': 0, 'Fel': 0}
secondary_profile_dict = {'A': 0, 'W': 0, 'SB': 0, 'TB': 0, 'M': 0, 'Mag': 0, 'IP': 0, 'FP': 0}

#career_name = cf.career_selection(scheme_name)

#print(scheme_name)
#print(career_name['Skills'])
career = cf.career_selection(scheme_name)

career['Skills'] = ', '.join(career['Skills'])
career['Talents'] = ', '.join(career['Talents'])
career['Trappings'] = ', '.join(career['Trappings'])
career['Career Entries'] = ', '.join(career['Career Entries'])
career['Career Exits'] = ', '.join(career['Career Exits'])
liststat = list(career['Statblock'])
main_profile_adv = liststat[0:7]
secondary_profile_adv = liststat[7:]


mp = dict(zip(main_profile_dict,main_profile_adv))
sp = dict(zip(secondary_profile_dict,secondary_profile_adv))


scheme_output = '''{}
{}
{}
{Skills}
{Talents}
{Trappings}
{Career Entries}
{Career Exits}
'''.format(scheme_name, mp, sp, **career)

print(scheme_output)
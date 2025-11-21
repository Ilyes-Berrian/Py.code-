def Email_Slicer(email):
        
    (username, domain)= email.split('@')
    (domain, extenstion)= domain.split('.')
    
    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ',extenstion)
    print('')
    

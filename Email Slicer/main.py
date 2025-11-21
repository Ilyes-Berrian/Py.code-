from functions import Email_Slicer

ar=[
    'yanoder965@izeao.com',
    'yanoder965@izeao.com',
    'noreply@tiktok.com',
    'no-reply@duolingo.com',
    'no-reply@revolut.com'
]

print(f'{"\nWellcome on our Email Slicer App":=>65}\n{'='*32}')
for email in ar:
    print('Email Address: ', email)
    Email_Slicer(email)
    
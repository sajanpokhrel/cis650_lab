def remember(x):
    if hasattr(remember, 'Date'):
        return(f'done on {remember.Date}')
    if hasattr(remember, 'Author'):
        return f'Hi {x}. Authored by {remember.Author}'
    else:
        return f'Hi {x}'
    
print(remember('Joe'))
i = remember
i. Author = 'Dell'
print(remember('Joe'))

remember.Date = 'Monday'
print(remember ('Joe'))

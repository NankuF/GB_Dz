def users(name, surname, age, town, email, tel):
    user = f'{name}, {surname}, {age}, {town}, {email}, {tel}'
    print(user)
    return user


users(name='Hugo', age=65, town='London', surname='Boss', email='hugo@gmail.com', tel='+7-777-777-77-7')

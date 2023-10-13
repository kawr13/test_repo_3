

def my_test_project(data: list):
    if not data:
        print('Пусто нету ни чего')
    else:
        for i in data:
            print(i)



if __name__ == '__main__':
    my_test_project([1, 2, 3, 4, 5])


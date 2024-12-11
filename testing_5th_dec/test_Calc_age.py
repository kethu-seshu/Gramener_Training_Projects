
from calc_age import get_age

def test_get_age():

    yyyy, mm, dd = map(int, "2003/01/01".split("/"))   

    age = get_age(yyyy, mm, dd)

    assert age == 22
    

# if __name__== "__main__":
#     unittest.main()
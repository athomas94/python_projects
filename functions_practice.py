def hello():
    print("Hello there!")

def pack(item1, item2, item3):
    packed_items = {item1, item2, item3}
    return packed_items

def eat_lunch(list):
    for i in list:
        if not list:
            print("My lunchbox is empty!")
        elif i == 0:
            print("First I eat an", list[0])
        else:
            print("Then I eat ", i)
    print("My lunchbox is empty!")
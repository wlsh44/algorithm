def to_minute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    book_time.sort()
    books = []
    for time in book_time:
        if not books:
            books.append(time)
        else:
            flag = True
            for i, book in enumerate(books):
                if to_minute(book[1]) + 10 <= to_minute(time[0]):
                    books[i] = time
                    flag = False
                    break
            if flag:
                books.append(time)
    return len(books)
import db
from mplace import ozon


def main():
    session = db.session_factory()

    rows = session.query(ozon.Posting).limit(100).all()
    for row in rows:
        print(row.order_number)


if __name__ == '__main__':
    main()

import db
from mplace import ozon


def main():
    session = db.session_factory()

    rows = session.query(ozon.Realization).limit(100).all()
    for row in rows:
        print(row.doc_date)


if __name__ == '__main__':
    main()

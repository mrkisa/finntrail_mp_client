import db
from mplace import wb


def main():
    session = db.session_factory()

    rows = session.query(wb.Sale).limit(100).all()
    for row in rows:
        print(row.srid)


if __name__ == '__main__':
    main()

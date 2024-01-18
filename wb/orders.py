import db
from mplace.models import WBOrder


def main():
    session = db.session_factory()

    rows = session.query(WBOrder).all()
    for row in rows:
        print(row.srid)


if __name__ == '__main__':
    main()

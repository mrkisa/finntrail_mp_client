import db
from mplace.models import WBSale


def main():
    session = db.session_factory()

    rows = session.query(WBSale).limit(100).all()
    for row in rows:
        print(row.srid)


if __name__ == '__main__':
    main()

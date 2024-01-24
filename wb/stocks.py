import db
from mplace.models import WBStock


def main():
    session = db.session_factory()

    rows = session.query(WBStock).limit(100).all()
    for row in rows:
        print(row.nmId)


if __name__ == '__main__':
    main()

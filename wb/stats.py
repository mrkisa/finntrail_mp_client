import db
from mplace.models import WBStatRow


def main():
    session = db.session_factory()

    rows = session.query(WBStatRow).limit(100).all()
    for row in rows:
        print(row.dt)


if __name__ == '__main__':
    main()

import db
from mplace import wb


def main():
    session = db.session_factory()

    rows = session.query(wb.RealizationRow).limit(100).all()
    for row in rows:
        print(row.rrd_id)


if __name__ == '__main__':
    main()

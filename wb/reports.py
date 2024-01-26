import db
from mplace.models import WBReportRow


def main():
    session = db.session_factory()

    rows = session.query(WBReportRow).limit(100).all()
    for row in rows:
        print(row.rrd_id)


if __name__ == '__main__':
    main()

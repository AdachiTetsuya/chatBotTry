import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from api.serializers import ResponseMessageSerializer

from .utils import is_all_empty_str_row

# CSV ファイルの 列番号
TEXT = 2
RELATIONSHIP_LEVEL_MIN = 3
RELATIONSHIP_LEVEL_MAX = 4
POLL_GENDER = 5
POLL_AGE_MIN = 6
POLL_AGE_MAX = 7

HEADER_LENGTH = 1


class Command(BaseCommand):
    help = "Create ResponseMessage"

    def add_arguments(self, parser):
        parser.add_argument("csv_file_name", type=str)

    def handle(self, *args, **options):
        csv_file_name = options["csv_file_name"]
        print(csv_file_name)
        csv_file_path = f"{settings.BASE_DIR}/api/data/csv/{csv_file_name}.csv"

        # CSVファイルを開く
        csv_file = open(csv_file_path, "r", encoding="utf_8", newline="")

        # CSVデータを読み込む
        reader = csv.reader(
            csv_file,
            delimiter=",",
            doublequote=True,
            lineterminator="\r\n",
            quotechar='"',
            skipinitialspace=True,
        )

        # ラベルデータをスキップする
        for skip in range(HEADER_LENGTH):
            next(reader)

        csv_reader = list(reader)

        data_list = [
            {
                "text": row[TEXT],
                "relationship_level_min": row[RELATIONSHIP_LEVEL_MIN],
                "relationship_level_max": row[RELATIONSHIP_LEVEL_MAX],
                "poll_gender": row[POLL_GENDER],
                "poll_age_min": row[POLL_AGE_MIN],
                "poll_age_max": row[POLL_AGE_MAX],
            }
            for row in csv_reader
            if not is_all_empty_str_row(row)
        ]

        serializer = ResponseMessageSerializer(data=data_list, many=True)

        if serializer.is_valid():
            serializer.save()
        else:
            raise CommandError(serializer.errors)

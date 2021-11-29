import sys


def validate():
    exit_one_checks = [
        ("{{ cookiecutter.project_name }}", "project name"),
        ("{{ cookiecutter.creator }}", "creator"),
        ("{{ cookiecutter.creator_email }}", "creator email address"),
        ("{{ cookiecutter.license }}", "license"),
        ("{{ cookiecutter.meilisearch_url }}", "MeiliSearch URL"),
    ]

    for check in exit_one_checks:
        exit_one(check[0], check[1])

    license = "{{ cookiecutter.license }}"
    copyright_year = "{{ cookiecutter.copyright_year }}"

    if license == "MIT" and not copyright_year.strip():
        print("You must specify a copyright year for the MIT license")  # noqa: T001
        sys.exit(2)

    if license == "GNU General Public License v3.0" and not copyright_year.strip():
        print(  # noqa: T001
            "You must specify a copyright year for the GNU General Public License v3.0"
        )
        sys.exit(2)

    year_error_msg = "The copyright year entered is not a valid year"
    if copyright_year.strip() and len(copyright_year) != 4:
        print(year_error_msg)  # noqa: T001
        sys.exit(3)
    if len(copyright_year) == 4:
        try:
            int(copyright_year)
        except ValueError:
            print(year_error_msg)  # noqa: T001
            sys.exit(3)


def exit_one(text_check, field_name):
    if not text_check.strip():
        print(f"You must specify a {field_name} to use this template.")  # noqa: T001
        sys.exit(1)


if __name__ == "__main__":
    validate()

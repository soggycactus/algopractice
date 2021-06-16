""" Unique Email Addresses """


def number_unique_emails(emails: list) -> int:
    """
    Returns the number of unique email addresses
    """
    new_emails = []
    for i in emails:
        local, domain = i.split("@")
        first_plus_sign = local.find("+")
        local = list(local[0:first_plus_sign]) if first_plus_sign != -1 else list(local)

        while "." in local:
            local.remove(".")

        new_email = "".join(local) + "@" + domain
        new_emails.append(new_email)

    return len(dict.fromkeys(new_emails).keys())


def main():
    """
    Entrypoint
    """
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    print(number_unique_emails(emails))


if __name__ == "__main__":
    main()

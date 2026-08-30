import re


def extract_emails(input_file, output_file):
    try:
        # Read the input text file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Regular expression pattern for email addresses
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

        # Find all email addresses
        emails = re.findall(email_pattern, text)

        # Remove duplicate emails
        unique_emails = list(dict.fromkeys(emails))

        if unique_emails:
            # Save extracted emails to output file
            with open(output_file, "w", encoding="utf-8") as file:
                for email in unique_emails:
                    file.write(email + "\n")

            print("=" * 45)
            print("          EMAIL ADDRESS EXTRACTOR")
            print("=" * 45)

            print(f"\n{len(unique_emails)} email address(es) found:\n")

            for email in unique_emails:
                print(email)

            print(f"\nEmails saved successfully to '{output_file}'.")

        else:
            print("\nNo email addresses were found.")

    except FileNotFoundError:
        print(f"\nError: '{input_file}' was not found.")


def main():
    input_file = "input.txt"
    output_file = "emails.txt"

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()
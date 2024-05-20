import csv

input_file = "input.txt"
output_file = "output.csv"

with open(input_file, "r") as file:
    records = file.read().split("*DIV*")

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file, delimiter="~")
    writer.writerow(["subreddit", "short_desc", "long_desc", "no_subscribers"])

    for record in records:
        lines = record.strip().split("\n")
        subreddit = lines[0].split(": ")[0]
        short_desc = ": ".join(lines[0].split(": ")[1:])
        long_desc = " ".join(lines[1:len(lines)-1])
        no_subscribers = lines[-1]

        writer.writerow([subreddit.strip(), short_desc.strip(), long_desc.strip(), no_subscribers.strip()])

print("Conversion complete. Output saved to", output_file)

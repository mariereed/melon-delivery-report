def print_delivery_report(day_number, data_file_by_day):
    the_file = open(data_file_by_day)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    the_file.close()

    print "Day {}".format(day_number)
    print "Delivered {} {}s for total of ${}".format(count, melon, amount)
    print


print_delivery_report(1, "um-deliveries-20140519.txt")

print_delivery_report(2, "um-deliveries-20140520.txt")

print_delivery_report(3, "um-deliveries-20140521.txt")

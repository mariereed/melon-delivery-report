def print_delivery_report(day_number, data_file_by_day):
    """Print the name, quantity and total sold in $ of melons Delivered.

    Take in the day number and the corresponding data file (as a string)
    as arguments. Return the printed report in a pleasing format."""
    #Open the data file and save as variable the_file.
    the_file = open(data_file_by_day)
    #Print the day as a heading for each file.
    print "Day {}".format(day_number)
    #For each line, strip the whitespace and split the string into words.
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        #Save the data in corresponding variables.
        melon = words[0]
        count = words[1]
        amount = words[2]

        #Print each line of the file reformated to display the data pleasingly.
        print "Delivered {} {}s for total of ${}".format(count, melon, amount)

    #Close the file    
    the_file.close()

print_delivery_report(1, "um-deliveries-20140519.txt")

print_delivery_report(2, "um-deliveries-20140520.txt")

print_delivery_report(3, "um-deliveries-20140521.txt")

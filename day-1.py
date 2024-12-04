# imports
import polars as pl

# Replace multi-byte separator with single byte seperator before reading
def preprocess_file(file_path, original_separator='   ', new_separator=','):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the actual multi-byte separator with a single byte separator
    processed_content = content.replace(original_separator, new_separator)
    
    # Save or return the processed content
    with open(file_path + '-processed', 'w', encoding='utf-8') as f:
        f.write(processed_content)

# main()
def main ():
    preprocess_file("inputs/day-1/day-1-input-data")
    file_path = "inputs/day-1/day-1-input-data-processed"
    # load data
    df = pl.scan_csv(file_path, separator=",", encoding="utf8", has_header=False).collect()
    # label columns
    df.columns = ["left", "right"]
    # sort
    left_series = df.get_column("left").sort()
    right_series = df.get_column("right").sort()
    # remove dataframe reference
    df = None
    # compute the differece sum # part 1
    total_distance = sum(abs(d1 - d2) for d1, d2 in zip(left_series, right_series))
    print("total distance is: ", total_distance)
    # part 2
    matching_value_check = left_series.is_in(right_series)
    # new df to record the count 
    df = pl.DataFrame({
        "value": left_series,
        "matching_value_check": matching_value_check
    })

    # group by value and sum the boolean values to get the counts occurrences
    count = df.filter(df["matching_value_check"]).group_by("value").count()
    print(count)
    #print(left_series[15])
    # for n in matching_values:
    #     print(n)
    #print(matching_values)

if __name__ == "__main__":
    main()
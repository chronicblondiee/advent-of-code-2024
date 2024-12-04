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
    total_distance = 0
    file_path = "inputs/day-1/day-1-input-data-processed"
    # load data
    df = pl.scan_csv(file_path, separator=",", encoding="utf8", has_header=False).collect()
    # label columns
    df.columns = ["col1", "col2"]
    # sort
    col1_series = df.get_column("col1").sort()
    col2_series = df.get_column("col2").sort()
    # remove dataframe reference
    df = None
    # compute the differece sum
    total_distance = sum(abs(d1 - d2) for d1, d2 in zip(col1_series, col2_series))
    print(total_distance)

if __name__ == "__main__":
    main()
# imports
import polars as pl

# Replace multi-byte separator with a standard space before reading
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
    df = pl.scan_csv(file_path, separator=",", encoding="utf8").collect()
    df.columns = ["col1", "col2"]
    col1_series = df.get_column("col1").sort()
    col2_series = df.get_column("col2").sort()

    print(col1_series)

    #df = df.sort(["col1", "col2"])
    #df = df.sort(["col2"])
    #print(df.select(sorted(df.columns)))



if __name__ == "__main__":
    main()